# coding: utf-8
import params
import pandas as pd
from Scrapper.GoogleScrapper import GoogleScrapper
from Scrapper.BlogScrapper import BlogScrapper
from Scrapper.YoutubeScrapper import YoutubeScrapper
from SentimentAnalysis import SentimentAnalysis
import os

def main():
    DataPath ='{}/Data'.format(params.homepath)

    youtubeapi = params.youtubeapi
    youtubecommentapi = params.youtubecommentapi
    kpram = params.youtubeparams
    vparams = params.params_v

    Sentiment = SentimentAnalysis()


    youtube=YoutubeScrapper()
    comments , video_id = youtube.youtubescrapper(youtubeapi,kpram,youtubecommentapi,vparams)
    sent, sentVal = Sentiment.txtanalysis(comments)
    d = {'comments':comments,'video_id':video_id,'label':sent,'sentVal':sentVal}
    df = pd.DataFrame(d) #creates empty dataframe
    filename = os.path.join(DataPath, params.youtubefilename).replace("\\","/")
    df.to_csv(filename)
    print('Youtube Average Sentiment:',Sentiment.avgsentiment(comments))


    url = params.newsurl #'https://news.google.com/?output=rss&q='
    symbol = params.newssymbol
    Google = GoogleScrapper()
    links, titles = Google.Google_Scrap(url,symbol)
    news = Google.Google_newsStoryGrabber(links)
    #seenews = Google_seeNews(titles,links)
    #print(seenews)
    sent, sentVal  = Sentiment.txtanalysis(news)
    d = {'links':links, 'news':news,'titles':titles,'label':sent,'sentVal':sentVal}
    df = pd.DataFrame(d) #creates empty dataframe
    filename = os.path.join(DataPath, params.newsfilename).replace("\\","/")
    df.to_csv(filename)
    print('Google News Average Sentiment:' , Sentiment.avgsentiment(news))


    blogurl = params.blogurl #"https://www.narendramodi.in/blog/loadblogs?language=en&page="
    Blog =BlogScrapper()
    links, titles = Blog.blog_parser(blogurl)
    text = Blog.blog_newsStoryGrabber(links)
    #seenews = BlogScrapper.blog_seeNews(links)
    #print(seenews)
    sent, sentVal  = Sentiment.txtanalysis(text)
    d = {'links':links, 'text':text,'titles':titles,'label':sent,'sentVal':sentVal}
    df = pd.DataFrame(d) #creates empty dataframe
    filename = os.path.join(DataPath, params.blogfilename).replace("\\","/")
    df.to_csv(filename)
    print('Blogs Average Sentiment:', Sentiment.avgsentiment(text))


if __name__=='__main__':
    main()