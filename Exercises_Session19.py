# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 20:57:44 2018

@author: Leila
"""

#%%
    
#Create a function that uses the requests library to get the lyrics of a song.
#You can use the lyrics.ovh api as described here: 
#https://lyricsovh.docs.apiary.io/#reference/0/lyrics-of-a-song/search?console=1

import requests

lyrics = requests.get("https://api.lyrics.ovh/v1/Mariah Carey/Hero").json()

print(lyrics)

#%%

#Create a function that returns the current latitude and longitude of the ISS
#http://api.open-notify.org/

import requests

ISS = requests.get("http://api.open-notify.org/iss-now.json").json()

print(ISS["iss_position"]["longitude"])
print(ISS["iss_position"]["latitude"])

#%%

#using the given population API, create a program that:
#
#- gets a list of all available countries
#
#- Gets the first 10 countries
#
#- Gets the country's today & tomorrow population.
#
#http://api.population.io/#!/countries/listCountries

import requests

all_countries = requests.get("http://api.population.io:80/1.0/countries").json()

print(all_countries)