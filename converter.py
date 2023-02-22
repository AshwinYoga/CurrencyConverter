import sys
import requests

# write main function


def convertCurrency(baseCurrency, quoteCurrency, conversionRate):
    print(f"1 {baseCurrency} : {conversionRate} {quoteCurrency}")
    conversionAmt = input(
        f"How much {baseCurrency} would you like to convert to {quoteCurrency}: ")
    total = float(conversionAmt)*conversionRate
    print(f"{round(total,2)} {quoteCurrency}")

#one input function asks user for base or quote
def chooseCurrency(base_or_quote):
    displayCurrencies(base_or_quote)
    currency = input(">")
    if currency == "ALL":
        displayAllCurrencies()
        currency = input(">")
    return currency


def displayCurrencies(base_or_quote):
    # list top ten most common traded currencies
    topCurrencies = ["USD", "EUR", "GBP", "CAD",
                     "AUD", "NZD", "CHF", "JPY", "CNY", "HKD"]
    print(f"Select {base_or_quote} Currency: ")
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



#returns it in reverse
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
        baseCurrency, quoteCurrency = swapCurrencies(baseCurrency,quoteCurrency)
        conversionRate = getConversionRate(baseCurrency, quoteCurrency)
        convertCurrency(baseCurrency, quoteCurrency, conversionRate)
    elif input == 'E':
       baseCurrency, quoteCurrency, conversionRate = runConversion()
    else:
        print("Invalid Option")

    return baseCurrency, quoteCurrency, conversionRate


def main():
    # stuff goes here
    baseCurrency,quoteCurrency, conversionRate = runConversion()

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
