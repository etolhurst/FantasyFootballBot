#python reddit bot

# A Reddit bot that posts explanation of xkcd comic strips posted in comments
# The explanation is extracted from http://explainxkcd.com
# Created by Ayush Dwivedi (/u/kindw)
# License: MIT License

#from bs4 import BeautifulSoup
from urllib.parse import urlparse

import praw
import time
import re
import requests
import bs4

path = '/home/eric/Desktop/python/reddit/commented.txt'
# Location of file where id's of already visited comments are maintained

#header = '**Explanation of this xkcd:**\n'
#footer = '\n*---This explanation was extracted from [explainxkcd](http://www.explainxkcd.com) | Bot created by u/kindw | [Source code](https://github.com/aydwi/explainxkcdbot)*'
# Text to be posted along with comic description

myTeam = ["Aaron Rodgers", "Devonta Freeman", "Ezekiel Elliott", "Jordy Nelson",
          "Michael Crabtree", "Jordan Reed", "Adam Thielen", "Matt Bryant", "Bilal Powell", 
          "Martavis Bryant", "DeSean Jackson", "Adrian Peterson", "Ted Ginn Jr.", "Eddie Lacy", 
          "Martellus Bennett"]

def authenticate():
    
    print('Authenticating...\n')
    reddit = praw.Reddit('fantasyBot', user_agent = 'web:fantasyBot:v0.1')
    print('Authenticated as {}\n'.format(reddit.user.me()))
    return reddit

def run_explainbot(reddit):
    
    print("Getting 250 comments...\n")
    
    for comment in reddit.subreddit('fantasyfootball').comments(limit = 250):
        for player in range(len(myTeam)):
            match = re.findall(myTeam[player], comment.body)
            if match:
                print('Player found in comment with comment ID: ' + comment.id)
                player_url = match[0]
                print('Link: ' + player_url)
            
                file_obj_r = open(path,'r')
                        
                if comment.id not in file_obj_r.read().splitlines():
                    print('Link is unique...posting explanation\n')
                    #comment.reply("player found")
                    msg = 'Comment: ' + comment.body + '\n' + 'Link: ' + comment.permalink(fast=False)
                    reddit.redditor('etolhurst').message('Found Comment About ' + myTeam[player], msg)

                    file_obj_r.close()

                    file_obj_w = open(path,'a+')
                    file_obj_w.write(comment.id + '\n')
                    file_obj_w.close()
                else:
                    print('Already visited link...no message needed\n')
            
        time.sleep(10)

    print('Waiting 1 minute...\n')
    time.sleep(60)


def main():
    reddit = authenticate()
    while True:
        run_explainbot(reddit)


if __name__ == '__main__':
    main()
