import requests
from bs4 import BeautifulSoup

# List of websites:
# 1. Epicurious

# Problems:
# 1. Getting duplicate titles and links


# Epicurious Website Class 
class Epicurious:
    
    def __init__(self, search):
        self.search = search 
    
    def get_soup(self):
        """get_soup() = Get soup (HTML contents that have <a> tag and with wanted class)"""
        src = requests.get(f"https://www.epicurious.com/search/{self.search}").content
        soup = BeautifulSoup(src, "lxml")
        recipes = soup.find_all("a", {"class": "view-complete-item"})
        return recipes
    
    def get_titles(self, soup):
        """get_titles(soup) = Get titles from a specified soup (search result)"""
        titles = []
        for title in soup:
            titles.append(title.text[4:])
        return titles

    def get_links(self, soup):
        """get_links(soup) = Get links from a specified soup (search result)"""
        links = []
        for link in soup:
            links.append("https://epicurious.com" + link.attrs["href"])
        return links

    # def get_duplicates(self, data):
    #     duplicates = {}
    #     for key, value in data.items():
    #         duplicates.setdefault(value, set()).add(key)
    #     result = filter(lambda x: len(x)>1, duplicates.values())
    #     return list(result)
