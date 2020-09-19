import praw
import os

def bot_login():
    try:
        print("logging in: ", os.getenv("Sidikulous"))
        reddit = praw.Reddit(client_id = os.getenv("dpNlSeAlbrNlGA"),
                    client_secret = os.getenv("I9HwugR1YLiltOCwQI0yxtzJWMQ"),
                    user_agent = 'PRAW API tutorial Python Script',
                    username = os.getenv("Sidikulous"),
                    password = os.getenv("siddhesh12"))   
        print("logged in!")
    except:
        print("Login failed")

    return reddit
