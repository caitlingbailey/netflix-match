# -*- coding: utf-8 -*-

# Netflix Match App by Caitlin

# Imports

import requests, json, csv, os

# Credentials

api_key = "04b2253f2a386ad7e8fcc3104c69531e"

# Genres Function

def get_genres():
  query = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
  response = requests.get(query)
  
  if response.status_code == 200:
    array = response.json()
    genres = {}
    for i in array['genres']:
      genres[i['id']] = i['name']
    return genres

  else:
    return ("error")

# Introduction Function

def greeting():
  print("Hi there! Struggling to find a movie to watch? Let us help!")
  print(".")
  print(".")
  print(".")
  print(".")
  print("Simply type y or n in response to each of the questions, and your partner will do the same.")
  print(".")
  print(".")
  print(".")
  print(".")

# User Input

def get_input(choices, stage):
  '''
  Takes input from two users and returns the intersection. Second argument is 1/2 for genres or movies.  
  '''
  
  # User Input
  user1 = []
  print("\nFirst User\n")

  for choice in choices:
    if stage == 1:
      user_input = input(f"Do you want to watch a {choice} movie? " )
    elif stage == 2:
      user_input = input(f"Do you want to watch {choice}? " )

    if user_input == "y":
      user1.append(choice)

  # User 2 Input
  user2 = []
  print("\nSecond User\n")

  for choice in choices:
    if stage == 1:
      user_input = input(f"Do you want to watch a {choice} movie? " )
    elif stage == 2:
      user_input = input(f"Do you want to watch {choice}? " )

    if user_input == "y":
      user2.append(choice)
  
  return list(set(user1).intersection(user2))

# Matching Genres

def responseMessage(genres):
  '''
  Depending on the matched genres, returns a string.
  '''
  print("\n")
  if len(genres) == 1:
    return "You should watch " + genres[0] + "!\n" 
  elif len(genres) == 2:
    return "You should watch " + genres[0] + " or " + genres[1] + "!\n"
  elif len(genres) >= 3:
    message = "You should watch "
    for i in range(len(genres) - 1):
      message = message + genres[i] + ", "
    message = message + " or " + str(genres[-1]) + ".\n"
    return message
  else:
    return "Maybe you should go for a walk?\n"

# Find Trending Movies based on their genres

def findMovies():
  query2 = f"https://api.themoviedb.org/3/trending/movie/day?api_key={api_key}"

  response = requests.get(query2)
  response.json()

  movie_choices = {}

  for title in response.json()['results']:
    movie_genres = []

    for genre in title['genre_ids']:
      movie_genres.append(genres[genre])
    movie_choices[title['original_title']] = movie_genres

  return movie_choices

def likedMovies(genres, movie_choices):

  movies_list = []
  for key, value in movie_choices.items():
    if set(genres).intersection(value):
      movies_list.append(key)

  return movies_list

# Testing Functions

def main():
  genres = get_genres()
  greeting()
  output = get_input(genres.values(), 1)

  print(responseMessage(output))

  movies_output = get_input(likedMovies(output, findMovies()), 2)

  print("\nYou should watch:")

  for movie in movies_output:
    print("- " + movie)

main()