sample_list = [10, 2, 20, 30, 5, 80, 90]
# elements_to_search = 35

# even_nums = []
# sum_even = 0

# odd_nums = []
# sum_odd = 0

# for ele in sample_list:
#     if ele %2 == 0:
#         even_nums.append(ele)
#         sum_even += ele
#     else:
#         odd_nums.append(ele)
#         sum_odd += ele

# print(sum_even, sum_odd)

# sample_str = "This is a sample string"
# sample_str_list = list(sample_list)
# print(sample_str_list)

# for c in sample_str:
#     print(c)

# sample_str_list = ['T', 'h', 'i', 's', 'i', 's', 'a', 's', 'a']
# sample_str = ""

# for c in sample_str_list:
#     sample_str += c
# sample_str = "".join(sample_str_list)
# print(sample_str)


# sample_tuple = ('a', 'b', 'c', 'd')
# for ele in sample_tuple:
#     print(ele)

# sample_tuple_list = [('a', 1), ('b', 2), ('c', 3)]
# for val1, val2 in sample_tuple_list:
#     print(val1, val2)

# d = {'k': 1, 'k2': 2, 'k3': 3}
# for k, v in d.items():
#     print(k, v)

# sample_list = [10, 20, 30, 5, 80, 90]
# element_to_search = 10  ## 35

# idx = 0

# #####  break and continue
# for ele in sample_list:
#     if ele == element_to_search:
#         print("Element found at position", idx)
#         break
#         # continue
#     idx += 1

# ## enumerate 
# sample_list = [10, 20, 30, 5, 80, 90]
# for idx, ele in enumerate(sample_list):
#     print(idx, ele)

# #### range
# sample_list = [10, 20, 30, 5, 80, 90]
# for idx in range(len(sample_list)):
#     print(idx, sample_list[idx])

# sample_list = [10, 20, 30, 5, 80, 90]
# idx = 0
# while (idx < len(sample_list)):
#     print(sample_list[idx])
#     idx += 1

# zip()
# list1 = [10, 2, 20, 30, 5, 80, 90]
# list2 = ['a', 'b', 'c', 'd', 'e']

# for ele1, ele2 in zip(list1, list2):
#     print(ele1, ele2)

sample_list = [10, 20, 30, 5, 80, 90]
element_to_search = 80

if element_to_search not in sample_list:
    print("Element not found")
else:
    print("Element found")
    