from VoiceIt import *

import json

# global variables
developerId = "7e9729573a09490194f97e2e9be820be"
myVoiceIt = VoiceIt(developerId)
userAuthenticated = False
userName = ""
locale = "en-US"
response = {}


def user_login():
    uid = input("Enter the user ID/Name: ")
    password = input("Enter the password: ")

    try:
        response = json.loads(myVoiceIt.getUser(developerId, uid))

        if response["Result"] == "Success":
            wav_path = input("Enter the location of wav file: ")
            response = json.loads(myVoiceIt.authentication(uid, password, wav_path, locale))

            if response["Result"] == "Success":
                userAuthenticated = True
                userName = uid

    except (ValueError, KeyError, TypeError):
        print("JSON format error")


def create_user():
    uid = input("Enter the user ID/Name: ")
    password = input("Enter the password: ")

    try:
        response = json.loads(myVoiceIt.getUser(uid, password))

        if response["Result"] == "User not found":
            '''
            TO-DO
            '''

    except (ValueError, KeyError, TypeError):
        print("JSON format error")


if __name__ == "__main__":
    print("------------------------------------------------------")
    print("||  Welcome to VoiceIt voice authentication system  ||")
    print("------------------------------------------------------")
    print("1 - Login")
    print("2 - New user registration.")
    choice = input("Your choice: ")
    print("------------------------------------------------------")

    if choice == 1:
        user_login()
    elif choice == 2:
        create_user()
