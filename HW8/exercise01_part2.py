import csv

from itertools import groupby
from collections import Counter
from collections import defaultdict

anon_list = []
imdb_list = []
anon_list_name = []
imdb_list_name = []
donald_trump_movies = []
with open('./anon_data/com402-2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        anon_list.append(row)
        anon_list_name.append(row[1])
        line_count += 1
    print(f'Processed {line_count} lines. from com402-2.csv')

with open('./anon_data/imdb-2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        imdb_list.append(row)
        imdb_list_name.append(row[1])
        line_count += 1
        if (row[0] == "donald.trump@whitehouse.gov"):
            donald_trump_movies.append(row)
    print(f'Processed {line_count} lines. from imdb-2.csv')

print()


# Sort the movies by the number of rates in the two files com402-2.csv and imdb-2.csv.
# Create a one to one mapping between these two sorts method, you should get a one to one hash <-> movie name mapping

# # sorting on bais of frequency of elements
result_anon = [item for items, c in Counter(anon_list_name).most_common()
									for item in [items] * c]
result_imdb = [item for items, c in Counter(imdb_list_name).most_common()
								    for item in [items] * c]

anon_freq = list(dict.fromkeys(result_anon))
imdb_freq = list(dict.fromkeys(result_imdb))

print(len(anon_freq), len(imdb_freq)) # should be the same

movie_dict_1 = {}
movie_dict_2 = {}
for i in range(len(anon_freq)):
    movie_dict_1[anon_freq[i]] = imdb_freq[i]
    movie_dict_2[imdb_freq[i]] = anon_freq[i]
    print(i, anon_freq[i], "<->", imdb_freq[i])

print()

donald_trump_movie_hashes = []
for i in range(len(donald_trump_movies)):
    print(donald_trump_movies[i])
    donald_trump_movie_hashes.append(movie_dict_2[donald_trump_movies[i][1]])
    # print(movie_dict_2[donald_trump_movies[i][1]])

donald_trump_movie_hashes_set = set(donald_trump_movie_hashes)

print("Number of Donald trump public rates =",len(donald_trump_movie_hashes_set))
# Find the Donald Trump email hash

user_movies = defaultdict(set)
for i in range(len(anon_list)):
    user_movies[anon_list[i][0]].add(anon_list[i][1])


for userHash, movie_hashlist in user_movies.items():
    found = 0
    for movie in movie_hashlist:
        if (movie in donald_trump_movie_hashes_set):
            found += 1


    if (found >= 18):
        print("\nDonald Trump email hash =", userHash)
        donald_trump_hash = userHash
        print("\nAll movies rated by Donald Trump:")
        i = 0
        for movie_hash in movie_hashlist:
            print('\t',i, movie_dict_1[movie_hash])
            i += 1
        break
