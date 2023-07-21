import webbrowser

search_string = input("Enter the item you want to search::  ")

webbrowser.open("https://www.google.com/search?q="+search_string, new=2)