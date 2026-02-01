# sample_dict = {
#     'colors': ['orange', 'red', 'blue'],
#     'numbers': [1234, 456, 789, 10],
#     'tools': ['Ansible', 'Terraform', 'Prometheus', 'Docker', 'Kubernetes'],
#     (1234, 456, 789): 'a',
# }

# print(sorted(sample_dict['colors']))
# sample_dict['numbers'][-1] = 100
# print(sample_dict['numbers'])

# sample_dict = {
#     "employee": {
#         "name": "John",
#         "age": 30,
#         "city": "New York"
#     }
# }

# print(sample_dict["employee"]["name"])

sample_dict = {
    'colors': ['orange', 'red', 'blue'],
    'numbers': [1234, 456, 789, 10],
    'tools': ['Ansible', 'Terraform', 'Prometheus', 'Docker', 'Kubernetes'],
    (1234, 456, 789): 'a',
}

sample_dict['fruits'] = ['apple', 'banana', 'orange']
# print(sample_dict)

print(sample_dict.keys())
print(sample_dict.values())
print(sample_dict.items())