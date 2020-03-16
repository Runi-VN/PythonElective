# Use BeautifulSoup to extract all titles on all radio programs https://www.dr.dk/radio/programmer

from tqdm import tqdm
import bs4
import requests


# First find how many pages there are
r = requests.get('https://www.dr.dk/radio/programmer')
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html.parser')

div_items = soup.select('.pagination__item')

page_values = []
for page_item in div_items:
    page_values.append(int(page_item.get('data-page')))
page_count = max(page_values)  # used for last exercise
print('amount of pages:', page_count)


# Then find all titles on https://www.dr.dk/radio/programmer?side=1
titles = []

r = requests.get('https://www.dr.dk/radio/programmer?side=1')
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html.parser')

titleElements = soup.select('.spot-content__title')
# print(titleElements)

for element in titleElements:
    titles.append(element.text)

print(titles)

# Then find all titles on all pages
# should probably have used functions and re-use code lol
all_titles = []
for page_no in tqdm(range(1, (page_count)+1)):
    url = f'https://www.dr.dk/radio/programmer?side={page_no}'
    r = requests.get(url)
    r.raise_for_status

    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    titleElements = soup.select('.spot-content__title')
    for element in titleElements:
        all_titles.append(element.text)

print(all_titles)
