#!/usr/bin/env python
# coding: utf-8

# # Exercise 6

# In[ ]:





# #### Problem 1
# 
# (True/False) The class object `str` has a method `capitalize()` which may be called explicitly as follows,
# 
# ```python
# string = "my string"
# 
# str.capitalize(string)
# ```

# In[6]:


problem1 = True # True or False


# #### Problem 2
# 
# Given a string `p2s`, assign to `problem2` a new string resulting from first capitalizing the first letter and then swapping the case of all the characters in `p2s` using a single statement through chaining method calls.

# In[116]:


#p2s = "together"
problem2 = (str.capitalize(p2s[0]) + p2s[1:]).swapcase()
#print(problem2)


# #### Problem 3
# 
# Given the string `p3s`, assign to `problem3` the sub-string resulting from concatenating every other (that is, each alternate: first, third, ...) character in `p3s` (starting with the first).

# In[4]:


problem3 = p3s[::2]


# #### Problem 4
# 
# Given the list `p4l`, assign to `problem4` the last item of the list.

# In[ ]:


problem4 = p4l[-1]


# #### Problem 5
# 
# Given the list `p5l` of numeric objects, assign `problem5` a new list with items (in order): the minimum value, the maximum value, and the average value in `p5l`.

# In[19]:


p5l.sort()
problem5 = [p5l[0],p5l[-1],sum(p5l)/len(p5l)]


# #### Problem 6
# 
# Develop a function `problem6(list1, list2)` that concatenates two copies of `list1` with three copies of `list2`.

# In[94]:


def problem6(list1, list2): 
    x = 2*(list1) + 3*(list2)
    return(x)


# #### Problem 7
# 
# Develop a function `problem7(lists)` that finds the first and last string (lexicographic order) in a list of strings `lists` and returns a new list with these items (in order).

# In[117]:


def problem7(lists):
    sorted = lists.sort()
    NewList = [lists[0],lists[-1]]
    return(NewList)


# #### Problem 8
# 
# Given lists `p8l1` and `p8l2` along with an object `p8i`, assign to `problem8` the value `True` if `p8i` is an item in both lists, otherwise `False`.

# In[110]:


problem8 = (p8i)
if p8i in list(p8l1) and p8i in list(p8l2):
    problem8 = True
else:
    problem8 = False
print(problem8)

