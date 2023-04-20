#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1.1
for i in range(10):
    print('Hello python')


# # 2.1

# In[6]:


for i in range(1,11):
    print(i)


# # 3.1

# In[12]:


sum=0
for i in range(1,11):
    sum+=i
print('the sum of fist number is',sum)


# # 4.1

# In[17]:


x=int(input('Enter the value'))
print("The list of n numbers from 1 to",x)
for i in range(1,n+1):
    print(i,end=' ')


# # 5.1

# In[20]:


num = int(input("Please enter the number: "))

sum = 0

for value in range(1, num + 1):
    sum = sum + value
    
print(sum)


# In[22]:


for i in range(1,11):
    print(2*i)


# # 7.1

# In[24]:


n=int(input("enter the number for factorial.: "))
factorial = 1
for i in range(1,n+1):
    factorial *=i
print("The factorial of given number is. ",factorial)


# # 8.1

# In[30]:


n =100
for i in range(2,n+1,2):
    print(i)


# # 9.1

# In[31]:


n =100
for i in range(1,n+1,2):
    print(i)


# # 2.2

# In[35]:


n=32
for i in range(1,n+1):
    if n%i==0:
        print('The factors are',i)


# # 7.2

# In[5]:


n = int(input('Enter the value'))
for i in range(1,n-1):
    reverse=i-1
    print('The reverse are',reverse)


# ## 4.2

# In[8]:


n = int(input('Enter the value'))
for i in range(1,n-1):
    reverse=i-1
    print('The reverse are',reverse)
    sum=n+reverse
    print('The sum of the numbers',sum)


# #8.2

# In[12]:


number = int(input("Enter a number"))

for i in range(1, number+1):
    cube = i**3  
    print('The cube of a number is',cube)


# # 1.3

# In[1]:


number = int(input("Enter a number: "))
count = 0

while number != 0:
    number //= 10
    count += 1

print("The number of digits in the entered number is:", count)


# ### 2.3

# In[3]:


n = int(input("Enter the number"))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# In[44]:


i=int(input('Enter the number'))
x=i
sum=0
while i<0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if x==sum:
    print('It is a armstrong number')
else:
    print('It is not a armstrong number')


# In[45]:


i=int(input('Enter the num'))
x=i
rev=0
while i>0:
    rev=(rev*10)+i%10
    i=i//10
if x==rev:
    print('It is a palindrome')
else:
    print('It is not a palindrome')


# # perfect number

# # write a python program to find those numbers which are divisible by 7 and multiple of 5

# In[5]:


x=int(input("Enter the lower range:"))
y=int(input("Enter the upper range:"))
for i in range (x,y+1):
    if(i%7==0 and i%5==0):
        print(i)


# # write a program to print the following number pattern

# In[15]:


# b star

for i in range(1,6):
    for j in range(1,6):
        if  j>=1:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()


# In[5]:


n=5
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()


# In[16]:


# a

for i in range(1,6):
    for j in range(1,6):
        if j<=1:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# # c

# In[37]:


n=int(input('Enter the num'))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print('*',end='')
    print()


# # e

# In[15]:


n=5
for i in range(n):
    for j in range(i,n):
        print('',end= ' ')    #Decreasing space
    for j in range(i+1):
        print('*',end='')     #Increasing star
    print()


# # d

# In[18]:


n=5
for i in range(n):
    for j in range(i+1):
        print('',end= ' ')    #increasing space
    for j in range(i,n):
        print('*',end='')     #decreasing star
    print()


# # a   Number

# In[27]:


n=int(input('Enter the value'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()


# In[28]:


n=5
s=5
for i in range(n):
    for j in range(i+1):
        print(j,end=' ')
        s-=1
    print()


# In[22]:


n=int(input('Enter the value'))
s=1
for i in range(n):
    for j in range(i):
        print(s,end=' ')
        s+=1
    print()


# # b

# In[29]:


n=int(input('Enter the value'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()


# # d

# In[36]:


n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()


# In[38]:


n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()


# # e

# In[42]:


n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()


# In[47]:


n=int(input('Enter the value'))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()


# # b alphabet

# In[1]:


n=int(input('Enter the value'))
for i in range(n):
    for j in range(i+1):
        print(chr(65+i) ,end=' ')
    print()


# In[3]:


n=int(input('Enter the value'))
for i in range(n):
    for j in range(i-1):
        print(chr(65+i) ,end=' ')
    print()


# In[8]:


n=int(input('Enter the value'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(65+i),end=' ')
    print()


# In[18]:


n=5
for i in range(n,0,-1):
    for j in range(i+1):
        print(chr(65+i),end=' ')
    print()


# # a

# In[26]:


n=int(input('Enter the value'))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j), end=' ')
    print()


# # c

# In[36]:


n=int(input('Enter the value'))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(64+j), end=' ')
    print()


# # d

# In[42]:


n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(64+i),end=' ')
    print()


# In[ ]:





# In[ ]:




