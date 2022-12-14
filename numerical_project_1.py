# -*- coding: utf-8 -*-
"""Numerical Project 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lyn1GLwz1eqPKnp2vIfdwsnHG8o3yB0b
"""

#@title Evaluator
import math
def function(x,equation):
    y=eval(equation)
    return y

#@title Bisection Method
def bisection(xl,xu,epislon,iterations,equation):
  iterator=1
  e_a=10000.0
  flag=True

  while e_a>epislon and  iterator<iterations:
    if function(xl,equation)*function(xu,equation)<0:    
      xr=(xl+xu)/2
      
      # print("iteration number :",iterator)
      # print("xlower is :",xl)
      # print("xupper is :",xu)
      # print("xaverage is :",xr)
      # print("function of xr is :",function(xr,equation))

      if function(xl,equation)<function(xu,equation):
        if function(xr,equation)<0:
          xl=xr
        else:
          xu=xr
          
      else:
        if function(xr,equation)<0:
          xu=xr
        else:
          xl=xr
      
      if iterator==1:
     #   print("relative approxmate error is ",e_a)
        pass
      
      else:
        e_a=abs((float(xr-xr_old)/float(xr)))*100
        #print("relative approxmate error is ",e_a)

      xr_old=xr
      iterator+=1
    else:
      print("No Root")
      flag=False
      break;
  if flag==True:
    return xr

#@title FalsePosition Method
def FalsePosition(xl,xu,epislon,iterations,equation):
  iterator=1
  e_a=10000.0
  flag=True

  while e_a>epislon and  iterator<iterations:
    if function(xl,equation)*function(xu,equation)<0:    
      xr=(xu*function(xl,equation)-xl*function(xu,equation))/(function(xl,equation)-function(xu,equation))

      if(function(xr,equation)==0):
        return xr
      
      print("iteration number: ",iterator)
      print("xlower is: ",xl)
      print("xupper is: ",xu)
      print("xaverage is: ",xr)
      print("function of xr is: ",function(xr,equation))

      if function(xl,equation)<function(xu,equation):
        if function(xr,equation)<0:
          xl=xr
        else:
          xu=xr
          
      else:
        if function(xr,equation)<0:
          xu=xr
        else:
          xl=xr
      
      if iterator==1:
        
        print("relative approxmate error is: ",e_a)
        pass
      
      else:
        e_a=abs((float(xr-xr_old)/float(xr)))*100
        print("relative approxmate error is: ",e_a)

      xr_old=xr
      iterator+=1
    else:
      print("No Root: ")
      flag=False
      break
  if flag==True:
    return xr

#(math.e**x)+(2**-x)+2*math.cos(x)-6

#@title FixedPoint Method
# def FixedPoint()

# x2-2x-3=0

# +x fel n7yteeen!!

#@title Newton Method
from sympy import * 
def Newton(x0,epislon,iterations,equation):
    x, y = symbols('x y')
    iterator=1
    e_a=10000.0
    differn = Derivative(equation, x)
    differ_evaluate=str(differn.doit())
    while e_a>epislon and  iterator<iterations:
      print("iteration number: ",iterator)
      print("xold is: ",x0)
      xnew=x0-function(x0,equation)/function(x0,differ_evaluate)
      print("x new  is: ",xnew)
      e_a=abs((xnew-x0)/xnew)*100
      print("error is: ",e_a)

      if(e_a==0):
        return xnew

      x0=xnew
      iterator+=1
    return xnew

#@title Secant Method
def secant(x0,x1,epislon,iterations,equation):
    iterator=1
    e_a=10000.0
    while e_a>epislon and  iterator<iterations:
      print("iteration number: ",iterator)
      print("xi-1 is: ",x0)
      print("xi is: ",x1)
      print("function of xi-1 is: ",function(x0,equation))
      print("function of xi is: ",function(x1,equation))

      # xnew=(x0*function(x1,equation)-x1*function(x0,equation))/function(x1,equation)-function(x0,equation)
      xnew=x1-(function(x1,equation)*(x1-x0)/(function(x1,equation)-function(x0,equation)))
      print("x new  is: ",xnew)
      e_a=abs((xnew-x1)/xnew)*100
      print("error is: ",e_a)

      if(e_a==0):
        return xnew

      x0=x1
      x1=xnew
      iterator+=1
    return xnew

