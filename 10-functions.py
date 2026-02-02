def sum_of_values(num1=10, num2=20):
    print(num1, num2)
    return num1 + num2

def sum_of_values(*args, **kwargs):
    print(args, kwargs)
    return sum(args), sum(kwargs.values())

# ans = sum_of_values(10, 20, 30, 40, 50, 60, 70, num1=10, num2=20)
# print(ans)

# ans = sum_of_values(10, 20, 30, 40, num1=10)
# print(ans)

# ans = sum_of_values(10, 20)
# print(ans)

# print(*objects, sep=' ', end='\n', file=None, flush=False)
# print(1, 2, sep='\n', flush=True)

# def square(num):
#     return num ** 2
# ans = square(10)
# print(ans)

# sample_list = range(1, 11) ### 1...10
# square = lambda num: num ** 2

# ans = map(square, sample_list)
# print(ans)

# for ele in ans:
#     print(ele)

# sample_list = range(1, 11) ### 1...10
# even = lambda x: x % 2 == 0
# ans = filter(even, sample_list)
# ans = list(filter(even, sample_list))
# ans = list(map(even, sample_list))
# print(ans)

# for ele in ans:
#     print(ele)

### list comprehension
sample_list = range(1, 11) ### 1...10
for ele in sample_list:
    if ele % 2 == 0:
        print(ele)
# ans = [ele for ele in sample_list if ele % 2 == 0]
ans = [ele if ele % 2 == 0 else False for ele in sample_list]
print(ans)