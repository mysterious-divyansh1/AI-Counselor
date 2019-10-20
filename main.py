import pandas as pd
import numpy as np 
import kai_text_classifier

data = pd.DataFrame(pd.read_csv('Questions_data.csv'))

Child_name = input('Enter your name: ')
print("Welcome to the KAI ",Child_name)

print("We are here to ask you some questions kindly be attentive")
child_data = data[data['Type']=='C']
print(child_data)
total_score = 0
for i in range(5,len(child_data)+5):
    print('Select one of the options: ')
    print('(1) Not at all (2) Almost Never (3) Sometimes (4) Most of the times')
    answer = input(child_data['Questions'].loc[i])
    answer = int(answer,10)
    total_score = total_score + answer
