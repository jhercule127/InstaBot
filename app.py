from instapy import InstaPy 
from instapy import smart_run
import argparse
import schedule 
import time 
import datetime


parser = argparse.ArgumentParser()
parser.add_argument("-u",required=True)
parser.add_argument("-p",required=True)
parser.add_argument("-clarifai_api",default="N/A")
parser.add_argument("-interval",default="weekly")
parser.add_argument("-time",default="12:00pm")


def instagram_job():
    '''Automates the work done in Instagram '''
    session.login()
    with smart_run():
        hashtags = session.target_list("./hashtags.txt")
        session.like_by_tags(hashtags,amount=100)
        session.dont_like(['naked','nsfw'])
        session.set_do_follow(True,percentage=5)
        session.set_relationship_bounds(enabled=True, max_followers=7500)

        if CLARIFAI_API != "N/A":
            session.set_use_clarifai(enabled=True, api_key=CLARIFAI_API)
            session.clarifai_check_img_for(['nsfw'])

        session.end()



def validate_time(timestr):
    '''Validates time and converts it into military time'''
    try:
        new_time = datetime.datetime.strptime(timestr,"%I:%M%p")
        return new_time.strftime("%H:%M%p")[:-2]
    except ValueError as e:
        print("Value Error: {}".format(e))


if __name__ == "__main__":
    args = parser.parse_args()
    USERNAME = args.u 
    PASSWORD = args.p
    CLARIFAI_API = args.clarifai_api
    INTERVAL = args.interval
    TIME = args.time

    correct_time = validate_time(TIME)
    
    session = InstaPy(username=USERNAME,password=PASSWORD,bypass_security_challenge_using='sms')
    
    try:
        if INTERVAL == "weekly":
            today = datetime.datetime.today().strftime('%A').lower()
            schedule.every().today.at(correct_time).do(instagram_job)
        elif INTERVAL == "daily" and correct_time:
            print(correct_time)
            schedule.every().day.at(correct_time).do(instagram_job)
    except Exception as e:
        print(e)

    
    while True:
        schedule.run_pending()
        time.sleep(10)
    
    
