
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

import google_cal_api as gcal

def demo(UserCal):
    """
    This is a demo function to check functionality of a valid UserCal
    """
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    
    print('Getting the upcoming 10 events')
    eventsResult = UserCal.service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


def main():
    """
    This is the main routine for DeCalcify
    """

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    curCal = gcal.UserCal()
    demo(curCal)

if __name__ == '__main__':
    print("Running DeCalcify.py")
    main()
