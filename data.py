import requests
from bs4 import BeautifulSoup

# List of websites:
# 1. Epicurious

# Problems:
# None (for now)


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

    def filter_items(self, titles, links):
        """filter_items(titles, links) = Get a dictionary {"title": "links"} free from duplicates"""
        import pprint

        if len(titles) == len(links):
            dictionary = {titles[i]: links[i] for i in range(len(titles))}

            for i in list(dictionary):
                if len(i) <= 10:
                    del dictionary[i]
            else:
                pprint.pprint(dictionary)
