import os
import random


"""creating the random quiz generator for the geography teacher"""
capital = {
'Andhra Pradesh':'Hyderabad'
'Arunachal Pradesh': 'Itanagar'
'Assam':'Dispur'
'Bihar':'Patna'
'Chattisharh':'Raipur'
'Goa':'Panaji'
'Gujurat':'Gandhinagar'
'Haryana':'Chandigarh'
'Punjab':'Chandigarh'
'Himachal Pradesh':'Shimla'
'Jammu and Kashmir':'Srinagar'
'Jharkhand':'Ranchi'
'Karnataka':'Bengaluru'
'Kerala':'Thiruvananthapuram'
'Madhya Pradesh':'Bhopal'
'Maharashtra':'Mumbai'
'Manipur':'Imphal'
'Meghalaya':'Shillong'
'Mizoram':'Aizawl'
'Nagaland':'Kohima'
'Odisha':'Bhubaneswar'
'Rajasthan':'Jaipur'
'Sikkim':'Gangtok'
"Tamil Nadu":'Chennai'
'Telangana':'Hyderabad'
'Tripura':'Agartala'
'Uttar Pradesh':'Lucknow'
'Uttarakhand':'Dehradun'
'West Bengal':'Kolkata'
    }



for quizNum in range(15):
    quizfiles = open('home/rishi/Documents/pyatbs/capitalquiz%s.txt'%(quizNum+1),'w')
    answerfile = open('home/rishi/Documents/pyatbs/heel/capitalsquiz_ans%s'%(quizNum+1),'w')
    quizfiles.write('Name : \n\nDate: \n\nPeriod\n\n')
    quizfiles.write((' '*20)+'States Capital Quiz (Form #%s)'%s(quizNum + 1))
    quizfiles.write('\n\n')


    #shuffle the order of the states.
    states = list(capital.keys())
    random.shuffle(states)


    for questionNum in range(29):
        correctans = capital(states[questionNum])
        wrongans = list(capital.values())
        

    



    
