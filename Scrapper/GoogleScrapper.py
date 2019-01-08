# coding: utf-8
import urllib,  urllib.request
import urllib.parse
from lxml import etree
import datetime
from xml.dom.minidom import parseString
import lxml                                               
from bs4 import BeautifulSoup as bs 
from newspaper import Article
import pandas as pd
import os, re, os.path
from urllib.request import urlopen
import bs4
from bs4 import BeautifulSoup as soup


class GoogleScrapper:
    def __init__(self):
        print("Started Google Scrapping Engine")

    def Google_Scrap(self,url,symbol):
        #stock symbol you want to download news for
        #symbol = symbol
        #this is the url where we grab the data
        # 'https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en&q='
        #url = "https://news.google.com/?output=rss&q="

        #use urllib2 to download the data
        response = urllib.request.urlopen(url + symbol)
        xml = response.read()
        #turn into an xml doc
        doc = etree.fromstring(xml)
        #we're only interested in tags under <item>
        item_tags = doc.xpath('//channel/item')
        links = []
        date = []
        titles = []
        for item in item_tags:
            #split up by the four tags
            date_tag = item.xpath('pubDate')
            title_tag = item.xpath('title')
            link_tag = item.xpath('link')
            description_tag = item.xpath('description')
            date_text = date_tag[0].text
            title_text = title_tag[0].text
            link_text = link_tag[0].text
            description_text = description_tag[0].text

            links.append(link_text)
            date.append(date_text)
            titles.append(title_text)

            #print('date:' + date_text)
            #print('title:' + title_text)
            #print('link:' + link_text)
            #print('description:' + description_text)
        return links , titles

    def Google_newsStoryGrabber(self,links):   # Use the Links list to goto the site and get the first two
        data = []
        for i in range(len(links)):
            try:
                article = Article(links[i])
                article.download()
                article.parse()
                a= article.text
                content = " ".join(a.replace(u"\xa0", " ").strip().split())
                data.append(content)
            except Exception as e:
                print(e)
                content = "failed with HTTPSConnectionPool"
                data.append(content)
                pass
        return data

    def Google_seeNews(self,titles,links):
        stories = newsStoryGrabber(links)
        for i in range(len(titles)):
            print(titles[i] + '\n' + stories[i]+ ' \n')
            print('________________________________________\n')
