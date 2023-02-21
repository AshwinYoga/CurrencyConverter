import sys
import requests

#write main function


def interactions():
    quoteCurrency = print("Choose Quote Currency: ")

def convertCurrency(baseCurrency, quoteCurrency, conversionRate):
    conversionAmt = print(f"How much {baseCurrency} would you like to convert to {quoteCurrency}")
    total = conversionAmt*conversionRate

    return total


def displayAllCurrencies():
      #reading txt files -> found on stack
      with open('Currencies.txt', 'r', encoding='utf-8') as f:
        for line in f: 
            currency = line.split()[0]  #gets the word at first index of eachline
            print(currency)


def displayCurrency():
    #list top ten most common traded currencies
    topCurrencies = ["USD", "EUR", "GBP", "CAD","AUD", "NZD", "CHF","JPY","CNY", "HKD"]
    print("Select a Currency: ")
    #lists them
    for currency in topCurrencies:
        print(currency)   
    print("Enter 'ALL' to List All Currencies")
    #takes user input
    baseCurrency = input(">")
    if baseCurrency == "ALL":
        displayAllCurrencies()
        baseCurrency = input(">")

    
    return baseCurrency    


# def displayAll():
#     d

   

#API call 
def exchangerate(baseCurrency):
    # baseCurrency = input("Choose base currency: ")
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
    
    exchangerate(displayCurrency())



#this is just something you always do in python for main functions idk why
if __name__ == "__main__":
    main()