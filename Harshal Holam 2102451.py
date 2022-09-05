#!/usr/bin/env python
# coding: utf-8

# ## Harshal Shivaji Holam - 2102451
# ## Python Notebook

# 
# # 25 / 07 / 2022

# #### what are variables?
#  variable are name given to an object

# In[2]:


x = 5


# In[4]:


harsh = 9


# In[6]:


harsh


# In[7]:


print = 6


# In[9]:


print


# In[12]:


#for = 9  #it cant be run as for is keyword ...there are 33 keywords


# In[14]:


A=5
a=6   #both are different as python is case sensitive


# In[17]:


_harsh = 9   #variables can start only with speacial character underscore


# In[21]:


#   @harsh = 5  #it is invalid ... other than underscore
# 9harsh = 2 #invalid as variables can start only with alphabet or underscore


# # Data Types
# there are four data types
# 1. integer
# 2. float
# 3. string
# 4. boolean
# 

# ### Integer

# In[23]:


a = 5
type(a)


# ### Float

# In[25]:


f = 5.9
type(f)


# ### Boolean

# In[31]:


a=5
b=6
a==b


# In[37]:


k=9
h = 9
k == h


# ### string

# In[38]:


a = "harsh"
type(a)


# # 25 / 07 / 2022

# # Operators
# 1.arithmatic
# 2.comparison
# 3.logical

# ### ARITHMATIC

# In[41]:


#ADDITION
a=9
b=7
k=a+b
k


# In[42]:


#SUBSTRACTION
a=9
b=7
k=a-b
k


# In[43]:


#MULTIPLICATION
a=9
b=7
k=a*b
k


# In[44]:


#DIVISION
a=9
b=7
k=a/b
k


# In[45]:


#MODULO  
a=9
b=7
k=a%b
k


# In[47]:


#FLOOR DIVISION
a=9
b=7
k=a//b
k


# In[49]:


#EXPONENT
a=9
b=7
k=a**b
k


# ### COMPARISON

# In[51]:


#GRETER THAN
a=9
b=7
k=a>b
k


# In[52]:


#LESS THAN
a=9
b=7
k=a<b
k


# In[54]:


#NOT EQUALS TO
a=9
b=7
k=a!=b
k


# In[56]:


#GREATER THAN EQUALS TO
a=9
b=7
k=a>=b
k


# ### LOGICAL
# ##### AND = if both the arguments are true then it is true ....ow its false
# ##### OR = if either of the argument are true then it is true .... ow its false
# ##### NOT = opposite of logical answer

# In[57]:


#AND
a=9;b=7
a<10 and b >6


# In[59]:


#AND
a=9;b=7
a>10 and b >6


# In[61]:


#OR
a=9;b=7
a<10 or b >6


# In[63]:


#OR
a=9;b=7
a>10 or b <6


# In[67]:


#NOT
a=5
not a >4


# # CONDITIONAL
# *if statement 
# *if else
# *for loops
# *break and continue
# *relational operator
# *boolean operator|

# In[ ]:


fruits = ['Apple','Banana','Guava']
for i in fruits:
    print(i)


# In[2]:


# if else
a=98
b=45
if (a>b):
    print("a is greater than b")
else:
    print("a is less than b")


# In[3]:


a=input(int)
b=input(int)
if (a>b):
    print("a is greater than b")
else:
    print("a is less than b")


# In[10]:


age = 15
if (age > 18):
    print("eligible for voting")
elif (age == 18):
    print("yes ! , you are eligible or voting")
else:
    print("sorry you are not eligible for voting!")


# In[32]:


passing_marks =60
student_score = int(input())
if (student_score >= passing_marks):
    print("congratulations!, you have passed the exam")
else:
    print("Fail")
    print("better luck next time")


# In[ ]:


#if student want to passed the exam he msut secured marks gretaer than equals to 60 out of 100
passing_marks =60
student_score = int(input())
if (student_score >= passing_marks):
    print("congratulations!, you have passed the exam")


# In[ ]:


fruits = ['Apple','Banana','Guava']
for i in fruits:
    print(i)
    fruits=='Banana'
    break


# In[ ]:


fruits = ['Apple','Banana','Guava']
for i in fruits:
    if i == 'Banana':
        continue
    print(i)


