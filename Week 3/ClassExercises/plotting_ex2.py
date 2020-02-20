
import matplotlib.pyplot as plt

# 1.1 Using this dict: {} display a bar plot of the people and there ages sorted by age.
# 1.2 Add title and x and y axis labels to the bar plot


person_dict = {'Holger': 25, 'Helga': 54, 'Hasse': 76,
               'Halvor': 12, 'Hassan': 43, 'Hulda': 31, 'Hansi': 102}
person_dict_sorted = {k: v for k, v in sorted(
    person_dict.items(), key=lambda item: item[1])}  # sort dict https://stackoverflow.com/a/613218


# title, label setup
plt.title("Person/Age bar plot", fontsize=24)
plt.xlabel("Person", fontsize=14)
plt.ylabel("Age", fontsize=14)

# axis value setup
# get max value of a dictionary
max_y_key = max(person_dict, key=person_dict.get)
max_y_val = person_dict[max_y_key]
print('max:', max_y_val)

# axis setup
# axis(x-min, x-max, y-min, y-max)
#plt.axis([0, len(list(person_dict.keys())), 0, max_y_val+10])

# plot setup
plt.bar(list(person_dict_sorted.keys()), list(
    person_dict_sorted.values()), width=0.5, align='center')

plt.show()

# 2.1 Using the kkdata module with population data from Copenhagen display a line graph showing the population development over time (year on x and population on y)
