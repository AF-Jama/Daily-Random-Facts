import requests
import json
import random
from datetime import datetime
import tweepy
import time
from config import configuration


class FactFetcher:
    '''fetches random facts using API'''
    def __init__(self) -> None:
        self.BASE = "https://uselessfacts.jsph.pl" #base url

    def random(self):
        '''get request to return'''
        request = requests.get(self.BASE + "/random.json?language=en")
        request = request.json()
        return request['text']

    def today(self):
        '''get request to return'''
        request = requests.get(self.BASE + "/today.json?language=en")
        request = request.json()
        return request['text']

    # def choose(self):
    #     '''method randomly chooses what type of fact is retrieved'''
    #     list = [self.today(),self.random()]
    #     return random.choice(list) # returns class method from list,return type is string



class TwitterBot:
    fact_set = set() # creates set to store facts to ensure there are no duplicates
    def __init__(self) -> None:
        '''Keys are initalised here when an object is created'''
        APIKEY,KEYSECRET,BK,AK,AKS = configuration.values()
        auth = tweepy.OAuth1UserHandler(APIKEY,KEYSECRET,AK,AKS)
        self.API = tweepy.API(auth) # Creates Twitter API object

    def check(self):
        try:
            self.API.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")

    def tweet_now(self,message):
        #tweet contains a random fact so composition can be used
        try:   
            if message not in TwitterBot.fact_set:
                '''triggers block if message is not already in set of unique tweets'''
                print("Tweeted")
                self.API.update_status(message)
                TwitterBot.fact_set.add(message) # appends message into list 
                time.sleep(300.0)

            else:
                '''triggered if message is in set which signifies it has already been tweeted'''
                pass    

        except:
            '''if any exception is triggered when updatating status/tweeting it will just be passed. most common exception is 187 - Status is a duplicate. '''
            pass


    def schedule(self):
        '''logic for scheduling tweet a 5pm uk time and 12 pm est'''
        f = FactFetcher()
        date_now = datetime.now()
        hour_now = datetime.strftime(date_now,"%H")
        minute_now = datetime.strftime(date_now,"%M")
        second_now = datetime.strftime(date_now,"%S")
        if int(minute_now) %5 == 0:
            #triggered update status if evaluates to True
            self.tweet_now(f.random()) # updates status/tweeting at 5pm

        else:
            #triggered when if statement does not evaluate to True
            pass


    def run(self):
        while True:
            self.schedule()
            




# if __name__ == '__main__':
t = TwitterBot()
t.check()
t.run()