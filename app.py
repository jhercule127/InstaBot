from instapy import InstaPy 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-username")
parser.add_argument("-password")
parser.add_argument("-clarifai_api",default="N/A")


if __name__ == "__main__":
    args = parser.parse_args()
    USERNAME = args.username 
    PASSWROD = args.password
    CLARIFAI_API = args.clarifai_api

    session = Instapy(username=USERNAME,password=PASSWROD)
    session.login()
    session.like_by_tags(['elsalvador'],amount=100)
    session.dont_like(['naked','nsfw'])
    session.set_do_follow(True,percentage=5)
    session.set_relationship_bounds(enabled=True, max_followers=7500)


    if CLARIFAI_API != "N/A":
        session.set_use_clarifai(enabled=True, api_key='<your_api_key>')
        session.clarifai_check_img_for(['nsfw'])

    session.end()