#@title Modified Secant
#@title Secant Method
def modifiedSecant(x0,percentage,epislon,iterations,equation):
    p=percentage/100
    iterator=1
    e_a=10000.0
    while e_a>epislon and  iterator<iterations:
      print("iteration number: ",iterator)
      print("xi is: ",x0)
      print("function of xi is: ",function(x0,equation))

      xnew=x0-(function(x0,equation)*(p*x0)/(function(x0+p*x0,equation)-function(x0,equation)))
      print("x new  is: ",xnew)
      e_a=abs((xnew-x0)/xnew)*100
      print("error is: ",e_a)

      if(e_a==0):
        return xnew

      x0=xnew
      iterator+=1
    return xnew

#@title Equation Translator
def translator(equation):
  
  flag=False
  counter=0
  translated_equation=""
  i=0

#Handle 1/9  and 7^1/3 for example cases
  if equation[0].isdigit() and equation[1]=='^':
    translated_equation=f'x**{equation[4:]}-{equation[0]}'
    flag=True
  elif equation[0].isdigit()and equation[1]=='/' and 0<=int(equation[2:])<=9:
    translated_equation=f'x-{equation}'
    flag=True



  if flag==False:
    while(i!=length):
      #Handle Spaces
      if equation[i]==' ':
        counter=1
        pass
      #sin and cos First case : sin x -> sin(    Second case : 2sin x -> 2*sin(
      elif (equation[i:i+3]=='sin')or (equation[i:i+3]=='cos'):
        if i==0:
          counter=3
          translated_equation+=f'math.{equation[i:i+3]}('
        elif equation[i-1].isdigit():
          counter=3
          translated_equation+=f'*math.{equation[i:i+3]}('


        

      #exponential
      elif equation[i]=='e':
        if i==0:
          translated_equation+=f'math.e'
          counter=1
        elif equation[i-1].isdigit():
          translated_equation+=f'*math.e'
          counter=1
        else:
          translated_equation+=f'math.e'
          counter=1

          
      #Power
      elif equation[i]=='^':
        translated_equation+='**'
        counter=1


      # First case: sin x then == sin(x)   Second case  sin2x == sin(2*x)    
      elif len(translated_equation)>0 and (equation[i-4:i-1]=="sin" or equation[i-4:i-1]=="cos"):
        if translated_equation[-1]=='(' and equation[i]=='x':
          translated_equation+=f'{equation[i]})'
          counter=1
        if translated_equation[-1]=='(' and equation[i]!='x':
          translated_equation+=f'{equation[i]}*{equation[i+1]})'
          counter=2
      
      #Polynomial
      elif equation[i]=='x':
        if i==0:
          translated_equation+='x'
          counter=1
        elif equation[i-1].isdigit():
          translated_equation+='*x'
          counter=1
        else:
          translated_equation+='x'
          counter=1

      else:
        translated_equation+=equation[i]
        counter=1

      i+=counter
    return translated_equation

#@title Main Function

print(" Welcome to Root Finder  ")
method=int(input("Please Choose Method to find root with : 1- Bisection 2-False Position 3-Fixed Point 4-Newton 5-Secant 6-Modified Secant: "))
equation = input("Enter your equation: ")
length=len(equation)
iterations=int(input("Enter Number of Iterations: "))
epislon=float(input("Enter Epislon: "))

equation=translator(equation)
if method ==1:  
  xl=float(input("Enter X Lower: "))
  xu=float(input("Enter X Upper: "))
  root=bisection(xl,xu,epislon,iterations,equation)
elif method ==2:
  xl=float(input("Enter X Lower: "))
  xu=float(input("Enter X Upper: "))
  root=FalsePosition(xl,xu,epislon,iterations,equation)

elif method ==3:
  pass

elif method ==4:
  x0=float(input("Enter X0: "))
  root=Newton(x0,epislon,iterations,equation)

elif method ==5:
  x0=float(input("Enter Xi-1: "))
  x1=float(input("Enter Xi: "))
  root=secant(x0,x1,epislon,iterations,equation)
elif method==6:
  x0=float(input("Enter X0: "))
  percentage=float(input("Enter Percentage"))
  root=modifiedSecant(x0,percentage,epislon,iterations,equation)

print(root)

####### Samples  #################

#x**3-0.165*x**2+3.993*10**-4 ->> Newton(10,0,0.05)
#y=3*x**2-math.e**x ->> Bisection(10,3,0.5,1)
# math.e**x+2**-x+2*math.cos(x)-6 ->> False Postion (10,0.1,1,2)
# x**2-2 ->> Secant(10,5,0.5,1)
#7^1/3 ->>Newton(10,0,2)
# 1/9 ->>Newton(10,0,0.1)
#math.e**-x-x ->>ModifiedSecant(10,1,1,1)