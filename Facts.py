import requests
import json
import random
from datetime import datetime
import tweepy


class FactFetcher:
    '''fetches random facts using API'''
    def __init__(self) -> None:
        self.BASE = "https://uselessfacts.jsph.pl/" #base url

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

    def choose(self):
        '''method randomly chooses what type of fact is retrieved'''
        list = [self.today(),self.random()]
        return random.choice(list) # returns class method from list,return type is string



class TwitterBot:
    def __init__(self) -> None:
        '''Keys are initalised here when an object is created'''
        APIKEY  = "F6AMMqXJY5BstWnU5dQKF6l3Z"
        KEYSECRET = "xCQvK8a9Ntxz60Z1RCcdeKQjawfJGFCDvPb379kHIjQWvCxAgE"
        BK = "AAAAAAAAAAAAAAAAAAAAAJ2BYgEAAAAASxgTRoUzE%2FG866sHUTqL41oT2Cs%3DwzbGyDoCcUjJuM2Rkm5siJGhyMVe7YBD381pc72AXhBKW9hW5C"
        AK = "1486796514815102986-q17H0xRXWoz0Sn5Ulbt6of8TjrCgvl"
        AKS = "ogMvkLJLrz3Ya9pkSwHNa3nl8gJZZZdPSb6HvfF9suQsF"
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
        self.API.update_status(message)


    def schedule(self):
        '''logic for scheduling tweet a 5pm uk time and 12 pm est'''
        f = FactFetcher()
        date_now = datetime.now()
        hour_now = datetime.strftime(date_now,"%H")
        minute_now = datetime.strftime(date_now,"%M")
        second_now = datetime.strftime(date_now,"%S")
        if hour_now == '17' and minute_now == '00' and second_now == '01':
            #triggered update status if evaluates to True
            self.API.update_status(f.choose()) # updates status/tweeting at 5pm

        else:
            #triggered when if statement does not evaluate to True
            pass


    def run(self):
        #runs logic in loop and triggers when condition is met
        count = 1
        while True:
            self.schedule()
            


# t = TwitterBot()
# t.check()
# t.run()



if __name__ == '__main__':
    t = TwitterBot()
    t.check()
    t.API.update_status("Bot has Deployed")
    t.run()
