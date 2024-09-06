import requests
import json
import os
"""
Choose an API from RapidAPI that interests you—make sure it has a free tier and simple authentication. 
Write a Python script that makes a request to your selected API, using the appropriate endpoint and parameters to retrieve data. 
Save the response data to a variable, and handle it as JSON to work with nested structures. 
Extract a specific item from the nested dictionary in the response, and print a statement that meaningfully displays this information.
"""
api_key = os.getenv('API_KEY')
#the search suggestion function will process the user request
#in this function, keywords and type search are aruguments from main function. They are from the user input
#the end point in search suggesstion funtion is for giving suggestions from youtube music
def search_suggestions(keywords, type_search):
    url = "https://youtube-music-api3.p.rapidapi.com/search_suggestions"

    #here is the parameter for searching, only one paramenter used for search request which is the words that user input
    querystring = {"q":keywords}

    #Following is the API key, please replace these with your own API key
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "youtube-music-api3.p.rapidapi.com"
    }

    #store the response fron GET request to a variable called "repsonse". url, headers and querystring are parameters required for GET request
    response = requests.get(url, headers=headers, params=querystring)

    #here using json format to view the data
    music_data = response.json()
    #formatted_music_data = json.dumps(music_data, indent = 4)
    #print(formatted_music_data)
    
    #the "found" variable here is going to be used for showing the result. If youtube music can not give the suggestion based on user input, then "found" will be false
    found = False
    
    # to get the result that user want depends on their input
    for item in music_data["items"]:
        if(type_search == "all"):
            found = True
            #output example: Searched the Hello for you. Search details: Song • Adele • 3.3B plays
            print(f"Searched the {item["title"]} for you. Search details: {item["subtitle"]}")
        if(item["type"] == type_search):
            found = True
            print(f"Searched the {item["title"]} for you. Search details: {item["subtitle"]}")
    if(found == False):
        print(f"Sorry, we didn't find any {type_search} for you at this moment :(")

#This function is when user want to search an item from all songs, albums, podcasts from Youtube
#if the user has the author or song that they want to search, this function can help them to match
def search(search, type, song_name, author):
    url = "https://youtube-music-api3.p.rapidapi.com/search"

    querystring = {"q":search,"type":type}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "youtube-music-api3.p.rapidapi.com"
    }

    
    response = requests.get(url, headers=headers, params=querystring)
    music_data = response.json()
    #formatted_music_data = json.dumps(music_data, indent = 4)
    #print(formatted_music_data)
    #get the first layer
    results = music_data.get("result")
    #iterate elements in the results list
    print(f"Here is the searching results for you: \n")
    
    #this is a flag to handle the case for not find anything to match
    found = False
    if(song_name == "n" and author == "n"):
        for result in results:
            print(f"{result.get("title")} by {result.get("author")}")
            found = True
    elif(song_name == "n"):
        for result in results:
            if(result.get("author") == author):
                print(f"{result.get("title")} by {result.get("author")}")
                found = True
    elif(author == 'n'):
        for result in results:
            if(result.get("title") == song_name):
                print(f"{result.get("title")} by {result.get("author")}")
                found = True
    else:
        for result in results:
            if(result.get("title") == song_name and result.get("author") == author):
                print(f"{result.get("title")} by {result.get("author")}")
                found = True
    if not found:
        print("Sorry, there is no result matched :(n")

    
    
action = input("Would you like to explore the suggestions? y/n \t")


#For this script, I've used two APIs to handle two different requests from user.
#The user can search from the suggestion list or can search from the whole library.

match action: 
    case "y":
        print("Welcome! Your can search songs from suggestions :)\n")
        type_search = input("Are you looking for songs or albums? \nPlease enter 'songs' for songs, 'albums' for albums, 'all' for all searching results.\n")  
        keywords = input("Enter any words to get suggestion: \n")
        search_suggestions(keywords, type_search)
    case "n":
        search_name = input("What would you like to search? \n")
        type_search = input("What is the type? Select from song, videos, albums, artists, featured_playlists, community_playlists, and podcasts\n")
        song_name = input("Are you looking for a particular song? If no, please enter n\n")

        author = input("Are you looking for any author? If no, please enter n \n")
        search(search_name, type_search, song_name, author)
        



