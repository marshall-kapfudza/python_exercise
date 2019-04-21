###############
## Problem 1 ##
###############

s = "django"

# Using index to print out the following
# 'd'
# print(s[0])

# 'o'
# print(s[-1])

# 'djan'
# print(s[:4])

# 'jan'
# print(s[1:4])

# 'go'
# print(s[4:])

# use of indexing to reverse the string
# print(s[::-1])

###############
## Problem 2 ##
###############

# Given nested list
l = [3,7,[1,4,'hello']]
# reasigning "hello" to be "goodbye"
l[2][2] = 'goodbye'

# print(l)

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
# print(d1['simple_key'])

d2 = {'k1': {'k2':'hello'}}
# print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# print(d3['k1'][0]['nest_key'][1][0])

###############
## Problem 4 ##
###############

# Using a set to find the unique values of the list below:
myList = [1,1,1,1,1,2,2,2,2,3,3,3,3]
# print(set(myList))

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = 'Sammy'

# Use print formating to print the following string:
# Hello my dog's name is Sammy and he is 4 years old
# print('Hello my dog\'s name is {b} and he is {a} years old'.format(a=age,b=name))
