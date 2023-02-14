import sys
import requests

#write main function

#API call 
def exchangerate():
    #API key
    url = " https://v6.exchangerate-api.com/v6/d1fb75f31e693824ef75c19f/latest/USD"
    #USD is base currency

    response = requests.get(url)
    data = response.json()
    print(data)

def main():
    exchangerate()
    print("hello")
    print("AShwin")
    print("devo")

    print("whats up")
    
#this is just something you always do in python for main functions idk why
if __name__ == "__main__":
    main()