# coding: utf-8
import requests
import pandas as pd
import numpy as np
import langid
import time

class YoutubeScrapper:
    def __init__(self):
        print("Started Youtube Scapper")

    def youtubescrapper(self,youtubeapi,kpram,youtubecommentapi,vparams):
        params = (
            ('key', kpram['key']),
            ('part', kpram['part']),
            ('type', kpram['type']),
            ('maxResults',kpram['maxResults']),
            ('q', kpram['q']),
            ('relevanceLanguage', kpram['relevanceLanguage']), #is not guaranteed to work
        )
        response = requests.get(youtubeapi, params=params)
        response_json=response.json()

        # Extract Video names
        channel_ids = []
        videoid_name = {}
        for i in range(len(response_json['items'])):
            channel_ids.append(response_json['items'][i]['snippet']['channelId'])
            videoid_name[response_json['items'][i]['snippet']['title']] = response_json['items'][i]['id']['videoId']

        #Extract video ID's for Vedio names
        videos_required=[]
        for name in videoid_name.keys():
            videos_required.append(videoid_name.get(name))

        comments=[]
        video_id = []
        for video in videos_required:

            params_v = (
                ('key',vparams['key'] ),
                ('part', vparams['part']),
                ('videoId', video),
                ('maxResults', vparams['maxResults']),
            )

            response_v = requests.get(youtubecommentapi, params=params_v)
            response_json_v=response_v.json()


            for i in range(len(response_json_v['items'])):
                comments.append(response_json_v['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'])
                video_id.append(response_json_v['items'][i]['snippet']['topLevelComment']['snippet']['videoId'])
            time.sleep(3)
            return comments, video_id

    