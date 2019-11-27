import csv

anon_list = []
imdb_list = []
with open('./anon_data/com402-2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        anon_list.append(row)
        line_count += 1
    print(f'Processed {line_count} lines. from com402-2.csv')

with open('./anon_data/imdb-2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        imdb_list.append(row)
        line_count += 1
    print(f'Processed {line_count} lines. from imdb-2.csv')

print()


#
# # In this exercise I will try to construct a mapping between the hash of the movie and its name
# movie_dict = {}
# for i in range(len(anon_list)):
#     # print("movies rated on", anon_list[i][2])
#     movies_for_date = []
#     for j in range(len(imdb_list)):
#         if (anon_list[i][2] == imdb_list[j][2]):
#             # print("\t", imdb_list[j][1])
#             movies_for_date.append(imdb_list[j])
#
#     if (len(movies_for_date) == 1):
#         movie_dict[anon_list[i][1]] = movies_for_date[0]
#
# # print(movie_dict)
#
# public_donald_trump_movies = []
# donald_trump_email_hash = "" # to be found
# for i in range(len(imdb_list)):
#     if (imdb_list[i][0] == 'donald.trump@whitehouse.gov'):
#         #print(imdb_list[i])
#         rates = []
#         print("Donald Trump rated one of the following movies movies on ", imdb_list[i][2])
#         for j in range(len(anon_list)):
#             if (anon_list[j][2] == imdb_list[i][2]):
#                 print("   ", anon_list[j][1])
#                 rates.append(anon_list[j])
#         if (len(rates) == 1):
#             donald_trump_email_hash = rates[0][0]
#             public_donald_trump_movies.append(rates[0])
#             # print("Found Donald Trump email hash ", donald_trump_email_hash)
#             # break;
#
# print("\nFound Donald Trump email hash ", donald_trump_email_hash)
# print("\nDonald Trump has seen the following movies:")
# k = 0
# for j in range(len(anon_list)):
#     if (anon_list[j][0] == donald_trump_email_hash):
#         print("\t", k, movie_dict[anon_list[j][1]][1])
#         k += 1

# print("\nSecret movies rated by (Donald Trump) hash=", donald_trump_email_hash)
# secret_donald_trump_movies = []
# k = 0
# for j in range(len(anon_list)):
#     if (anon_list[j][0] == donald_trump_email_hash):
#         if (anon_list[j] not in public_donald_trump_movies):
#             secret_donald_trump_movies.append(anon_list[j])
#             print("   ", k, "Movie hash :", anon_list[j][1], "date", anon_list[j][2])
#             k += 1

# print()
# for i in range(len(all_donald_trump_movies)):
#     for j in range(len(imdb_list)):
#         if (all_donald_trump_movies[i][2] == imdb_list[j][2]):
#             print(imdb_list[j][1])


# for i in range(len(donald_trump_movies)):
#     for j in range(len(anon_list)):
#         if (anon_list[j][1] == donald_trump_movies[i] and anon_list[j][0] != donald_trump_email_hash):
#             print("Movie ", donald_trump_movies[i], "was rated by", anon_list[j][0] , "too.")
