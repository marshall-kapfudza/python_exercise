#####################################
#### PART 9: FUNCTION EXERCISES ####
#####################################

# Complete the task below by writing functions! Keep in mind, these can be
# really tough, it's all about breaking the problems into smaller, logical
# steps. If you feel stuck, don't feel bad about having to pick to the solution

#####################
## ~~ PROBLEM 1 ~~ ##
#####################

# Given a list of intergers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1,1,2,3,1]) -> True
# arrayCheck([1,1,2,4,1]) -> True
# arrayCheck([1,1,2,1,2,3]) -> True

def arrayCheck(nums):
  return (1,2,3)[-1] in nums
# print(arrayCheck([1,1,2,3,1]))
# print(arrayCheck([1,1,2,4,1]))
# print(arrayCheck([1,1,2,1,2,3]))

  # Instructor Solution
  # for i in range(len(nums)-2):
  #   if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
  #     return True
  # return False


#####################
## ~~ PROBLEM 2 ~~ ##
#####################

# Given a string, return a new string made of every other character starting
# with first, so "Hallo" yields "Hlo"

# For example

# stringBits('Hello') -> 'Hlo'
# stringBits('Hi') -> 'H'
# stringBits('Heeeololeo') -> 'Hello'

def stringBits(mstr):   
  return mstr[::2]
# print(stringBits('Hello'))
# print(stringBits('Hi'))
# print(stringBits('Heeololeo'))

  # Instructor Solution
  # result = ''
  # for i in range(len(mstr)):
  #   if i%2 == 0:
  #     result = result + mstr[i]
  # return result

#####################
## ~~ PROBLEM 3 ~~ ##
#####################

# Given two strings, return True if either of the string appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase vesion of a string.
#
# Examples
#
# end_other('Hiabc', 'abc') -> True
# end_other('AbC', 'HiaBc') -> True
# end_other('abc', 'abXabc') -> True

def end_other(a, b):
  return a[-3::].lower() == b[-3::].lower()
# print(end_other('Hiabc', 'abc'))
# print(end_other('AbC', 'HiaBc'))
# print(end_other('abc', 'abXabc'))

  # Instructor Solution
  # a = a.lower()
  # b = b.lower()
  # return a[-(len(b)):] == b or a == b[-(len(a)):]

#####################
## ~~ PROBLEM 4 ~~ ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') -> 'TThhee'
# doubleChar('AAbb') -> 'AAAAbbbb'
# doubleChar('Hi-there') -> 'HHii--tthheerree'

def doubleChar(mstr):
  return ''.join([s*2 for s in mstr])
# print(doubleChar('The'))   
# print(doubleChar('AAbb'))   
# print(doubleChar('Hi-there'))

  # Instructor Solution
  # results = ''
  # for char in mstr:
  #   results += char*2
  # return results

#####################
## ~~ PROBLEM 5 ~~ ##
#####################

# Given 3 int values, a b c, return their sum. However, if any of these values is a
# teen -- in the range 13 - 19 inclusive -- then that value counts as 0, exept 15
# and 16 do not count as a teens. Write a seperate helper "def fix_teen(n):" that
# takes in an int value and returns that value fixed for the teen rule.
# 
# In this way, you avoid repeating the teen code three times (i.e "decomposition").
# Define the helper below at the same indent level as the main no_teen_sum().
# Again, you will have two function for this problem!
# 
# Examples:
# no_teen_sum(1, 2, 3) -> 6
# no_teen_sum(2, 13, 1) -> 3
# no_teen_sum(2, 1, 14) -> 3

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
  if n in [13, 14, 17, 18, 19]:
    return 0
  return n
# print(no_teen_sum(2, 15, 1))

#####################
## ~~ PROBLEM 6 ~~ ##
#####################

# Return a number of even integers in a given array.
#
# Examples
#
# count_evens([2, 1, 2, 3, 4]) -> 3
# count_evens([2, 2, 0]) -> 3
# count_evens([1, 3, 5]) -> 0

def count_evens(nums):
  count = 0
  for i in nums:
    if i % 2 == 0:
      count += 1
  return count
# print(count_evens([2, 1, 2, 3, 4]))