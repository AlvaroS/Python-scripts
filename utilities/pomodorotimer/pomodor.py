#!/bin/python

import time
from pygame import mixer

def session_timer(total_minutes):
    '''
    Countdown displayed in mm:ss for sessions.
    '''

    total_minutes -= 1
    for minute in range(total_minutes, -1, -1):
        for second in range(59, -1, -1):
            print("{:02d}:{:02d}".format(minute, second), end="\r")
            time.sleep(1)

def session_rest(total_minutes):
    '''
    Countdown displayed in mm:ss for rests.
    '''

    total_minutes -= 1
    for minute in range(total_minutes, -1, -1):
        for second in range(59, -1, -1):
            print("{:02d}:{:02d}".format(minute, second), end="\r")
            time.sleep(1)

def user_input():
    '''
    user input of sessions and rests time and sessions number
    '''

    try:
        SESSION_TIME = int(input("insert session time: "))
        REST_TIME = int(input("insert rest time: "))
        SESSION_NUMBER = int(input("insert sessions number: ")) + 1
        return SESSION_TIME, REST_TIME, SESSION_NUMBER
    except ValueError:
        print('please insert only integrers')
        quit()


if __name__ == "__main__":
    mixer.init()
    stop = mixer.Sound('ding.wav')
    start = mixer.Sound('dong.wav')
    session = 1

    SESSION_TIME, REST_TIME, SESSION_NUMBER = user_input()

    while SESSION_NUMBER != session:
        print(f"session {session}")
        session_timer(SESSION_TIME)
        stop.play()
        print("Rest time!")
        session_rest(REST_TIME)
        start.play()
        session = session + 1

    start.play()
    print('session ended')
