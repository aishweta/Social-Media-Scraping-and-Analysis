# coding: utf-8
#.Sentiment Analysis
from textblob import TextBlob

class SentimentAnalysis:
    def __init__(self):
        print("Initiating SentimentAnalysis Class")

    def findsentiment(self,val):
        if val<=0.1 and val>-0.1:
            return 'Neutral'
        elif val>0.1:
            return 'Positive'
        else:
            return 'Negative'

    def txtanalysis(self,comments):
        sent = []
        sentVal = []
        for news in comments:
            analysis = TextBlob(news)
            sentiment = self.findsentiment(analysis.sentiment.polarity)
            qq = analysis.sentiment.polarity
            sentVal.append(qq)
            sent.append(sentiment)
        return sent, sentVal

    def avgsentiment(self,comments):
        sent, sentVal = self.txtanalysis(comments)
        totalSent = sum(sentVal)
        avgSent = totalSent/len(comments)
        sent = self.findsentiment(avgSent)
        return avgSent, sent
