# sample_list = [1, 2, 3]
# sample_list = [1, 'a', '3', True, 'one', 'two', 'three', 4, 5]

# print(len(sample_list))
# print(sample_list[::2]) ### [1, '3', 'one', 'three', 5]

# sample_list = sample_list + [6, 7, 8]

# sample_list *= 2
# print(sample_list)

# ### append(), extend()
# sample_list = [1, 2, 3]
# sample_list.append(4)
# sample_list.append([6, 7, 8])
# sample_list.extend([6, 7, 8])
# print(sample_list)

# sample_list = [1, 2, 3, 4, [6, 7, 8], 6, 7, 8]
# ele = sample_list.pop(0)
# print(ele)
# sample_list.reverse()

# sample_list = ['c', 'b', 'a', 'e', 'd']
# sample_list.sort()
# sample_list_sorted = sorted(sample_list)
# print(sample_list)
# print(sample_list_sorted)

# #### Nesting Lists 
# sample_list = [1, 2, 3, 4, [60, 70, 80], 6, 7, 8]
# print(sample_list[4][0])

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
# sample_list = [list1, list2]
# print(sample_list)

# sample_list = [[1, 2, 3], [10, 20, 30]]

# a, b, c = [1, 2, 3] ## Unpacking
# print(a, b, c)

### Swapping values
# a = 1
# b = 2
# a, b = b, a
# print(a, b)

a = 2
b = 1

sample_list = [1, 2, 3, 4, [60, 70, 80], 6, 7, 8]
sample_list[-2] = 700
sample_list = sample_list[::-1]
print(sample_list)