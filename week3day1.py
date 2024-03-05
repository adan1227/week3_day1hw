#!/usr/bin/env python
# coding: utf-8

# # Map, Filter, Reduce, Lambda & Recursion

# ## Tasks Today:
# 
# 1) <b>Lambda Functions</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Saving to a Variable <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Multiple Inputs <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Passing a Lambda into a Function <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Returning a Lambda from a Function <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) In-Class Exercise #1 <br>
# 2) <b>Map</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Using Lambda's with Map <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #2 <br>
# 3) <b>Filter</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Using Lambda's with Filter <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #3 <br>
# 4) <b>Reduce</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Using Lambda's with Reduce <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #4 <br>
# 5) <b>Recursion</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Implementing a Base <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Writing a Factorial Function <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #5 <br>
# 6) <b>Generators & Iterators</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Yield Keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Inifinite Generator <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #6 <br>
# 7) <b>Exercises</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Exercise #1 - Filtering Empty Strings <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Exercise #2 - Sorting with Last Name <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Exercise #3 - Conversion to Farhenheit <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Exercise #4 - Fibonacci Sequence <br>

# ## Lambda Functions <br>
# <p>Lambda functions... or "Anonymous Functions" are referring to inline functions with no name. The keyword lambda denotes the no name function, and executes within a single line. Without saving it to a variable; however, it is not able to be used, unless passed in either as a paramater or within list comprehension.<br>Written as "(keyword lambda) (one or more inputs) (colon) (function to be executed)"</p>

# #### Syntax

# In[ ]:


(lambda num: num + 2)(5)


# #### Saving to a Variable

# In[ ]:


add_nums = lambda num1, num2: num1 + num2

add_nums(4,5)


# #### Multiple Inputs

# In[ ]:


lambda string1, string2: f'{string1} + {string2}')('foo', 'bar')


# #### Passing a Lambda into a Function

# In[ ]:


def math_ooperations(func, num):
    return func(num)

math_operations(lambda num: num * 2, 8)

math_operations(lambda num: num // 2, 50)


# #### Returning a Lambda from a Function

# In[ ]:


def outter_func(num):
    inner_fun_var = 'foo'
    
    return lambda astring: f'{inner_func_var} {str1} {astring}'

addToFooBar = outter_func('fizz')

addToFOoBar('spam')



# #### If Statements within Lambdas

# In[ ]:


def foobar():
    if True:
        return True
    else:
        return false
    
    lambda astring: astring.upper() if astring[0].lower()  in 'aeiou' else astring
    
    print(upperVowel('octopus'))
    
    upperVowel('dylan')


# #### In-Class Exercise #1 <br>
# <p>Write an anonymous function that cubes the arguments passed in and assign the anonymous function to a variable 'f'.</p>

# In[ ]:


more_readable = (lambda num: num**3 if num % 2 == 0 else num **2) (2)

print(more_readable)


# ## Map <br>
# <p>The map function allows you to iterate over an entire list while running a function on each item of the list. This is why the map function works well with lambda's, because it simplifies things and you write less lines of code.<br>The syntax for a map function is "map(function to be used, list to be used)"<br>However, you must be careful, as the map function returns a map object, not a list. To turn it into a list we use the list() type conversion.</p>

# #### Syntax

# In[2]:


list(map(lambda astring: astring.upper(), ['foo', 'bar', 'spamn', 'eggs']))

def capitalize_string(astring):
    return astring.upper()

[word for word in map(capitalize_string, ['foo', 'bar', 'fizz', 'buzz']) ]


# #### Using Lambda's with Map

# In[ ]:


nums_plus_ten = map( lambda num: num + 10, [3, 4, 8, 29] )

list(nums_plus_ten)


# #### In-Class Exercise #2 <br>
# <p>Use the map function to double each number and minus it by one in the list by using a lambda function</p>

# In[4]:


number - [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2 -1, numbers))
print(squared_numbers)


# ## Filter() <br>
# <p>Filter's are similar to the map function, where you're able to pass a function argument and a list argument and filter out something from the list based on the conditions passed. Similar to the map function, it returns a filter object, so you need to type convert it to a list()</p>

# #### Syntax

# In[5]:


list(filter(lambda astring: True, [12,3,1,3,18]))


# #### Using Lambda's with Filter()

# In[9]:


list(filter(lambda num: num % 2 == 0 else False, [3,8,27,1,3,22]))

