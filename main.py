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
        response = json.loads(myVoiceIt.getUser(uid, password))
        print(response)

        if response["ResponseCode"] == "SUC":
            wav_path = input("Enter the location of wav file: ")
            response = json.loads(myVoiceIt.authentication(uid, password, wav_path, locale))
            print(response)

            if response["ResponseCode"] == "SUC":
                userAuthenticated = True
                userName = uid

    except (ValueError, KeyError, TypeError):
        print("JSON format error")


def create_user():
    uid = input("Enter the user ID/Name: ")
    password = input("Enter the password: ")

    try:
        response = json.loads(myVoiceIt.getUser(uid, password))

        if response["ResponseCode"] == "UNF":
            response = json.loads(myVoiceIt.createUser(uid, password))

            if response["ResponseCode"] != "SUC":
                print("Error creating new user!")

    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    print("User", uid, ",is created sucesfully!")

    # create enrollment
    print("You will now need to upload some voice samples for voice authentication.")
    print("You will be prompted 3 times for voice enrollment")
    for i in range(3):
        wav_path = str(input("Enter the .wav file for upload: "))
        response = json.loads(myVoiceIt.createEnrollment(uid, password, wav_path, locale))
        print(response)
        if response["ResponseCode"] != "SUC":
            print("Enrollment failed try again")
            i -= 1

    print("New user registration complete!")
    

if __name__ == "__main__":
    print("------------------------------------------------------")
    print("||  Welcome to VoiceIt voice authentication system  ||")
    print("------------------------------------------------------")
    print("1 - Login")
    print("2 - New user registration.")
    choice = int(input("Your choice: "))
    print("------------------------------------------------------")

    if choice == 1:
        user_login()
    elif choice == 2:
        create_user()
