# -*- coding: utf-8 -*-

# Netflix Match App by Caitlin

# Imports

#import requests, json, csv, os
import helpers

# Main Application
# Runs helper functions in sequence

def main():
    helpers.greeting()

    genres = helpers.get_genres()
    output = helpers.get_input(genres.values(), 1)

    print(helpers.responseMessage(output))

    movies_output = helpers.get_input(helpers.likedMovies(output, helpers.findMovies(genres)), 2)

    print(helpers.outputMessage(movies_output))

main()