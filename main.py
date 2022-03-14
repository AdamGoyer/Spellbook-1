print('Hello, Practice Spellbook!')
#import this
#import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib inline
#pd.__version__ # Version Check doesn't seem to be working in replet...
#import random
# import matplotlib.pyplot as plt

#print('I cast 100 Magic Missiles into the Darkness!')
#"""Roll a D20 100 times"""
#for i in range(3):
#  print(random.randint(1,20),end=' ')

print('---')

def test(x,y,a,b): 
  if x == y and a == b:
    print('True is aaaa')
  else:
    print('False is xyab')
  
x = 'a'
y = 'a'
a = 'a'
b = 'a'

(test(x,y,a,b))



def number_tracks(day,city):
    track_list = df[df['day'] == day]
    track_list = track_list[track_list['city'] == city]
    return(track_list)
    track_list_count = track_list['user_id'].count()
    return(track_list_count)
    print(track_list_count)