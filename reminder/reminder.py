#!/usr/bin/python

import time
import os
from win10toast import ToastNotifier
toaster = ToastNotifier()

# For Windows:
birthdayFile = 'C:\\Vinoth\\Python\\python-scripts\\reminder\\reminder.py'
# For Linux:
#birthdayFile = '/mnt/python-scripts/reminder/reminder.py'
#
def checkTodaysBirthdays():
    fileName = open(birthdayFile, 'r')
    today = time.strftime('%m%d')
    flag = 0
    for line in fileName:
        if today in line:
            flag = 1
            print (line[1])
            line = line.spilt(' ')
            toaster.show_toast("Birthday Reminder Today", "This notification + line[1] + ' ' + line[2] + ' ' ", icon_path = "custom.ico", duration = 5, threaded = True)
    if flag == 0:
        toaster.show_toast("No Birthday Today", "Kindly Ignore this note", icon_path = "custom.ico", duration = 10, threaded = True)
if __name__ == '__main__':
    checkTodaysBirthdays()