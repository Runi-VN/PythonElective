
import bs4
import requests
import matplotlib.pyplot as plt
from time import sleep
from selenium import webdriver
from tqdm import tqdm
import json
# https://docs.google.com/spreadsheets/d/10HYM2KRqslBTQjkcz8B0ooz4TnnXd4n5xxFsSl9saZQ/edit#gid=0
# Charming Reaction
# See .ipynb for presentation
_URL = 'https://www.dba.dk/biler/biler/'


def getData(url):
    r = requests.get(url, headers={"User-Agent": "Application"})
    r.raise_for_status()
    return bs4.BeautifulSoup(r.text, 'html.parser')


def exercise1():
    """
    1. Hvor mange brugte biler er der at vælge i mellem
    """
    # What defines a used car? A car with >1 km, of course
    soup = getData(_URL + '?km=(1-)')
    amount_of_cars_text = soup.select(
        'tr[class=search-result-separator] > td')[0].text
    # import re
    # string1 = "498results should get"
    # int(re.search(r'\d+', string1).group()) https://stackoverflow.com/a/11339230
    return int(''.join(x for x in amount_of_cars_text if x.isdigit()))


# print('Amount of used cars available:', exercise1())


def exercise2():
    """
    2. Udskriv alle biler af mærket Ford
    """
    soup = getData(_URL + 'maerke-ford/')
    page_count = int(soup.findAll(
        'a', {'data-ga-lbl': 'paging-number'})[-1].text)
    print('Amount of pages w/ fords:', page_count)

    for page in tqdm(range(1, page_count+1)):
        soup = getData(_URL + 'maerke-ford/side-' + str(page))
        car_data = soup.findAll('tr', {'class': 'dbaListing listing'})
        print('###############')
        print('NEW PAGE: ', page)
        print('###############')
        for car in car_data:
            single_car = car.find('script', {'type': 'application/ld+json'})
            car_json = json.loads(single_car.text)
            print(json.dumps({'name': car_json['name'],
                              'url': car_json['url'],
                              'price': car_json['offers']['price']}, indent=2), '\n')


# exercise2()


def exercise3():
    """
    3.
    Åben de 5 dyreste biler med selenium i decending order
    og vis dem i et barchart
    """

    browser = webdriver.Chrome()
    browser.get(_URL)
    browser.implicitly_wait(3)  # load

    # get rid of GDRP button blocking the whole damn screen
    gdrp_button = browser.find_element_by_id('gdpr-notice__accept')
    gdrp_button.click()
    browser.implicitly_wait(2)

    # actually work - find price element
    def sort_by_price():  # tried to do it by range, but could not work
        thead = browser.find_element_by_class_name('sorting')
        price_element = thead.find_elements_by_class_name('human-ref')[-1]
        price_element.click()
        browser.implicitly_wait(2)
    # click twice to sort desc
    sort_by_price()
    sort_by_price()
    # (could have just webscraped the URL or started from there)

    # get current html
    soup = bs4.BeautifulSoup(browser.page_source, 'html.parser')
    car_data = soup.findAll('tr', {'class': 'dbaListing listing'})
    cars = []
    for car in car_data[:5]:  # get 5 cars
        single_car = car.find('script', {'type': 'application/ld+json'})
        car_json = json.loads(single_car.text)
        cars.append({'name': car_json['name'],
                     'price': car_json['offers']['price']})
    browser.close()
    # plt.figure()
    # plt.bar
    return cars


# print(exercise3())


def exercise3_bargraph(data):
    """
    Creates the barchart required for ex3
    """

    # setup figure
    plt.figure()  # figsize=[8, 5]
    plt.ticklabel_format(style='plain')  # no scientific notation (10^e7)
    plt.title('Top 5 most expensive cars on DBA')
    plt.xlabel('Cars')
    plt.ylabel('Prices')
    plt.grid(axis='y', linestyle='--', zorder=0)
    plt.xticks(rotation=45, ha='right')
    # plt.rcParams['xtick.labelsize'] = 'small'
    # car_names = []
    # car_prices = []
    for car in data:
        print(car)
        # name = car['url'][19:46]  # could have used name too
        name = car['name'][:20]
        price = int(car['price'])
        # car_names.append(car['name'][:18])
        # car_prices.append(int(car['price']))  # IMPORTANT: Convert to int
        plt.bar(name, price, zorder=3, width=0.3)
    # myDict = dict(zip(car_names, car_prices))
    # print('dict', myDict)
    # plt.bar(myDict.keys(), myDict.values(),
    #        zorder=3, width=0.5, align='center')
    plt.tight_layout()  # re-size to fit labels
    plt.show()


# exercise3_bargraph([{'name': 'Porsche 918 Spyder 4,6 Benzin aut. Automatgear...', 'url': 'https://www.dba.dk/porsche-918-spyder-46-benzin/id-504944706/', 'price': '10125000'}, {'name': 'Ferrari 458 4,5 Italia DCT Benzin aut....', 'url': 'https://www.dba.dk/ferrari-458-45-italia-dct/id-505162615/', 'price': '2379900'}, {'name': 'Ferrari F512 M 4,9 Benzin model&amp;#229;r 1995 km 33000...',
#                                                                                                                                                                                                                                                                                                                                 'url': 'https://www.dba.dk/ferrari-f512-m-49-benzin/id-503913036/', 'price': '1953600'}, {'name': 'Ferrari 458 4,5 Speciale DCT Benzin aut....', 'url': 'https://www.dba.dk/ferrari-458-45-speciale-dct/id-505209289/', 'price': '1949900'}, {'name': 'Mercedes SL65 6,0 AMG Black Series aut. Benzin...', 'url': 'https://www.dba.dk/mercedes-sl65-60-amg-black/id-504442331/', 'price': '1878600'}])
