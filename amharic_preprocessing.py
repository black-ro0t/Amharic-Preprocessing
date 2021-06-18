# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 07:50:59 2021

@author: Kidus
"""

# import pandas as pd
import nltk 
import re
from symspellpy import SymSpell, Verbosity
from itertools import islice

ex_punctuation = "@#$^&*;<>|" #used for removing these punctuations
numbers = "0123456789"
path = "//home/black/Documents/project/amh.txt"
dctpath = "/home/black/Documents/project/dictionary.txt"
dictionary = open(dctpath
,'r',encoding='utf-8').read()
    

    
def file_read(mode):
    file = open(path,mode,encoding='utf-8')
    return file    

    
def remove_extra_spaces(file): # removes extra spaces
    inputs = file.read()
    print(inputs)
    file.close()
    inputs = inputs.split()
    print(inputs)
    # filewrite = open(path,'w',encoding='utf-8')
    # filewrite.truncate()
    clearwords = ' '.join(inputs)
    print(clearwords)
    # filewrite.write(clearwords)   
    # filewrite.close()


def remove_unnecessary_characters(file):
    inputs = file.read()
    print(inputs)
    inputs = inputs.split()
    clearedwords=""
    temp=""
    for word in inputs:
        for elt in word:
            if elt not in ex_punctuation:
                temp = temp + elt
        
        clearedwords += temp + " "
        temp=""
        
    print(clearedwords)
    # file.close()
    # filewrite = open(path,'w',encoding='utf-8')
    # filewrite.truncate()
    # filewrite.write(clearedwords)
    # filewrite.close()
    
def split_number_from_string(file):
    inputs = file.read()
    inputs = inputs.split()
    templist=[]
   
    for word in inputs:
        pr = word[0]
        temp=""
        for elt in word:
            if elt.isnumeric() and pr.isnumeric():
                temp+=elt
            elif elt.isalpha() and pr.isnumeric():
                templist.append(temp)
                temp=elt
            elif elt.isalpha() and pr.isalpha():
                temp+=elt
            elif elt.isnumeric() and pr.isalpha():
                templist.append(temp)
                temp=elt
            pr=elt
        templist.append(temp)
        final_string = ' '.join(templist)
    print(final_string)


def find_merged_words(file):
    inputs = file.read()
    inputs = inputs.split()
    # print(inputs)
    line = dictionary.split()
    templist=[]
    print(inputs)
    
    for word in inputs:
        if not(word in line):
            splited=split_merged_words(word, line)
            templist.extend(splited)
        else:
            templist.append(word)

    print(templist)        
    

def split_merged_words(word,line):
    flag= True
    wordparts=[]
    temp=""
    remind=word
    for i in word:
        for char in remind:
            temp+=char
            if temp in line:
                front=temp
                remind= word[word.index(char)+1:]
                word=remind
                if remind in line:
                    flag=False
                    break
        wordparts.append(front)
        temp=""
        if not flag:
            flag=True
            wordparts.append(remind)
            break
    return wordparts
                
        

def spell_correction(file):
    inputs = file.read()
    inputs = inputs.split()
    line = dictionary.split()
    print(len(line))
    templist=[]
    spellcheck = SymSpell(max_dictionary_edit_distance=2,prefix_length=7)
    spellcheck.load_dictionary(dctpath,term_index=0,count_index=1)
    print(list(islice(spellcheck.words.items(),5)))

    for word in inputs: 
       
        if word in line:  

            templist.append(word)
        else:      
            print(word)
   
            suggest = spellcheck.lookup(word,verbosity=2,max_edit_distance=2)
            templist.append(suggest[0]._term)
            
    print(' '.join(templist))
        



    
if __name__ == '__main__':
    file= file_read('r')
    spell_correction(file)
    
    
    

    
    
