from instapy import InstaPy 
from instapy import smart_run
from instapy import set_workplace
import argparse
import schedule 
import time 
import datetime



parser = argparse.ArgumentParser()
parser.add_argument("-username")
parser.add_argument("-password")
parser.add_argument("-clarifai_api",default="N/A")
parser.add_argument("-interval",default="weekly")
parser.add_argument("-time",default="12:00pm")


def instagram_job():
  session.login()
  with smart_run():
    session.like_by_tags(['elsalvador'],amount=100)
    session.dont_like(['naked','nsfw'])
    session.set_do_follow(True,percentage=5)
    session.set_relationship_bounds(enabled=True, max_followers=7500)

    if CLARIFAI_API != "N/A":
        session.set_use_clarifai(enabled=True, api_key=CLARIFAI_API)
        session.clarifai_check_img_for(['nsfw'])

    session.end()


if __name__ == "__main__":
    args = parser.parse_args()
    USERNAME = args.username 
    PASSWROD = args.password
    CLARIFAI_API = args.clarifai_api
    INTERVAL = args.interval
    TIME = args.time

    
    session = Instapy(username=USERNAME,password=PASSWROD)

    try:
        if INTERVAL == "weekly"
            today = datetime.datetime.today().strftime('%A').lower()
            schedule.every().today.at(TIME).do(instagram_job)
        elif INTERVAL == "daily":
            schedule.every().day.at(TIME).do(instagram_job)
    else Exception as e:
        print(e)


    while True:
        schedule.run_pending()
        time.sleep(10)