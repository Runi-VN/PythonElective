# Black Tears

import matplotlib.pyplot as plt
from time import sleep
from selenium import webdriver
import bs4
import requests

_URL = 'https://www.merchbar.com/search?q=breaking%20benjamin'


def exercise1():
    """
    Hvor mange produkter kommer frem, 
    når man søger på "breaking benjamin"
    """
    r = requests.get(_URL)
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    span = soup.find(
        'div', {'class': 'd-none d-md-block col-md-3'}).find('span')
    return int(''.join(filter(str.isdigit, span.text)))
    # https://stackoverflow.com/questions/26825729/extract-number-from-string-in-python

#print('Total amount of products on the page:', exercise1())


def exercise2():
    """
    Hvor mange TRACKs er der i det første produkt, 
    som ligger i kategorien CDs?
    """
    browser = webdriver.Chrome()
    browser.get(_URL)
    browser.implicitly_wait(1)
    checkbox_items = browser.find_elements_by_class_name(
        'ais-RefinementList-labelText')  # weird website code

    checkbox_items[2].click()  # click to sort show CDs
    sleep(2)
    browser.find_elements_by_class_name('product-tile')[0].click()
    return len(browser.find_elements_by_class_name('track'))


#print('total amount of tracks on first CD:', exercise2())


def exercise3():
    """
    Vis et bar chart der viser: 
    - Procentdel af de viste produkter, der rent faktisk 
      indeholder Breaking Benjamin merch
    - Procentdel af den merch, der er på tilbud
    - Procentdel af den merch, der ikke er på lager
    """
    merch_count = {'Breaking Benjamin': 0, 'Other': 0}
    merch_offers = {'On sale': 0, 'Other': 0}
    merch_stock = {'In stock': 0, 'Other': 0}

    def get_data():
        r = requests.get(_URL)
        r.raise_for_status()
        soup = bs4.BeautifulSoup(r.text, 'html.parser')

        products = soup.select('div > .product-tile')
        for product in products:
            print(product, '\n')
            if (product.find('div', attrs={'MerchTile.module__brandName'}).text == 'Breaking Benjamin'):
                merch_count['Breaking Benjamin'] += 1
            else:
                merch_count['Other'] += 1
            if (product.find('span', attrs={'MerchTile.module__salePrice'}) != None):
                merch_offers['On sale'] += 1
            else:
                merch_offers['Other'] += 1
            if (product.find('div', attrs={'MerchTile.module__status'}).text == 'In Stock'):
                merch_stock['In stock'] += 1
            else:
                merch_stock['Other'] += 1
    get_data()
    print(merch_count)
    print(merch_offers)
    print(merch_stock)
    print(list(merch_count.values()))
    count_percentage = list(merch_count.values())[
        1]/list(merch_count.values())[0]*100
    offers_percentage = list(merch_offers.values())[
        1]/list(merch_offers.values())[0]*100
    stock_percentage = list(merch_stock.values())[
        1]/list(merch_stock.values())[0]*100
    # offers_percentage =
    # stock_percentage =
    print(count_percentage)
    print(offers_percentage)
    print(stock_percentage)
    # plt.figure()
    # plt.bar()


exercise3()
