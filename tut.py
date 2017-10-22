import tensorflow as tf
import matplotlib.pyplot as plt

data_sets = [100,80, 78, 65, 60, 55, 55, 54]

# list manipulation
# data_sets.append(133)
# data_sets.pop(2)
# data_sets.sort()
# data_sets.reverse()

# fig = plt.figure()
# plt.plot(data_sets2)
# plt.show()

# list comprehension
# data_sets2 = []

# # uneffectiv
# for i in range(11):
#     data_sets2.append(i)

# data_sets3 =[i for i in range(11)]

# print(data_sets3)

# dict

data_dict = {0: 'jan', 1: 'mio'}

# for key,val in data_dict.items():
#     print(key,val)

data_list = [1,2]
# for indx, val in enumerate(data_list):
#     print(indx, val)

# for i, val in zip(range(2,3),data_list):
#     print(i, val)

for (k, v), i, val in zip(enumerate(data_dict),range(2,5),data_list):
    print(k, v, i, val)