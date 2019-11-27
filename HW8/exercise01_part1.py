import csv

anon_list = []
imdb_list = []
# Reading .csv files into lists
# anonimized db/.csv file
with open('./anon_data/com402-1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        anon_list.append(row)
        line_count += 1
    print(f'Processed {line_count} lines. from com402-1.csv')

# plain text db/.csv file
with open('./anon_data/imdb-1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        imdb_list.append(row)
        line_count += 1
    print(f'Processed {line_count} lines. from imdb-1.csv')

print()

# In this exercise I will use a mapping between the hash of the movie and its plain text name
# by exploiting the fact that for some dates, only one movie was rated.
movie_dict = {}
for j in range(len(imdb_list)):
    # print("movies rated on", anon_list[i][2])
    movies_for_date = []
    for i in range(len(anon_list)):
        if (anon_list[i][2] == imdb_list[j][2]):
            # print("\t", imdb_list[j][1])
            movies_for_date.append((anon_list[i][1], imdb_list[j][1]))

    if (len(movies_for_date) == 1): # Only one movie was rated on imdb_list[j][2]
        movie_dict[movies_for_date[0][0]] = movies_for_date[0][1]

# print(movie_dict)

public_donald_trump_movies = []
donald_trump_email_hash = "" # to be found
for i in range(len(imdb_list)):
    if (imdb_list[i][0] == 'donald.trump@whitehouse.gov'):
        #print(imdb_list[i])
        rates = []
        print("Donald Trump rated:")
        for j in range(len(anon_list)):
            if (anon_list[j][2] == imdb_list[i][2]):
                print("   ", anon_list[j][1])
                rates.append(anon_list[j])
        if (len(rates) == 1):
            print("There is only one movie rated on", imdb_list[i][2], ". Only Donald Trump rated movies in this day ===> privacy--, hacking++")
            donald_trump_email_hash = rates[0][0]
            public_donald_trump_movies.append(rates[0])
            print("Found Donald Trump email hash ", donald_trump_email_hash)
            break;

print("\nDonald Trump has seen the following movies:")
k = 0
# use the hash->movieName mapping to find out all the movies that Donald Trump has seen
f = open("./results/ex_01_part01.txt", "w")
f.write(donald_trump_email_hash + "\n")
for j in range(len(anon_list)):
    if (anon_list[j][0] == donald_trump_email_hash):
        print("\t", k, movie_dict[anon_list[j][1]])
        f.write(anon_list[j][1] + "," + movie_dict[anon_list[j][1]]+"\n")
        k += 1


f.close()
