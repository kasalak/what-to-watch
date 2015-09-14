import csv

all_movies = {} # Movie objects go in here
all_users = {} #  User objects go in here

class User:

    def __init__(self, user_id):
        self.id = user_id
        all_users[self.id] = self
        self.ratings = {}


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
