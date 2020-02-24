import numpy as np

# Class exercise: table
# Find the five slicings on the image
# https://github.com/datsoftlyngby/dat4sem2020spring-python/blob/master/04%20Numpy.ipynb

table = np.arange(10, 30).reshape(4, 5)
yellow = table[0, 0]
lblue = table[:, [1, 3]]
red = table[0, 1:4]
green = table[0:3, 2]
dblue = table[[0, 2], 4]  # specific
# dblue = table[::2,4] #every 2nd on column 4

# print(table)
# print("yellow = 10:", yellow)
# print("lblue = 11,16,21,26 & 13,18,23,28:", lblue)
# print('red = 11,12,13:', red)
# print('green = 12,17,22: ', green)
# print('dblue = 14,24:', dblue)

# 3D
# reshape can be done with multiple dimensions.
# threed = np.arange(0, 27).reshape((3, 3, 3))  # = (z, y, x)
# print('whole cube: \n', threed, '\n---------------')

# print('1st row (x-values): \n', threed[0, 0, :], '\n---------')
# print('1st collumn (y-values, where x==0): \n', threed[0, :, 0], '\n---------')
# print('1st depth (z-values, where y==0 and x==0): \n',
#       threed[:, 0, 0], '\n---------')
# print('value of first side, second slice, third piece:\n',
#       threed[0, 1, 2], '\n-------------')  # equal to a[0][1][2] = 5
# # equivivalent to a[:,2,:] all z, y=2, all x.
# print('values of all x*z where y=2\n', threed[:, 2], '\n----------')
# print('all z and y values where x = 2: \n', threed[:, :, 2], '\n--------')  #
# # all z (skip each second) and all y (skip each second) etc.
# print('skip each second z,y,x: \n', threed[::2, ::2, ::2])

# Class exercise: cube
# Slice out [12 13 14] from the above cube using only one slice. e.g: a[:,:,:]
# slicemid = threed[1, 1, :]
# print('middle layer (12,13,14) printed:', slicemid)
# # Slice out [3 12 21].
# slicedepth = threed[:, 1, 0]
# print('middle layer (depth) (3,12,21) printed:', slicedepth)
# # Slice out all y-values where x is 2 and z is 0.
# slice_y = threed[0, :, 2]
# print('slice all y, where x=2,z=0 (2,5,8) printed:', slice_y)

# Class exercise: masking
# For the dataset:
# data = np.arange(1, 101).reshape(10, 10)
# print(data)
# # apply a mask that will return only the even numbers
# data_even = data[data % 2 == 0]
# print("Only Evens:", data_even)
# # using np.where() return only numbers that ends with 6
# # data_only6 = data[data % 10 == 6]
# # idk how to remove the None.
# # this returns a tuple and I cannot find a resource where you can write something else tha None for y
# data_only6 = np.where(data % 10 == 6, data, None)
# print("Only ending in 6:", data_only6)
# # using the operators: % and | mask to only get numbers that are divisible by 3 and numbers begining with 8
# data_complex_mask = data[((data % 3 == 0) | (data // 10 == 8) | (data == 8))]
# print('get divisible by 3 & all starting 8s:', data_complex_mask)


# Exercise numpy and csv
# 1. load the csv file: befkbhalderstatkode.csv into a numpy ndarray
filename = './befkbhalderstatkode.csv'
ds = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
# AAR,BYDEL,ALDER,STATKODE,PERSONER
#print(type(ds), ' of size: ', ds.size)
#print('first line:\n', ds[0], '\nlast line\n', ds[len(ds)-1])


# 2. How many german children were 0 years old in 2015?
def get_german_newborns_2015():
    # AAR,BYDEL,ALDER,STATKODE,PERSONER
    #germany = 5180
    german_mask = (ds[:, 0] == 2015) & (ds[:, 3] == 5180) & (ds[:, 2] == 0)
    # year = 2015, nationality = germany, age = 0
    german_newborns_in_2015 = ds[german_mask]
    newborn_sum = german_newborns_in_2015[:, 4].sum()
    return newborn_sum


print("amt. of newborn germans in 2015:", get_german_newborns_2015())  # 35

# 3. create a function that can take any combination of the 4 parameters:AAR,BYDEL,ALDER,STATKODE and return population data

# 4. create a new function like previous so that it can sum values for all ages if age is not provided to the function
# 5. further add functionality to sum values if citizenship or area was not provided to function.
# 6. create a new function that can also give average values for each year if year whas not provided.
# 7. create a function, that given year and nationality can return which area had the most of these nationals by that year. Test it by finding out which area had the most Moroccan people in both 1992 and 2015
# 8. Find the Area(s) where fewest foreingers lived in Copenhagen in 1992 and 2015 respectively
# 9. Find out what age most French people have in 2015
