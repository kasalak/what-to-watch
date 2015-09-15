from movie_lib import *

ebert = User(5)
siskel = User(12)
movie1 = Movie(3, "Toy Story")
movie2 = Movie(9, "Pretty Woman")

print(all_movies)

rating1 = Rating(siskel.id, movie1.id, 4)
rating2 = Rating(ebert.id, movie2.id, 1)
rating3 = Rating(siskel.id, movie2.id, 3)
rating4 = Rating(ebert.id, movie1.id, 1)

def test_user_creation():
    assert ebert.id ==5
    assert siskel.id ==12

def test_movie_creation():
    assert movie1.id == 3
    assert movie1.title == 'Toy Story'
    assert movie2.id == 9
    assert movie2.title == 'Pretty Woman'

def test_rating_creation():
    assert rating1.user_id == rating3.user_id == siskel.id
    assert rating2.user_id == rating4.user_id == ebert.id
    assert rating1.movie_id == rating4.movie_id == movie1.id
    assert rating2.movie_id == rating3.movie_id == movie2.id
    assert rating1.stars == 4
    assert rating2.stars == 1
    assert rating3.stars == 3
    assert rating4.stars == 1

def test_find_ratings_for_movie():

    #return a list of Rating objects
    toy_story_ratings =all_movies[movie1.id].get_ratings()
    print (len(toy_story_ratings))
    print(toy_story_ratings)
    assert len(toy_story_ratings) == 2

def test_find_ratings_for_user():
    siskels_ratings = all_users[siskel.id].get_ratings()
    print(siskels_ratings)
    assert len(siskels_ratings) == 2

# def test_get_average_rating_for_movie():
#     print(movie1.get_average_rating())
#     assert movie1.get_average_rating == 2.5
#     assert movie2.get_average_rating == 2 #every int can be compared to float



# def test_find_movies_by_id():
#     toy_story_id = all.movies[movie_title].get_ratings()
#     print(toy_story)
