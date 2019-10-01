# the equation for turning degrees Celcius into Fahrenheit is
# F = (C-32) * (5/9)
#this function completes the first step in the equation
#the second part will be done manually and written in the comments

def celtofah(sequence):
    result = []
    for element in sequence:
        result = result + [(element - 32) * 5]
    return result

#the following list will be inputted to the function
celtofah([9,27,56,81])
#divide each answer by 9, which will equal to 12.8, 2.8, 27.2 degrees Fahrenheit

#the following variable will be inputted to the function
x = [0,32,100,212]
celtofah (x)
#divide each answer by 9, which will equal to 17.8, 0, 37.8, 100 degrees Fahrenheit

#the following variable will return its value
y = celtofah(x)
print y
