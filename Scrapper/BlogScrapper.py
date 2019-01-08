# coding: utf-8
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import lxml
import urllib.request
import pandas as pd
import numpy as np

class BlogScrapper:
    def __init__(self):
        print("Start Blog Scrapper:")

    def blog_parser(self,Mainurl):
        titles = []
        links = []
        for i in range(5):
            #Mainurl = "https://www.narendramodi.in/blog/loadblogs?language=en&page="
            url = Mainurl + str(i)
            content = urlopen(url)
            soup = bs(content, "lxml")
            for link in soup.find_all('h3'):
                titles.append(link.text)
                #print(link.a['href'])
                links.append(link.a['href'])
        return links, titles

    def blog_newsStoryGrabber(self,links):
        text = []
        for link in links:
            content = urlopen(link)
            soup = bs(content, "lxml")
            article = soup.find("div", {"class":"content"}).findAll('p')
            text.append(str(article))
        return text

    def blog_seeNews(self,links):
        for link in links:
            content = urlopen(link)
            print("-----------------------------------")
            soup = bs(content, "lxml")
            article = soup.find("div", {"class":"content"}).findAll('p')
            for element in article:
                article_text = ''.join(element.findAll(text = True))
                print(article_text)



    