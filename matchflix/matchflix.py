# -*- coding: utf-8 -*-

# Netflix Match App by Caitlin

# Imports

#import requests, json, csv, os
import helpers

# Main Application

def main():
    genres = helpers.get_genres()
    helpers.greeting()
    output = helpers.get_input(genres.values(), 1)

    print(helpers.responseMessage(output))

    movies_output = helpers.get_input(helpers.likedMovies(output, helpers.findMovies()), 2)

    helpers.outputMessage(movies_output)

main()