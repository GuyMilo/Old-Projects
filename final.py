#!/usr/bin/env python
# coding: utf-8

# # NE 111 Final

# **Aids:** You may use tools such as Jupyter Notebook (without opening other files), iPython, and a Text Editor with syntax highlighting and basic autocomplete. However, access to the lecture/exercise content or other resources on your computer, the Internet, etc. is forbidden.
# 
# **Length**: 2.5 hours, **including submission**
# 
# **Instructions (in addition to LEARN Announcement)**:
# 
# 1. Complete exam identification information and academic integrity statement in the following cell.
# 2. Complete exam the problems. Each problem will give you instructions on how to complete it properly. **Save your work often.**
# 3. Unless explicitly asked for it, you do not have to check the types of your input. Assume that the types are correct.
# 4. When you are finished, in this notebook, go to File -> Download As -> Python (.py). **Do not leave this to the last minute. Periodically try this to make sure that you can submit**.
# 5. Submit using instructions in the LEARN announcement.
# 6. You may submit the exam as many times as you wish, only your last submission will be graded.
# 7. Once you have left the exam room, no further submissions will be accepted.
# 8. If you wish to leave early **you must** get approval from the instructor, not the TAs, and have them sign you out.
# 
# ## Academic Integrity Statement
# 
# * All electronic devices are prohibited during the exam except for the following uses:
#     - Checking the LEARN news item for this exam periodically for any clarifications or corrections.
#     - Completing the exam (Jupyter Notebook, Interactive Python Interpreter, Text Editor with/without syntax highlighting and basic autocomplete)
# * No aids, references, or notes are allowed that are not specified above.
# * No communication with anyone, other than the course instructor, is allowed during the exam period unless there is an emergency.
# * No sharing of the exam content in anyway, doing so is a serious academic integrity offense which will result in, at minimum, failure of the exam and referal to the Associate Dean of Undergraduate Studies for further discipline.
# 
# Your digital signature below confirms your understanding of the exam instructions, the university’s [academic integrity policy](https://uwaterloo.ca/academic-integrity/integrity-students), and that the solution to the exam that you submit is your own work.

# In[ ]:


# Enter your full name and student ID as strings
Student_Name = "James-Edward Gray"
Student_ID   = "21015159"

# Your exam WILL NOT be graded unless you changing this value to True to 
# indicate that you understand and confirm the academic integrity statement above.
Academic_Integrity = True


# **Please remember to import NumPy before proceeding.** You are allowed to modify the import statement however you prefer but please remember that the concept questions have been designed with these import statements in mind.

# In[ ]:


import numpy as np


# ## Problem 1 Multiple Choice (5 points, 1 pt/each)
# 
# Instructions: Enter your answers in the code block that follows.
# 
# **1.** Which of these collections are mutable?
# 
# > **a)**  `str`
# 
# > **b)**  `list`
# 
# > **c)**  `dict`
# 
# > **d)**  `tuple`
# 
# > **e)**  `set`
# 
# 
# **2.** Consider the following code :
# ```python 
# def sort_list(alist):
#     if sorted(alist)!=alist:
#         sorted_list=alist.sort()
#         return sorted_list
#     else:
#         return a_list
# ```
# 
# which of the following statements are **True**
# 
# > **a)**  If we call the function on an unsorted list, it would return the sorted list. 
#     
# > **b)**  There is at least one error in the code.
# 
# > **c)**  The `sorted` and `.sort()` methods both return the same result.
# 
# 
# **3.** If `list1 = [6, 7, 8, 9]`, which of the following returns the list `[9, 8, 7, 6]` **without** changing the original list?
# 
# > **a)** `list1.reverse()`
# 
# > **b)** `list1[len(list1)::-1]`
# 
# > **c)** `list1[::-1]`
# 
# > **d)** `list1.sort(reverse=True)`
# 
# 
# **4.** Which of the following methods are incorrect for determining the average of all the numbers in a multidimensional array `A`?
# 
# > **a)**  `np.mean(A)`
# 
# > **b)**  `np.average(A)`
# 
# > **c)**  `np.sum(A)/A.size`
# 
# > **d)**  `np.sum(A)/len(A)`
# 
# > **e)**  `np.add(A)/A.size`
# 
# 
# **5.** Given the array $A$. Which of the following methods for making a new array, named $b$, would result in changes in $A$ if the values in $b$ are changed?
# 
# $$ 
# A = \left[ \begin{array}{cccc}
# 5 & 6 & 7 & 8 \\
# 9 & 10 & 11 & 12\\
# 13 & 14 & 15 & 16 \\
# 17 & 18 & 19 & 20 \end{array} \right], \quad 
# $$
# 
# > **a)** `b=A.flatten()`
# 
# > **b)** `b=A.ravel()`
# 
# > **c)** `b=A.view()`
# 
# > **d)** `b=A`

# In[ ]:


# Enter your Multiple Choice  answers here
MC_1 = "abce"  # E.g. "", "a", "ab", etc.
MC_2 = "b" 
MC_3 = "bc"
MC_4 = "e"
MC_5 = "ab"


# ## Problem 2 (5 points)
# Complete the function according to its docstring.

# In[ ]:


