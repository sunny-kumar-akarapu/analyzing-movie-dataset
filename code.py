# --------------
from csv import reader


def explore_data(dataset, start, end, rows_and_columns=False):
    if rows_and_columns==True:
        print(len(dataset),len(dataset[0]))
        print("="*10)
    for i in range(10):
        lst=dataset[i]
        print(lst[start:end])
        print("="*25)
    """Explore the elements of a list.
    Print the elements of a list starting from the index 'start'(included) upto the index 'end'         (excluded).
    
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes binary          values, either True or False. If true, print the dimension of the list, else dont.
    """
    
    
        
     


def duplicate_and_unique_movies(dataset, index_):
    # return list(set(tuple(sorted(index_) for index_ in dataset)))
    duplicateMovieslist=[]
    count=0
    for i in range(0,len(dataset)):
        for j in range(i+1,len(dataset)):
            if(dataset[i][index_]==dataset[j][index_]):
                count+=1
                duplicateMovieslist.append(dataset[i][index_])
    return duplicateMovieslist
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or duplicated based     on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for duplicacy 
    
    """
    
    


def movies_lang(dataset, index_, lang_):
    movies_=[]
    for i in range(0,len(dataset)):
        if dataset[i][index_]==lang_:
            movies_.append(dataset[i])
    """Extract the movies of a particular language.

    Of all the movies available in all languages, this function extracts all the movies in a            particular laguage.
    Once you have extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    
    """
    
    return movies_
    



def rate_bucket(dataset, rate_low, rate_high):
    rated_movies=[]
    for i in range(0,len(dataset)):
        num=float(dataset[i][11])
        if rate_low<=num :
            rated_movies.append(dataset[i])
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.
    
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """

    
    return rated_movies

# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)

print(len(movies))
# The first row is header. Extract and store it in 'movies_header'.
movies_header=movies[0]
print(len(movies_header))
print(movies_header)
# Subset the movies dataset such that the header is removed from the list and store it back in movies
movies = movies[1:len(movies)]
print(len(movies))
# Delete wrong data
dellist=[]
for i in range(len(movies)):
    for j in range(len(movies[0])):
        if(movies[i][j]=='' ):
            dellist.append(i)
print(dellist,len(dellist))

for i in reversed(range(len(dellist))):
    print(i)
    del movies[i]
# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.


# Using explore_data() with appropriate parameters, view the details of the first 5 movies.

dupmovies=duplicate_and_unique_movies(movies, 13)
# print(dupmovies)
# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.

#duplicate_and_unique_movies(movies,13)


# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.

review_max=dict()
for i in range(len(dupmovies)):
    value=[]
    key=dupmovies[i]
    for j in range(len(movies)):
        if movies[j][13]==key:
            value.append(int(movies[j][12]))
    #print(review_max[key])
    #value=value.append(review_max[key])
    #print(value)
    review_max[key]=max(value)
        # else:
    # if !review_max[key]:
    #     review_max[key]=value
    # elif review_max[key]<value:
    #     review_max[key]=value
# print(review_max)
# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 
movies_clean=[]
cleandel=[]
for i in range(len(movies)):
    for key in review_max:
        if movies[i][13]==key:
            if int(movies[i][12])<review_max[key]:
                #print(movies[i][13],i,movies[i][12])
                cleandel.append(i)
                #del movies[i]
for i in cleandel:
    del movies[i]
#print(len(cleandel))
movies_clean=movies
# dupmovies=duplicate_and_unique_movies(movies_clean, 13)
# print(dupmovies)

# Calling movies_lang(), extract all the english movies and store it in movies_en.
movies_en=movies_lang(movies_clean,3,'en')
# Call the rate_bucket function to see the movies with rating higher than 8.
high_rated_movies=rate_bucket(movies_en,8,10)



