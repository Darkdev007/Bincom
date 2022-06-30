# to read the html page
import pandas as pd
url = 'http://127.0.0.1:5500/index.html' #hosted from my pc, url might differ from yours
df = pd.read_html(url)

# to append all colours to a list
df = df[0]
# print(df.values.tolist())
color = []

for i in range(len(df)):
    color.extend((df.loc[i,'COLOURS'].split(',')))

print(color)

#find frequency of all the colors
from collections import Counter
counts = Counter(color)
print(counts.most_common)



# Mean of colour to find was not given

# Blue is worn mostly thoughout the week
print(counts.most_common(1))

#median = orange
print((len(color))/2) #th value

# variance 
import numpy as np
# print(np.var(color))


# Probabilty of red
no_of_red = counts[' RED']
total = len(color)
prob_of_red = no_of_red/total
print(prob_of_red)


#recurssion
numbers = [1,2,3,4,5,6,7,8,9]
def find_number(l):
    if l in numbers:
        print (f'Your search {l} exists in the list of numbers')
    else:
        print (f'Your search {l} does not exist')
value = int(input('Enter your value :  \n'))
find_number(value)



#import random to select betwen 0 and 1 
import random
numbers = ['0','1']
digit = ''

#loop 4 times and concatenate
for i in range(0,4):
    digit += random.choice(numbers)
print(f'{digit} has been generated')
#convert to base 10
answer = int(digit, base = 2)
print(f'{digit} to base 10 is {answer}')
    

#fibonnaci
first = 0
second = 1
for i in range(50):
    temp = first
    first = second
    second = temp + second

print(f'{second} is the sum of the first 50 fibonnaci series' )