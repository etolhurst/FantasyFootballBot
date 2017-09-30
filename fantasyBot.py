#python fantasy football reddit bot

# A Reddit bot that sends a message to my personal reddit account every time
# a player from my fantasy football team is mentioned in a comment on 
# r/fantasyfootball
#
# Eric Tolhurst
# September 2017

import praw
import time
import re
import requests

path = '/home/eric/Desktop/python/reddit/commented.txt'

myTeam = ["Aaron Rodgers", "Devonta Freeman", "Ezekiel Elliott", "Jordy Nelson",
          "Michael Crabtree", "Jordan Reed", "Adam Thielen", "Matt Bryant", "Bilal Powell", 
          "Martavis Bryant", "DeSean Jackson", "Adrian Peterson", "Ted Ginn Jr.", "Eddie Lacy", 
          "Martellus Bennett", "Zeke", "Ginn Jr", "Jory", "Rodgers", "Freeman", "Crabtree"]

# authenticates and returns an instance of PRAW, a Reddit API wrapper
def authenticate():
    
    print('Authenticating...\n')
    reddit = praw.Reddit('fantasyBot', user_agent = 'web:fantasyBot:v0.1')
    print('Authenticated as {}\n'.format(reddit.user.me()))
    return reddit

# gets the 50 most recent comment in r/fantasyfootball, checks to see if
# any of the players on myTeam are mentioned, sends message if one is
def run_fantasybot(reddit):
    
    print("Getting recent comments...\n")
    
    for comment in reddit.subreddit('fantasyfootball').comments(limit = 50):
        for player in range(len(myTeam)):
        	#converting comments and players in myTeam to lowercase and comparing the two
            match = re.findall(myTeam[player].lower(), comment.body.lower())
            if match:
                print('Player found in comment with comment ID: ' + comment.id)
                player_url = match[0]
                print('Link: ' + player_url)
            
                file_obj_r = open(path,'r')
                        
                if comment.id not in file_obj_r.read().splitlines():
                    print('Comment is new...sending comment\n')
                    msg = 'Comment: ' + comment.body + "\n" + 'Link: ' + comment.permalink(fast=False)
                    reddit.redditor('etolhurst').message('Found Comment About ' + myTeam[player], msg)

                    file_obj_r.close()
                    file_obj_w = open(path,'a+')
                    file_obj_w.write(comment.id + '\n')
                    file_obj_w.close()
                else:
                    print('Already visited link...no message needed\n')
        print('Wating 1 second')    
        time.sleep(1)


def main():
    reddit = authenticate()
    while True:
        run_fantasybot(reddit)


if __name__ == '__main__':
    main()