import csv
import math

all_movies = {} # Movie objects go in here
all_users = {} #  User objects go in here

class User:

    def __init__(self, user_id):
        self.id = user_id
        all_users[self.id] = self
        self.ratings = {}

    def add_rating(self, rating):
        self.ratings[rating.movie_id] = rating

    def get_ratings(self):
        return self.ratings.values()


    #def similar_users_list(self)



class Movie:

    def __init__(self, movie_id, title, **kwargs):
        self.id = movie_id
        self.title = title
        self.ratings = {}
        all_movies[self.id] = self #when a Movie object is created, will go in the dictionary all_movies
        #self.ratings = {} # key: user_id, #value: Rating object


    def add_rating(self, rating):
        self.ratings[rating.user_id] = rating

    def get_ratings(self):
        return self.ratings.values() # look at ipython in terminal, pretty cool

    def get_average_rating(self):
        return sum(self.get_rating)
    def __str__(self):
        return 'Movie(movie_id={}, title={})'.format(self.movie_id, repr(self.title))

    def ___repr__(self):
        return self.__str__()

class Rating:
    def __init__(self, user_id, movie_id, stars):
        #stars represents rating
        self.user_id = user_id
        self.movie_id = movie_id
        self.stars = stars

        all_movies[self.movie_id].add_rating(self)
        #all_users[self.user_id].add_rating(self)

    def __str__(self):
        return "Rating(user_id ={}, movie_id = {}, rating = {} stars).".format(self.user_id, self.movie_id, self.stars)
    def __repr__(self):
        return self.__str__()


def movie_list():
    with open('u.item', encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=('movie_id', 'movie_title', " ", " ", "something else"), delimiter = '|')
        for row in reader:
            Movie(row('movie_id'), row('movie_title'))
def user_list():
    with open('u.user') as f:
        reader = csv.DictReader(f, fieldnames='user_id', delimiter = '|')
        for row in reader:
            User(row('user_id'))
def ratings_list():
    with open('u.data') as f:
        reader = csv.DictReader(f, fieldnames=('user_id', 'movie_id', 'rating'), delimiter = 'space')
        for row in reader:
            Rating(row('user_id'), row('movie_id'), row('rating'))
def get_top_fifty(num=50, all_movies =all_movies):
    top_movies = {}
    for x in all_movies:
        if len(all_movies[x].get_movie_ratings()) > 5:
            top_movies[x] = all_movies[x].get_average_rating()

def euclidean_distance(user_1, user_2):
    """Given two lists, give the Euclidean distance between them on a scale
    of 0 to 1. 1 means the two lists are identical.
    """
    # Guard against empty lists.
    if len(user_1) is 0:
        return 0
    # Note that this is the same as vector subtraction.
    differences = [user_1[idx] - user_2[idx] for idx in range(len(v))]
    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)
    return 1 / (1 + math.sqrt(sum_of_squares))
