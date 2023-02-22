import sys
import requests

# write main function


def convertCurrency(baseCurrency, quoteCurrency, conversionRate):

    print(f"1 {baseCurrency} : {conversionRate} {quoteCurrency}")

    conversionAmt = input(
        f"How much {baseCurrency} would you like to convert to {quoteCurrency}: ")
    total = float(conversionAmt)*conversionRate
    print(f"{round(total,2)} {quoteCurrency}")


def userInput(pair):

    displayCurrencies(pair)
    currency = input(">")
    if currency == "ALL":
        displayAllCurrencies()
        currency = input(">")

    return currency


def displayCurrencies(pair):
    # list top ten most common traded currencies
    topCurrencies = ["USD", "EUR", "GBP", "CAD",
                     "AUD", "NZD", "CHF", "JPY", "CNY", "HKD"]
    print(f"Select {pair} Currency: ")
    # lists them
    for currency in topCurrencies:
        print(currency)
    print("Enter 'ALL' to List All Currencies")


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


def chooseBase():
    return userInput("Base")


def chooseQuote():
    return userInput("Quote")


# menu
def menu(input, baseCurrency, quoteCurrency, conversionRate):

    if input == 'A':
        convertCurrency(baseCurrency, quoteCurrency, conversionRate)
    elif input == 'B':
        baseCurrency = chooseBase()
        conversionRate = getConversionRate(baseCurrency, quoteCurrency)
        return menu('A', baseCurrency, quoteCurrency, conversionRate)
    elif input == 'C':
        quoteCurrency = chooseQuote()
        conversionRate = getConversionRate(baseCurrency, quoteCurrency)
        return menu('A', baseCurrency, quoteCurrency, conversionRate)
    else:
        print("Invalid Option")

    return baseCurrency, quoteCurrency, conversionRate


def main():
    # stuff goes here
    baseCurrency = chooseBase()
    quoteCurrency = chooseQuote()
    conversionRate = getConversionRate(baseCurrency, quoteCurrency)
    convertCurrency(baseCurrency, quoteCurrency, conversionRate)

    # allowing the program to run
    while True:

        menuSelect = input(
            "Please Select A Menu Option\nA -> Enter A New Amount\nB -> Choose New Base Currency\nC -> Choose New Quote Currency\nD -> Swap Base and Quote Currency\nE -> New Conversion\nQUIT -> Exit Program\n> ")
        if menuSelect == "QUIT":
            break
        baseCurrency, quoteCurrency, conversionRate = menu(
            menuSelect, baseCurrency, quoteCurrency, conversionRate)


# this is just something you always do in python for main functions idk why
if __name__ == "__main__":
    main()