def find_location_of_first(input_string, character):
    if type(input_string) != str or type(character) != str:
        print("Invalid input")
        return(None)
    elif len(character) > 1:
        return None

    else:
        return({x for x in input_string if x == character})
    
    
    '''
    (str, str) -> int

    This function takes two arguments, `input_string`, a string of some length and `character` a string containing a single character.
    It returns the index of the first occurance of the `character` in `input_string`.

    If the inputs are invalid or if `character` does not occur in `input_string` return None.

    >>> find_location_of_first(123, 47)
    None  # Invalid input

    >>> find_location_of_first('HELLO', 'H')
    0

    >>> find_location_of_first('HELLO', 'L')
    2  # Find the first 'L'

    >>> find_location_of_first('HELLO', 10)
    None  # Invalid input

    >>> find_location_of_first('HELLO', 'P')
    None  # `character` isn't in the `input_string`
    '''
    pass


# ## Problem 3 (5 points)
# Complete the function according to its docstring.

# In[ ]:


def count_down(n):
    if type(n) != int:
        print("please enter an integer")
        return None
    else:
        if n < 0:
            n = abs(n)
            print("next time enter positive int")
            tuplea = tuple(sorted(range(1,n+1), reverse=True))
            return(tuplea)
        elif n == 0:
            return None
        else:
            tuplea = tuple(sorted(range(1,n+1), reverse=True))
            return(tuplea)
count_down()


# ## Problem 4 (5 points)
# Complete the function according to its docstring.

# In[ ]:


def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
    
    '''
    int -> int

    Return, as an integer, the sum of digits for the provided integer `number`.

    >>> sum_of_digits(23)
    5  # 2 + 3

    >>> sum_of_digits(100)
    1  # 1 + 0 + 0

    >>> sum_of_digits(12345)
    15  # 1 + 2 + 3 + 4 + 5 
    '''

sum_of_digits()


# ## Problem 5 (10 points)
# Complete the function according to its docstring.
# 
# **DO NOT USE THE BUILT-IN max(), numpy.max(), OR ANY OTHER BUILT-IN MAX FUNCTION. YOU MUST WRITE IT YOURSELF. USING THE BUILT-IN FUNCTIONS WILL RESULT IN A GRADE OF ZERO ON THIS QUESTION.**

# In[ ]:


def max_of_list(input_list):
	if len(input_list) == 0:
		return(None)
	else:
		newlist = sorted(input_list, reverse=True)
		return(newlist[0])
max_of_list()


# ## Problem 6 (10 points)
# Complete the function according to its docstring.
# 
# **DO NOT USE TRY-EXCEPT. DOING SO WILL RESULT IN ZERO MARKS FOR THIS QUESTION.**

# In[ ]:


def can_apply_operations(array1, array2):
    if array1.ndim == array2.ndim:
        if array1.shape[:] != array2.shape[:]:
            return(False)
    elif array1.ndim != array2.ndim and array1.ndim or array2.ndim != 1:
        if array1[0:] != array2[0:] or array1[:1] != array2[0:]:
            print(False)
    elif array1.ndim != array2.ndim and array1.ndim or array2.ndim == 1:
        if array1[0] != array2[0] or array1[0] != array2[1:0]:
            print(False)
    else:
        print(True)
    can_apply_operations()
    '''
    (ndarray, ndarray) -> bool

    **DO NOT USE TRY-EXCEPT. DOING SO WILL RESULT IN ZERO MARKS FOR THIS QUESTION.**

    Return a `True` if binary arithmetic opertions (+, -, \*, etc) 
    can be applied on the arrays `array1` and `array2`, or `False` otherwise.

    >>> can_apply_operations(np.array([1, 2]), np.array([[1, 1], [2, 2]]))
    True

    >>> can_apply_operations(np.array([1, 2, 1]), np.array([[1, 1], [2, 2]]))
    False

    >>> can_apply_operations(np.array([[1, 2], [3, 4]]), np.array([[[9, 8], [7, 6]], [[5, 4], [3, 2]], [[1, 0], [1, 2]]]))
    True
    '''
    pass


# ## **OPTIONAL BONUS:** Problem 7 (1 point)
# This question is completely optional. There are no part marks for this question.
# 
# Complete the function according to its docstring.

# In[ ]:


def merge_dictionary(a, b):
    '''
    (dict, dict) -> dict

    This function takes two dictionaries, `a` and `b`, and returns a new dictionary, `c`, containing the entries from both `a` and `b`. 

    Both `a` and `b` will use strings as keys, and lists as values.
    If a key, `K`, is present in both `a` and `b` then the new dictionary should have an entry for it 
    and the value associated with `K` should be the result of concatenating the values in `a[K]` and `b[K]`, in that order.

    Note: DO NOT modify either `a` or `b`. Take care not to do this directly, or indirectly.

    >>> merge_dictionary({'hello': ['world']}, {'beep': ['boop']})
    {'hello': ['world'], 'beep': ['boop']}

    >>> merge_dictionary({'hello': ['world']}, {'hello': ['moto']})
    {'hello': ['world', 'moto']} # 'hello' is key for both `a` and `b`, so `a['hello']` is concentenated with `b['hello']`
    '''
    pass

