import urllib.request 
from bs4 import BeautifulSoup
import requests

# dictonary containing all three URL, that are being used to find converted values
thisdict = {
    "xe": "https://www.xe.com/currencyconverter/convert/",
    "xr" : "https://www.x-rates.com/calculator/",
    "fr" : "https://api.frankfurter.app/latest"
}

# function takes both the values from 'call_from_main' function in main.py,
# calculate converted value using different functions and returns final ans
def call_from_main(from_currency, to_currency, amount):
    list_of_result = []
    for each_item in thisdict.values():
        val = show_value(from_currency, to_currency, amount, each_item)
        list_of_result.append(val)
    # for i in list_of_result:
    #     print(i)
    return min(list_of_result), max(list_of_result)

# Check for valid input and make url using string concateation, check condition
# and then call functions accordingly for all three values present in dictonary
def show_value(from_currency, to_currency, amount, url):    
    if(from_currency == 'Select' or to_currency == 'Select'):
        return 'Invalid input'
    if(from_currency != to_currency):
        if url == "https://www.xe.com/currencyconverter/convert/":
            str = "" + url +"?Amount=" + amount+"&From="+from_currency+"&To="+to_currency
            ans = final_val_for_first_link(str)
        elif url == "https://www.x-rates.com/calculator/":
            str = "" + url +"?from="+from_currency+"&to="+to_currency +"&amount=" + amount
            ans = final_val_for_second_link(str)
        elif url == "https://api.frankfurter.app/latest":
            str = "" + url + "?amount=" + amount+"&from="+from_currency+"&to="+to_currency
            ans = final_val_for_third_link(str, to_currency)
        return ans
    else:
        return '1'

# Parse html file using beautifulsoup
def get_beautiful_soup_object(url):
    html = urllib.request.urlopen(url)
    htmlParse = BeautifulSoup(html, 'html.parser')
    return htmlParse

# returns the converted value for the first url in the dictonary 
def final_val_for_first_link(url):
    print(url)
    soup = get_beautiful_soup_object(url)
    val = soup.find("p", class_="result__BigRate-sc-1bsijpp-1 iGrAod").get_text()
    result = val.split()
    return result[0]

# returns the converted value for the second url in the dictonary 
def final_val_for_second_link(url):
    print(url)
    soup = get_beautiful_soup_object(url)
    val = soup.find("span", class_="ccOutputRslt").get_text()
    result = val.split()
    return result[0]

# returns the converted value for the third url in the dictonary 
def final_val_for_third_link(url, to_currency):
    response = requests.get(url)
    result = f"{response.json()['rates'][to_currency]}"
    return result