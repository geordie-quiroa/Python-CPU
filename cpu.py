import sys

if sys.argv[1] == "test":
    TestMode()

def TestMode():
    print("Test mode!")
    ## Add automated test for travis

def Hello():    
    person = input('Enter your name: ')
    print('Hello', person)