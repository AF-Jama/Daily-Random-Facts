from cmath import e
from traceback import print_tb
import tweepy 

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
        print(self.API.verify_credentials())

    def get_tweets(self):
        #get statuses using home_timeline method
        return self.API.home_timeline()

    def delete_tweets(self):
        try:
            count = 1
            for status in tweepy.Cursor(self.API.home_timeline).items():
                '''triggers loop that goes through each status using pagination'''
                print(status)
                id = status. _json['id'] # returns id of tweet
                print("Deleted" + " " + str(id))
                self.API.destroy_status(id) #destroys/deletes tweet
                print("Deleted" + " " + str(id))
                print(count)
                count+=1
        except:
            print("Error")

             

t = TwitterBot()
# t.check()
# print(t.get_tweets()[0]. _json['id'])
t.delete_tweets()