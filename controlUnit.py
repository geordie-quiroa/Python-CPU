import sys

def TestMode():
    print("Test mode!")
    ## Add automated test for travis

def HelloPerson(person):    
    return ('Hello ' + person)    


if __name__ == '__main__':
    print(HelloPerson(input("Your name: ")))