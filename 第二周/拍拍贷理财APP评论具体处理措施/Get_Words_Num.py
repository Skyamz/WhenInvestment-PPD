# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 00:44:17 2017

@author: skyamz
"""

word_lst = []  
word_dict= {}  
with open('Sentence.txt') as wf,open("word.txt",'w') as wf2: 
  
    for word in wf:  
        word_lst.append(word.split(' '))   
        for item in word_lst:  
             for item2 in item:  
                if item2 not in word_dict: 
                    word_dict[item2] = 1  
                else:  
                    word_dict[item2] += 1  
                    
    word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    for key, counts in word_dict:  
        if counts>0:
           print key,counts  
           wf2.write(key+' '+str(counts)+'\n')  
    