student = ['robin','tony','rhett','carlos','zack','zoey']

[word for word in filter( lambda name: name[0].lower9() != 'z', students) ]

def divisible_by_ten(num):
    return num % 10 == 0

list(filter(divisible_by_ten, [10,33,20,30,455]))


# #### In-Class Exercise #3 <br>
# <p>Filter out all the numbers that are below the mean of the list.<br><b>Hint: Import the 'statistics' module</b></p>

# In[ ]:





# ## Reduce() <br>
# <p>Be very careful when using this function, as of Python 3 it's been moved to the 'functools' library and no longer is a built-in function.<br>The creator of Python himself, says to just use a for loop instead.</p>

# #### Syntax

# In[ ]:





# #### Using Lambda's with Reduce()

# In[ ]:





# #### In-Class Exercise #4 <br>
# <p>Use the reduce function to multiply the numbers in the list below together with a lambda function.</p>

# In[ ]:





# ## Recursion <br>
# <p>Recursion means that a function is calling itself, so it contanstly executes until a base case is reached. It will then push the returning values back up the chain until the function is complete. A prime example of recursion is computing factorials... such that 5! (factorial) is 5*4*3*2*1 which equals 120.</p>

# #### Implementing a Base Case

# In[11]:


def add_recursive(num):
    if num == 0:
        print(f'add_recurs({num}) = 0')
        return num
    print(f'add_recurs({num} = {num} + add_recurse({num = 1})')    
    return add_recursive(num - 1) + num

add_recursive(5)


# #### Writing a Factorial Function

# In[12]:


def find_factorial(num):
    if num == 1:
        print(f'find_factorial({num}) = {num}')
        return num
    print(f'find_factorial({num}) = {num} * find_factorial({num - 1})')
    return num * find_factorial(num - 1)

find_factorial(5)


# #### In-Class Exercise #5 <br>
# <p>Write a recursive function that subtracts all numbers to the argument given.</p>

# In[ ]:





# ## Generators <br>
# <p>Generators are a type of iterable, like lists or tuples. They do not allow indexing, but they can still be iterated through with for loops. They are created using functions and the yield statement.</p>

# #### Yield Keyword <br>
# <p>The yield keyword denotes a generator, it doesn't return so it won't leave the function and reset all variables in the function scope, instead it yields the number back to the caller.</p>

# In[ ]:


def range_generator(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step
        
my_range = range_generator(1,10,2)

print(my_range)

print([num for num in my_range])

print([num for num in my_range])

my_range2 = range_generator(0,20,2)

next(my_range2)
next(my_range2)
next(my_range2)
next(my_range2)

print([ num for num in my_range2])



# #### Infinite Generator

# In[ ]:


# bad, never create infinite loops


# #### In-Class Exercise #6 <br>
# <p>Create a generator that takes a number argument and yields that number squared, then prints each number squared until zero is reached.</p>

# In[ ]:





# # Exercises

# ### Exercise #1 <br>
# <p>Filter out all of the empty strings from the list below</p>
# 
# `Output: ['Argentina', 'San Diego', 'Boston', 'New York']`

# In[13]:


places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

filtered_places = list(filter(lambda x: x.strip() != "", places))

print(filtered_places)


# ### Exercise #2 <br>
# <p>Write an anonymous function that sorts this list by the last name...<br><b>Hint: Use the ".sort()" method and access the key"</b></p>
# 
# `Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']`

# In[14]:


author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key=lambda x: x.split()[-1].lower())

print(author)


# ### Exercise #3 <br>
# <p>Convert the list below from Celsius to Farhenheit, using the map function with a lambda...</p>
# 
# `Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
# `

# In[ ]:


# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

places_fahrenheit = list(map(lambda x: (x[0], (9/5) * x[1] + 32), places))

print(places_fahrenheit)


# ### Exercise #4 <br>
# <p>Write a recursion function to perform the fibonacci sequence up to the number passed in.</p>
# 
# `Output for fib(5) => 
# Iteration 0: 1
# Iteration 1: 1
# Iteration 2: 2
# Iteration 3: 3
# Iteration 4: 5
# Iteration 5: 8`

# In[16]:


def fib(n, a=0, b=1, iteration=0):
    if iteration == n:
        return b
    else:
        print(f"Iteration {iteration}: {b}")
        return fib(n, b, a + b, iteration + 1)


# In[ ]:





# In[ ]:




