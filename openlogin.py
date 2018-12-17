'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ismail A Ahmed
openlogin.py
Version 1.0
'''

import uuid
import hashlib
import time
from subprocess import call

files =open('idpin.txt')
grades = [x.strip() for x in files.readlines()] #gets encrypted username/password from file and stores as list
terracotta = grades[-1] #gets the last encrypted username/password in list to check when to break for loop below
lastitem = terracotta.split(' ') #splits username and password

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

def check_password2(hashed_password2, user_password2):
    password2, salt2 = hashed_password2.split(':')
    return password2 == hashlib.sha256(salt2.encode() + user_password2.encode()).hexdigest()

userID = input("Please enter your User ID: ")
pinpas = input("Please enter your PIN number: ")
for x in grades:
    ab = x.split(' ')

    if check_password(ab[1], pinpas): #checks password
        if check_password2(ab[0], userID): #checks username
            print('Logged in!')
            myfile = time.ctime(time.time())  # my time
            dafile = (userID+" logged in on "+str(myfile))
            outfile = open("logfiles.txt", "a")
            outfile.write(dafile+'\n')
            outfile.close()
            call(["python", "open.py"])
            break
        elif ab[1] == lastitem[1]: #checks to see if password last in list if password wrong, to see if for loop should check next one(if there is one)
            print('I am sorry but your user ID or pin is incorrect!')
            myfile2 = time.ctime(time.time())  # my time
            dafile2 = (userID + " attempted to log in on " + str(myfile2))
            outfile2 = open("logfiles.txt", "a")
            outfile2.write(dafile2 + '\n')
            outfile2.close()
            break
        else:
            pass

    elif ab[0] == lastitem[0]: #checks to see if username last in list if username wrong, to see if for loop should check next one(if there is one)
        print('I am sorry but your user ID or pin is incorrect!')
        myfile2 = time.ctime(time.time())  # my time
        dafile2 = (userID+" attempted to log in on "+str(myfile2))
        outfile2 = open("logfiles.txt", "a")
        outfile2.write(dafile2+'\n')
        outfile2.close()
        break
    else:
        pass