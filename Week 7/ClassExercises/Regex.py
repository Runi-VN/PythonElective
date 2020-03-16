import re

myStr = "Peter Hansen was meeting up with Jacob Fransen for a quick lunch, but first he had to go by Peter Beier to pick up some chokolate for his wife. Meanwhile Pastor Peter Jensen was going to church to give his sermon for the same 3 people in his parish. Those were Peter Kold and Henrik Halberg plus a third person who had recently moved here from Norway called Peter Harold"

regex_pattern = re.compile(r'Peter \w+')
result = regex_pattern.findall(myStr)
print(type(result))
print(result, '\n')

with open('./addresses.txt', encoding='utf-8') as f:
    addresses = f.read()

# print(addresses)


# all names in the list
regex1 = re.compile(r'\s\s(.+)')
result1 = regex1.findall(addresses)
print(result1, '\n')

# all telephone numbers
regex2 = re.compile(r'\d{2} \d{2} \d{2} \d{2}')
#regex2 = re.compile(r'(\d{2} ){3}\d{2}')
result2 = regex2.findall(addresses)
print(result2, '\n')

# all zip codes
regex3 = re.compile(r'\d{4}')
result3 = regex3.findall(addresses)
print(result3, '\n')

# all city names with corresponding zip code
regex4 = re.compile(r'\d{4} \w+')
result4 = regex4.findall(addresses)
print(result4, '\n')

# all street names
# regex5 = re.compile(r'(\n)+')
# result5 = regex5.findall(addresses)
# print(result5, '\n')
