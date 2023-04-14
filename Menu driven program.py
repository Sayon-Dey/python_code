#!/usr/bin/env python
# coding: utf-8

# In[3]:


def add(num1, num2):
    print('Sum =', num1+num2)

def sub(num1, num2):
    print('Sub =',num1-num2)

def mul(num1, num2):
    print('Mul =',num1*num2)

def div(num1, num2):
    print('Div =',num1/num2)

def mod(num1, num2):
    print('Mod =',num1%num2)

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
opt = int(input('Enter your choice from [1-5]: '))

if opt == 1:
    add(num1, num2)
elif opt == 2:
    sub(num1, num2)
elif opt == 3:
    mul(num1, num2)
elif opt == 4:
    div(num1, num2)
elif opt == 5:
    mod(num1, num2)
else:
    print('Invalid choice.')


# @ 3.Area

# In[5]:


def aos(num1):
    print('Area of square',num1**2)
def aor(num1,num2):
    print('Area of rectangle',num1+num)
def aoc(num1):
    print('Area of circle',3.14*num1*num1)
def aot(num1,num2):
    print('Area of triangle',1/2*num1*num2)
    
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
opt = int(input('Enter your choice from [1-4]: '))
if opt == 1:
    aos(num1)
elif opt == 2:
    aor(num1, num2)
elif opt == 3:
    aoc(num1, num1)
elif opt == 4:
    aot(num1, num2)
else:
    print('Invalid choice.')


# # 2.perimeter

# In[9]:


def pos(num1):
    print('The perimeter of a square',4*num1)
def por(num1,num2):
    print('The perimeter of a rectangle',2*(num1+num2))
def poc(num1):
    print('The perimeter of a circle',2*3.14*num1)
def pot(num1,num2,num3):
    print('The perimeter of a triangle',num1+num2+num3)
    num1=int(input('Enter the value'))
    num2=int(input('Enter the value'))
    opt = int(input('Enter your choice from [1-4]: '))
if opt == 1:
    pos(num1)
elif opt == 2:
    por(num1, num2)
elif opt == 3:
    poc(num1)
else:
    print('Invalid choice.')


# In[10]:


def pos(num1):
    print('The perimeter of a square', 4*num1)

def por(num1, num2):
    print('The perimeter of a rectangle', 2*(num1+num2))

def poc(num1):
    print('The perimeter of a circle', 2*3.14*num1)

def pot(num1, num2, num3):
    print('The perimeter of a triangle', num1+num2+num3)

num1 = int(input('Enter the value of num1: '))
num2 = int(input('Enter the value of num2: '))
opt = int(input('Enter your choice from [1-4]: '))

if opt == 1:
    pos(num1)
elif opt == 2:
    por(num1, num2)
elif opt == 3:
    poc(num1)
elif opt == 4:
    num3 = int(input('Enter the value of num3: '))
    pot(num1, num2, num3)
else:
    print('Invalid choice.')


# # 4.Volume 

# In[12]:


def vos(num1):
    print('The volume of a sphere',4/3*3.14*num1*num1*num1)
def voc(num1,num2):
    print('The volume of a cylinder',3.14*num1*num1*num2)
def voc(num1):
    print('The volume of cube',num1*num1*num1)
def voc(num1,num2):
    print('The vollume of cone is',3.14*num1*num1*num2/3)
num1 = int(input('Enter the value of num1: '))
num2 = int(input('Enter the value of num2: '))
opt = int(input('Enter your choice from [1-4]: '))

if opt == 1:
    vos(num1)
elif opt == 2:
    voc(num1, num2)
elif opt == 3:
    voc(num1)
elif opt == 4:
    voc(num1, num2)
else:
    print('Invalid choice.')


# In[ ]:




