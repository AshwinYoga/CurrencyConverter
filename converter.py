import sys
import requests
from datetime import datetime
import json
import queue


# write main function


# func to get time and add to dictionary and write to txt file
# if dictionary is longer than will remove the last entry
# FILO
def writeHistory(baseCurrency, quoteCurrency, inputAmount, outputAmount, data):

    # if file is empty, basically never matters
    if data is None:
        data = []
    # create list from the data passed through
    # data is already list
    # need to do this to recognize the list functions -> append, pop, etc..
    entryList = list(data)

    currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    entry = {
        "timeStamp": currentTime,
        "baseCurrency": baseCurrency,
        "quoteCurrency": quoteCurrency,
        "inputAmount": inputAmount,
        "outputAmount": outputAmount
    }

    # only have the last ten entries FIFO
    print(len(entryList))
    if len(entryList) == 10:
        entryList.pop(0)

    entryList.append(entry)
    writeToJson(entryList)


def readJson():
    history = []
    with open('history.json', 'r') as f:
        # prevents errors if the file is empty -> found on stack
        if len(f.readlines()) != 0:
            f.seek(0)
            history = json.load(f)
    return history


def writeToJson(historyList):
    with open("history.json", "w") as f:
        # indent= 3 allows for better formatting on json file, now neccessary, but more readable
        json.dump(historyList, f, indent=3)
    f.close()

# Actual conversion is done


def convertCurrency(baseCurrency, quoteCurrency, conversionRate):
    print(f"1 {baseCurrency} : {conversionRate} {quoteCurrency}")
    conversionAmt = input(
        f"---\nHow much {baseCurrency} would you like to convert to {quoteCurrency}: ")
    total = float(conversionAmt)*conversionRate
    print(
        f"---\n{conversionAmt} {baseCurrency} -> {round(total,2)} {quoteCurrency}")

    writeHistory(baseCurrency, quoteCurrency, float(
        conversionAmt), total, readJson())


# one input function asks user for base or quote
def chooseCurrency(base_or_quote):
    displayCurrencies(base_or_quote)
    currency = input("---\n> ")
    print("---")
    if currency == "ALL":
        displayAllCurrencies()
        currency = input("---\n> ")
        print("---")
    return currency


def displayCurrencies(base_or_quote):
    # entryList top ten most common traded currencies
    topCurrencies = ["USD", "EUR", "GBP", "CAD",
                     "AUD", "NZD", "CHF", "JPY", "CNY", "HKD"]
    print(f"Select {base_or_quote} Currency:\n---")
    # lists them
    for currency in topCurrencies:
        print(currency)
    print("---\nEnter 'ALL' to List All Currencies")


def displayAllCurrencies():
    # reading txt files -> found on stack
    with open('Currencies.txt', 'r', encoding='utf-8') as f:
        for line in f:
            # gets the word at first index of eachline
            currency = line.split()[0]
            print(currency)


# calling API here to get conversion rate
def getConversionRate(baseCurrency, quoteCurrency):

    # API key -> variable based on user input
    url = f"https://v6.exchangerate-api.com/v6/d1fb75f31e693824ef75c19f/latest/{baseCurrency}"
    # {baseCurrency} is base currency
    response = requests.get(url)
    data = response.json()
    # Converts the value of the last key,value pair into a new dictionary
    conversionRates = dict(data["conversion_rates"])

    return conversionRates[quoteCurrency]


# returns it in reverse
def swapCurrencies(baseCurrency, quoteCurrency):
    return quoteCurrency, baseCurrency


def runConversion():
    baseCurrency = chooseCurrency("Base")
    quoteCurrency = chooseCurrency("Quote")
    conversionRate = getConversionRate(baseCurrency, quoteCurrency)
    convertCurrency(baseCurrency, quoteCurrency, conversionRate)

    return baseCurrency, quoteCurrency, conversionRate


# menu
def menu(input, baseCurrency, quoteCurrency, conversionRate):

    if input == 'A':
        convertCurrency(baseCurrency, quoteCurrency, conversionRate)
    elif input == 'B':
        baseCurrency = chooseCurrency("Base")
        conversionRate = getConversionRate(baseCurrency, quoteCurrency)
        convertCurrency(baseCurrency, quoteCurrency, conversionRate)
    elif input == 'C':
        quoteCurrency = chooseCurrency("Quote")
        conversionRate = getConversionRate(baseCurrency, quoteCurrency)
        convertCurrency(baseCurrency, quoteCurrency, conversionRate)
    elif input == 'D':
        baseCurrency, quoteCurrency = swapCurrencies(
            baseCurrency, quoteCurrency)
        conversionRate = getConversionRate(baseCurrency, quoteCurrency)
        convertCurrency(baseCurrency, quoteCurrency, conversionRate)
    elif input == 'E':
        baseCurrency, quoteCurrency, conversionRate = runConversion()
    elif input == 'F':
        history = readJson()

        for entry in history:
            print("---")
            for key, value in entry.items():
                print(f"{key} : {value}")
    else:
        print("---\nInvalid Option")

    return baseCurrency, quoteCurrency, conversionRate


def main():
    # stuff goes here
    baseCurrency, quoteCurrency, conversionRate = runConversion()

    # allowing the program to run
    while True:

        menuSelect = input(
            "---\nPlease Select A Menu Option\n---\nA -> Enter A New Amount\nB -> Choose New Base Currency\nC -> Choose New Quote Currency\nD -> Swap Base and Quote Currency\nE -> New Conversion\nF -> Conversion History\nQUIT -> Exit Program\n---\n> ")
        print("---")
        if menuSelect == "QUIT":
            break
        baseCurrency, quoteCurrency, conversionRate = menu(
            menuSelect, baseCurrency, quoteCurrency, conversionRate)


# this is just something you always do in python for main functions idk why
if __name__ == "__main__":
    main()
