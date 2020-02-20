
import matplotlib.pyplot as plt

# Exercise 1
# based on kkdata
# show the distribution of citizenships
# in all copenhagen areas and all ages in 2015

stats = {5100: 492614, 5104: 899, 5106: 1968, 5110: 4093, 5120: 4745, 5126: 273, 5130: 2156, 5140: 977, 5150: 3069, 5154: 3906, 5164: 1999, 5170: 4523, 5180: 4021, 5228: 404, 5306: 560, 5390: 2534, 5448: 2552, 5464: 1692, 5472: 4502, 5502: 609, 5704: 447, 5752: 102, 5142: 565, 5156: 849, 5432: 2168, 5462: 7, 5700: 787, 5750: 285, 5756: 1518, 5115: 15, 5288: 38, 5314: 605, 5318: 146, 5611: 1348, 5234: 151, 5478: 9, 5128: 1413, 5289: 2087, 5438: 1093, 5160: 387, 5434: 137, 5474: 1396, 5607: 323, 5778: 321, 5272: 321, 5514: 143, 5716: 36, 5436: 2544, 5492: 1544, 5458: 122, 5134: 744, 5374: 21, 5354: 253, 5103: 632, 5158: 1891, 5456: 343, 5486: 200, 5609: 585, 5174: 796, 5269: 196, 5364: 3, 5759: 121, 5302: 161, 5182: 377, 5244: 1499, 5442: 192, 5482: 128, 5776: 217, 5129: 23, 5444: 383, 5488: 278, 5316: 223, 5754: 688, 5757: 195, 5484: 149, 5172: 3792, 5259: 3, 5706: 58, 5724: 34, 5153: 22, 5246: 364, 5392: 84, 5410: 787, 5424: 60, 5708: 59, 5712: 25, 5152: 1487,
         5268: 199, 5326: 16, 5328: 54, 5338: 29, 5358: 15, 5202: 132, 5262: 93, 5446: 460, 5720: 7, 5122: 68, 5151: 19, 5422: 24, 5282: 99, 5348: 12, 5294: 8, 5496: 2, 5714: 42, 5278: 25, 5366: 137, 5416: 27, 5240: 24, 5279: 25, 5356: 27, 5304: 29, 5162: 51, 5258: 129, 5277: 122, 5283: 2, 5418: 86, 5454: 6, 5245: 15, 5296: 31, 5324: 152, 5352: 20, 5404: 658, 5408: 8, 5459: 8, 5414: 47, 5108: 11, 5266: 125, 5718: 2, 5214: 273, 5222: 175, 5303: 3, 5105: 2, 5293: 32, 5232: 40, 5347: 2, 5376: 17, 5758: 57, 5522: 2, 5322: 23, 5297: 5, 5235: 5, 5233: 3, 5204: 7, 5207: 4, 5159: 1, 5287: 29, 5216: 50, 5342: 4, 5213: 48, 5238: 12, 5710: 28, 5305: 3, 5284: 2, 5761: 121, 5372: 4, 5236: 11, 5525: 12, 5255: 68, 5215: 3, 5281: 5, 5466: 13, 5298: 2, 5102: 9, 5452: 4, 5231: 16, 5295: 14, 5487: 3, 5285: 2, 5499: 1, 5402: 11, 5505: 2, 5292: 3, 5243: 9, 5308: 3, 5403: 1, 5722: 2, 5001: 4, 5107: 1, 5526: 2, 5345: 2, 5339: 4, 5299: 2, 5247: 5, 5412: 2, 5999: 1, 5242: 1, 5508: 2, 5457: 1}
# Copied from cit.get_citizen_dist(2015)
# get key to the max value of a dictionary
max_y_key = max(stats, key=stats.get)
max_y_val = stats[max_y_key]
print('max_y_key', max_y_key)
print('max:', max_y_val)
plt.cla()
# title, label setup
plt.title("Copenhagen Citizenship/Count", fontsize=14)
plt.xlabel("Citizenship no.", fontsize=10)
plt.ylabel("Amount of people", fontsize=10)

# bar(x-vals, y-vals, bar width)
plt.bar(list(stats.keys()), list(stats.values()), width=5)
plt.show()

# Exercise 2
# remove the danes (code 5100) and
# show only the top 10 nationalities.
stats2 = dict(stats)
print('dict contains 5100:', bool(5100 in stats2))
stats2.pop(5100)  # remove code 5100
print('dict contains 5100:', bool(5100 in stats2))
stats2_sorted_top10 = {k: v for k, v in sorted(
    stats2.items(), key=lambda item: item[1], reverse=True)[:10]}  # sort by index 1 (amt. of citizens), get top 10
print(stats2_sorted_top10)
plt.cla()
plt.title("Copenhagen Citizenship/Count", fontsize=14)
plt.xlabel("Citizenship no.", fontsize=10)
plt.ylabel("Amount of people", fontsize=10)

# bar(x-vals, y-vals, bar width)
plt.bar(list(stats2_sorted_top10.keys()), list(
    stats2_sorted_top10.values()), width=5)
plt.show()