# In[ ]:


for i in "HARSHAL":
    if i == 'S':
        break
    print(i)


# In[ ]:


a=int(input())
b=int(input())
if (a!=b):
    print("a is not equal to b")
else:
    print("a is equal to b")


# In[ ]:


a = 30
b = 45
if(a > 30 and b == 45):
    print("True")

else:
    print("False")


# In[ ]:


a =8
b =9
if(not(a == b)):
  print("If Executed")
else:
  print("Else Executed"


# # Looping construct

# In[24]:


for marks in range(87,99,2):       #87 as starting point , 99 as ending point , 2 as difference
    print( marks)


# In[16]:


for a in range(5):   #5 is end point but its not include
    print(a)


# In[17]:


for a in range (5,10):   #5 is start point and 10 is end point
    print(a)


# In[25]:


#loops for strings
word= 'Harshal'
for char in word:
    print(char)


# In[26]:


#for alternative output
for char in word[::2]:
    print(char)


# In[27]:


for i in range(10):    #stop condition
    print("I love India")


# In[31]:


#Nested for loop
#define the range of outer loop 
for i in range(1,4):        #outer loop
    for j in "HARSHAL ":         #inner loop       #it take space also
        print(i,j)


# In[34]:


n=0
while (n<4):
    print(n)
    n=n+1


# # Data structure

# In[36]:


list=[87,93,'India','pune',['NAshik','Mumbai']]


# In[38]:


#extraction
list[2]     #no starting from 0


# In[40]:


list[2:4]  #2 is start index and 4 is end index


# In[50]:


list[-2]


# In[43]:


#add element in list
list.append(4)
list


# In[45]:


#add multiple element
list.extend(['harshal','red'])
list


# In[46]:


#adding list in list
list.append([1,2])
list


# In[48]:


#delete element from list
list.remove(4)
list


# In[49]:


#delete element from list by indexing
del list[2]
list


# In[52]:


list.index('harshal')


# In[53]:


list.insert(2,'F')         #insert 'F' in the 2nd position
list


# In[55]:


'red' in list  #presence of list


# In[56]:


len(list)


# In[62]:


b=list.reverse()
b


# In[63]:


list


# In[65]:


list[4][1] #access element from list of list


# #### set

# In[68]:


#Student score
scores=[['Name', ['A','B','C','D','E']],
               ['Harsh', [55,22,24,65,78]],
               ['roh', [50,39,42,49,70]],
               ['xyz', [60,89,48,20,93]],
               ['bkp', [80,67,39,81,99]],
               ['swk', [90,67,50,96,90]]]


# In[69]:


scores


# In[71]:


scores[5]   #extraction


# In[72]:


#difference between two sets
set1={1,2,3,6,8,9}
set2={2,3,7,5,4,0}
set1.difference(set2)


# In[73]:


set1.intersection(set2)


# In[74]:


#check two sets are disjoint
set1.isdisjoint(set2)


# In[75]:


#subset or not
set1.issubset(set2)


# In[76]:


#superset?
set1.issuperset(set2)


# In[77]:


set1.update({778,85})
set1


# In[78]:


set1.union(set2)


# #### dictionary

# In[79]:


dict = {1: 'apple', 2: 'ball'}


# In[80]:


dict


# In[82]:


dict[1]   #accessed by key


# In[85]:


dict[3]='cat'   #add element 
dict


# In[88]:


#add multiple element
dict.update({4: 'xyz',5:'ghat'})
dict


# In[89]:


del dict[1] 
dict


# #### Function

# In[90]:


class ATMmachine:
    def cashwithdrawal(self):
        print("welcome to ATM")
        pin =int(input("write your pin: "))
        print("successful")
        amount=int(input("pls enter your amount: "))
        print("pls collect your cash")


# In[91]:


atm1=ATMmachine()


# In[93]:


atm1.cashwithdrawal()


# # Standard Libraries

# #### 1. Math

# In[94]:


import math #import library


# In[95]:


math.ceil(98.99) #smallest integer greater than or equal to x


# In[96]:


math.floor(98.999)  # the largest integer less than or equal to x


# In[98]:


math.comb(5,3)  # number of ways to choose k items from n items without repetition and without order


# In[101]:


math.copysign(5.2,-4.00) #Return a float with the magnitude (absolute value) of x but the sign of y.


# In[102]:


math.fabs(-89.55)   #Return the absolute value of x.


# In[103]:


math.factorial(3)  #Return x factorial as an integer


# In[107]:


math.gcd(42,28)      #gcd of two number


# #### 2. Random

# In[108]:


import random


# In[110]:


random.choice(['harshal','red','Nashik'])     #select random element from


# In[112]:


random.random()     #from 0 to 1 


# In[116]:


random.uniform(4,5)   #Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.

#The end-point value b may or may not be included in the range depending on floating-point rounding in the equation a + (b-a) * random().


# In[117]:


random.uniform(0,9)


# #### 3.Date and time

# In[7]:


from datetime import date
from datetime import time


# In[8]:


mydate = date(2000,10,29);mydate


# In[9]:


today=date.today()
print(today)


# In[12]:


#format date
print("Formatted date:",mydate.strftime("%d %b %Y"))


# In[10]:


#format date
print("Formatted date:",mydate.strftime("%m-%d-%y"))


# In[14]:


#format date
print("Formatted date:",today.strftime("%A on the %d day of %B"))


# In[17]:


#dates support calendar arithmetic
birthday=mydate
age=today-birthday
print("Age in days",age.days)


# #### 4. NUMPY

# In[18]:


import numpy as np


# In[19]:


np.__version__   #check version


# In[33]:


a=np.array([5,4,3,2,1])
a


# In[29]:


(np.array([5,8,9,6,'True']))


# In[23]:


type(np.array([5,8,9,6,'True']))


# In[25]:


xyz=[1,2,3,4,5]


# In[26]:


xyz*2


# In[34]:


a+2


# In[37]:


# Matrix using numpy
matrix=[[7,8,9,5],
       [4,5,6,8],
       [5,6,8,2],
       [6,5,2,3]]
matrix


# In[39]:


matrix=np.array(matrix)
matrix


# In[40]:


#extraction of element
matrix[3][3]


# In[43]:


#create matrix of random element
a=np.random.randint(0,10,(3,3))
b=np.random.randint(0,10,(3,3))


# In[44]:


a


# In[45]:


b


# In[46]:


a+b


# In[47]:


a-b


# In[48]:


a*b


# In[49]:


a+1


# In[50]:


b+5


# In[51]:


(a*b)+1


# In[52]:


#using random seed
np.random.seed(54)
np.random.randint(0,10,(3,3))


# In[56]:


#matrix of zeroes (3*3)
np.zeros((3,3),int)


# In[57]:


#matrix of ones
np.ones((3,3),int)


# In[58]:


np.ones((5,10),float)


# In[60]:


#identity matrix
np.identity(4,int)


# In[62]:


np.full((3,3),87)


# In[65]:


#Concatenation
a


# In[64]:


b


# In[68]:


matrix_concate = np.concatenate([a,b],axis=0) #row wise
matrix_concat


# In[70]:


matrix_concate = np.concatenate([a,b],axis=1) #column wise
matrix_concate


# #### 5.Pandas

# In[71]:


import pandas as pd


# In[73]:


data=pd.read_csv(r"C:\Users\LENOVO\Downloads\heart.data.csv")
data


# In[74]:


data.info


# In[75]:


data.shape


# In[76]:


data.dtypes


# In[77]:


data.columns


# In[79]:


data.isna().sum()   #check null values


# In[80]:


data.head(4)


# In[81]:


data.tail(4)


# In[82]:


data.describe()


# In[85]:


print(data.loc[495])


# In[94]:


data.corr()


# #### 6.matplotlib

# In[91]:


import matplotlib.pyplot as plt


# In[98]:


plt.title("smoking vs heart disease")
plt.plot("smoking","heart.disease",data=data)


# In[99]:


plt.title("biking vs heart disease")
plt.plot("biking","heart.disease",data=data)


# In[100]:


data.hist()
plt.show()


# In[105]:


plt.boxplot(data['smoking'])
plt.xlabel("smoking")
plt.show()


# In[106]:


plt.boxplot(data['biking'])
plt.xlabel("biking")
plt.show()


# In[107]:


plt.boxplot(data['heart.disease'])
plt.xlabel("heart.disease")
plt.show()


# In[ ]:




