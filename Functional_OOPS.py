
# coding: utf-8

# # Functions as First-Class objects

# In[13]:


def hello_world(h):
      def world(w):
              print(h, w)
      return world # returning functions

h = hello_world # assigning
x = h("hello") # assigning

#h("hello")


x("world") # (h("hellow),"world")

 #storing functions in a list
function_list = [h, x]
print(function_list)


# In[ ]:





# In[14]:


# procederal implementation
# Here we are specifying how to do summation
def naive_sum(list):
    s = 0 # counter 
    for l in list:
        s += l
    return s
naive_sum([1,2,67])


# In[15]:


# functional implementation with built-in function
sum(list)


# # Programming Functionally: Reducing usage of Loops

# In[23]:


# The below construct stems from the traditional thinking of visualizing
# the whole program as a series of steps where you define how things need to be done.
for x in l:
    func(x)


# # Map

# In[20]:


# using map to apply functions to objects
# the function map, maps functions to the some iterable object

# simple example
list(map(int, ["1", "2", "3"]))

# another example 
def add_by_5(i):
    return i + 5

list(map(add_by_5,[1,2,3,4]))


# In[53]:


# Map returns an iterable object
map_ = (map(int,(["1","2","3"])))


# In[56]:


next(map_)


# In[41]:


alist = ["uday","Madhan"]


# In[45]:


# map_list = [1,2,3]
map_list = [print(i) for i in map_]


# In[46]:





# In[ ]:


map_ = map(int(["1","2","3"]))


# In[63]:


# one-time function
square = map(lambda x: x*x,[5,6,7])
next(square)


# ### Lambda

# In[61]:


# lambda function to get the square of a number
# temporary functions

square = lambda x: x*x

square(5)
print(square)


# In[58]:


def square(number):
    return (number**2)

print(square(5))
print(square())


# In[24]:


# we can use the lambda expression to make procedural code functional

# procedural code
starting_number = 96

# get the square of the number
square = starting_number ** 2

# increment the number by 1
increment = square + 1

# cube of the number
cube = increment ** 3

# decrease the cube by 1
decrement = cube - 1

# get the final result
result = print(decrement) # output 783012621312


# In[25]:


# define a function `call` where you provide the function and the arguments
def call(x, f):
    return f(x)

# define a function that returns the square
square = lambda x : x*x

# define a function that returns the increment
increment = lambda x : x+1

# define a function that returns the cube
cube = lambda x : x*x*x

# define a function that returns the decrement
decrement = lambda x : x-1

# put all the functions in a list in the order that you want to execute them
funcs = [square, increment, cube, decrement]

#map(lambda x: x*x,96)
#map(lambda x: x+1,96)
#map(cube,96)

# bring it all together. Below is the non functional part. 
# in functional programming you separate the functional and the non functional parts.
from functools import reduce # reduce is in the functools library
print(reduce(call, funcs, 96)) # output 783012621312


# In[75]:


# Another example of reduce

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
    print(product)
    
    # Versus

from functools import reduce
product_reduce = reduce((lambda x, y: x * y), [1, 2, 3, 4])
#product_map = map((lambda x, y: x * y), [1, 2, 3, 4])


# In[ ]:


def fibo()


map(fibo ,[2,3,4,5,6])


# In[76]:



product_reduce


# In[1]:


# Zip

keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)


# # Iterators

# In[5]:


L = [1,2,3]
it = iter(L)
print(type(it))

print(it.__next__())  # same as next(it)

print(next(it))
print(next(it))
next(it)


# In[78]:


iterable = iter([1,2,3])

                 


# In[80]:





# A for loop is also an iterator and under the hood is supporte by the iter() function

# In[82]:


# Plain for loop
List_1 = ["Kapil","Aakash","Sirisha"]

for name in List_1: 
    print(name)


# In[83]:


# for loop implementation via iter() 
fetch = iter(List_1) #if we print(type) --> we have an iterable object
while True:
	try:
		i = fetch.__next__() #iterator method
	except StopIteration:
		break
	print(i)


# In[ ]:


for i in List_1:


# # Generators

# In[92]:




def add_exclamation(list_):
    for i in list_:
        i = i + "!"
        print(i)
    return i
list1 = ["uday","keith"]
print(add_exclamation(list1))


# In[109]:


def generate_ints(N):
    for i in range(N):
        yield(i)


# In[110]:


gen = generate_ints(5)


# In[111]:


print(gen)


# In[116]:


next(gen)


# In[117]:


next(gen)


# In[97]:


next(gen)


# In[16]:


from random import randint 
def randGen(aList):
    while len(aList) > 0:
        yield aList.pop(randint(0, len(aList)))
print(randGen([4,5,6]))


# In[122]:


import time

def factorial():
    kafnsklfn

start = time.time()



end  = time.time()

time_taken = (end-start)

print(time_taken)


# In[120]:


start


# In[ ]:




