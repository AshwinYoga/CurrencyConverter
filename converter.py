import sys
import requests

#write main function


def interactions():
    quoteCurrency = print("Choose Quote Currency: ")



#API call 
def exchangerate():
    baseCurrency = input("Choose base currency: ")
    #API key -> variable based on user input
    url = f"https://v6.exchangerate-api.com/v6/d1fb75f31e693824ef75c19f/latest/{baseCurrency}"
    #{baseCurrency} is base currency
    response = requests.get(url)
    data = response.json()

    #Converts the value of the last key,value pair into a new dictionary
    conversionRates = dict(data["conversion_rates"])

    #prints new conversion rate
    for key, value in conversionRates.items():
        print(key, ":", value)

    
       


def main():
    #stuff goes here
    exchangerate()



#this is just something you always do in python for main functions idk why
if __name__ == "__main__":
    main()