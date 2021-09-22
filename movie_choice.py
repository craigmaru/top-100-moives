import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century")

movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")

#movies = soup.find_all(name="h2")

movies = soup.select(selector="h2 strong") 

new_list = [movies.getText() for movies in movies]

movie_list = new_list[::-1]

with open("100_days_of_movies.txt", mode="w") as file:
    for i in movie_list:
        file.write(f"{i}\n")
