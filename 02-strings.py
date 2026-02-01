# sample_str = "Micorsoft Windows [Version 10.0.22621.2861]"


# print(sample_str.upper())
# print(sample_str.capitalize())
# print(sample_str.count("Microsoft"))

# ans = sample_str.split(" ")
# ans = sample_str.split("\n")
# ans = sample_str.splitlines()
# print(ans)

####### INDEXING ########

# print(sample_str[0])
# print(sample_str[2])
# print(sample_str[-1])
# print(sample_str[-2])

###### SLICING ###########

# print(sample_str[0:4]) ### 0 to 3 not 4
# print(sample_str[:5]) ### 0 to 4 
# print(sample_str[20:]) ### 0 to 4
# print(sample_str[-1:-4]) #### 0 to 3
# ### start, start  + 1, start + 2, ..... end 
# print(sample_str[-4:-1]) ## 0 to 3
# print(sample_str[:])  
# #### start, start + 2, start + 4,... end
# print(sample_str[::2])
# print(sample_str[1::2])

# ##### [start:end:step]
# # start: 0
# # end: end
# # step: -1
# print(sample_str[::-1])

# sample_str = "Micorsoft Windows [Version 10.0.22621.2861]"
# sample_str[0] = "p" # is not allowed
# print(sample_str)

# ## string concantenation
# sample_str = sample_str + " (c) Microsoft Corporation. All rights reserved."
# print(sample_str)

# sample_str = 'abc'
# sample_str = 10
# print(sample_str)

sample_str = "Micorsoft Windows [Version 10.0.22621.2861]"
sample_str = "{1}{0}".format(sample_str, "abc")
print(sample_str)