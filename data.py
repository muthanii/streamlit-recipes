import requests
from bs4 import BeautifulSoup

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

    def get_links(self, soup):
        """get_links(soup) = Get links from a specified soup (search result)"""
        links = []
        for link in soup:
            links.append("https://epicurious.com" + link.attrs["href"])
        return links

    def filter_links(self, links):
        filtered_links = []
        for i in links:
            if "https://epicurious.com/recipes/" in i:
                filtered_links.append(i)
        else:
            result = []
            result.append(filtered_links[0])
            for i in filtered_links:
                if i in result:
                    pass
                else:
                    result.append(i)
        return result
