from movie_lib import *
import csv

def import_items():
#"""This function will import movie list, and then read it"""
    with open('u.item', encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=['movie_id','movie_title'],delimiter = '|')
        for row in reader:
            Movie(row['movie_id'], row['movie_title'])
    print(list(all_movies.values())[:20])

import_items()
