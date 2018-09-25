
"""
#1
celsius = eval(raw_input('>>'))
fahrenheit = (9.0 / 5.0) * celsius + 32
print(fahrenheit)

#2
radius,length = eval(raw_input('>>'))
area = radius * radius * 3.1415926
volume = area * length
print(area,volume)

#3
feet = eval(raw_input('>>'))
meters = feet * 0.305
print(meters)

#4
M,initialTemperature,finalTemperature = eval(raw_input('>>'))
Q = M * (finalTemperature - initialTemperature) * 4148
print(Q)

#5
balance,interest1rate = eval(raw_input('>>'))
interest = balance * (interest1rate / 1200)
print(interest)

#6
v0,v1,t = eval(raw_input('>>'))
a = (v1 - v0) / t
print(a)


#7
a=float(raw_input('>>'))
a1=a*(1+0.00417)
a2=(a+a1)*(1+0.00417)
a3=(a+a2)*(1+0.00417)
a4=(a+a3)*(1+0.00417)
a5=(a+a4)*(1+0.00417)
a6=(a+a5)*(1+0.00417)
print(a6)"""

#8
number=eval(raw_input('>>'))
a=number%10
b=number//100
c=(number%100)//10
digits=a+b+c
print(digits)
