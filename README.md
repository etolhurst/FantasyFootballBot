#### FantasyFootballBot

a Reddit bot uses Reddit API to send a message to my personal Reddit account every time a player from
my fantasy football team is mentioned in the fantasy football subreddit.

## How To Run
Download and extract this respository 

In the same directory, creat a file called "praw.ini" as follows:
        [Fantasybot]
        username: <username>
        password: <reddit password>
        client_id: <client id provided by reddit>
        client_secret: <client secret provided by reddit>
To obtain a client id and client secret from Reddit, follow the instructions under "create application": https://www.reddit.com/prefs/apps/
Change the value of "path" in fantasyBot.py to the location of your blank commented.txt file

Change the values in myTeam to the players on your team.

Run the command "python3 fantasybot.py" in Terminal

## Notes
To run this program, you need Python 4, PRAW (pip3 install praw), and Python Requests (pip3 install requests)

I use the time.sleep() function because the Reddit API only allows 60 requests per minute.
