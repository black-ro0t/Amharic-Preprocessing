# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 07:50:59 2021

@author: Kidus
"""

# import pandas as pd
import re
from symspellpy import SymSpell


ex_punctuation = "@#$^&*;<>|ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnopqrstuvwxyz" #used for removing these punctuations
numbers = "0123456789"
path = "//home/black/Documents/project/amh.txt"
dctpath = "/home/black/Documents/project/dictionary.txt"
dictionary = open(dctpath
,'r',encoding='utf-8').read()
list_dictionary = dictionary.split()
spellcheck = SymSpell(max_dictionary_edit_distance=2,prefix_length=7)

    

    
def file_read(mode):
    file = open(path,mode,encoding='utf-8')
    return file    

def read_content(file):
    content = file.read()
    lists = content.split()
    return lists
    
def remove_extra_spaces(inputs): # removes extra spaces
    
    inputs = inputs.split()
    print(inputs)
    clearwords = ' '.join(inputs)
    return clearwords
   


def remove_unnecessary_punctuation(inputs):
    inputs = inputs.split()
    clearedwords=[]
    temp=""
    for word in inputs:
        for elt in word:
            if elt not in ex_punctuation:
                temp = temp + elt
        
        clearedwords.append(temp)
        temp=""
    
    return ' '.join(clearedwords)
    # file.close()
    # filewrite = open(path,'w',encoding='utf-8')
    # filewrite.truncate()
    # filewrite.write(clearedwords)
    # filewrite.close()
    
def split_number_from_string(inputs):
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
            else: temp+=elt
            pr=elt
        templist.append(temp)
        final_string = ' '.join(templist)
    return final_string


def find_merged_words(inputs):
    # inputs = file.read()
    inputs = inputs.split()
    # print(inputs)

    line = dictionary.split()
    templist=[]
    # print(inputs)
    
    for word in inputs:
        flag = False
        if not(word in line):
            for char in word:
                if char in "<>?\'\\!@#$%^&*()}{][/;'\":.,=-+_|፤፣፧፦፡፥.,።":
                    flag= True
            
            if not flag:
                splited= split_merged_words(word, line)
                print(splited)
                flag=False
                templist.extend(splited)
            else:
                 templist.append(word)
        else:
            templist.append(word)
    # print(templist)

    return templist     
    

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
    if wordparts[0] == wordparts[len(wordparts)-1]:
        wordparts = wordparts[:1]


    return wordparts


                
        

def spell_correction(inputs):
    
    inputs = inputs.split()
    line = dictionary.split()
    print(len(inputs))
    templist=[]
    # spellcheck = SymSpell(max_dictionary_edit_distance=2,prefix_length=7)
    # spellcheck.load_dictionary(dctpath,term_index=0,count_index=1)

    for word in inputs: 
       
        if word in line:  

            templist.append(word)
        else:      
            print(word)
   
            suggest = spellcheck.lookup(word,verbosity=2,max_edit_distance=2)
            templist.append(suggest[0]._term)
            
    templist=' '.join(templist)
    return templist

        



def split_punctuatioin_string(inputs):  #separating punctuations and nominals
    inputs = inputs.split()
    punctuation_open = "({[<"
    punctuation_close = ")}]>"
    splitpunctuation="፤፣፧፦፡፥/.,"
    qout = "\"\' ” "
    openqout = False
    templist = []
    temp = ""
    for word in inputs:
        if word in list_dictionary:
            templist.append(word)
        else:
            for char in word:
                if char in punctuation_open:
                    temp+=" "+char
                    print(char)
                elif char in punctuation_close:
                    if word[word.index(char)-1] in punctuation_close:
                        print(word[word.index(char)-1],",",word[word.index(char)])

                        temp+=char
                    else:
                        temp+=char+" "
                elif char in splitpunctuation:
                    # print(word[word.index(char)-1],word[word.index(char)+1],word[word.index(char)+2])
                    longindex = len(word)-1
                    if((word.index(char)+1 < len(word) and word[word.index(char)+1].isnumeric()) or (word.index(char)+2 <= longindex and  word[word.index(char)+2] in splitpunctuation) or word.index(char)+2 == len(word)):
                        temp+=char
                    else:
                        temp+=char+" "
                elif char in qout:
                    if openqout:
                        temp+=char+" "
                        openqout=False
                    else:
                        temp+=" "+char
                        openqout=True

                else:
                    temp+=char
            templist.append(temp)
            temp=""
    templist = ' '.join(templist)
    return templist


def split_sentence(input):
    data = input.split()
    print(data)
    flag = False
    temp=''
    for elt in data:
        for spell in elt:
            if spell=='።':
                flag= True
                break
        
        if(flag == True):
            temp+=' ' +elt
            temp+='\n'
            flag=False 
        else:
            temp+=' '+elt
    return temp

   

def split_sub_sentences(input):
    
    data = input.split()
    # input= ' '.join(data)
    final=''
    x=re.findall(r" [ሀ-ፐ|\d][/.)] ",input)
    print(len(x))
    if len(x)>0:
        for elt in data:
            for part in x:
                elt=elt.strip()
                if elt in part:
                    final+='\n'
                    final+=elt+" "
                    break
                elif part==x[len(x)-1]:
                    final+=elt+" "
        print(final)
        # final+=input[(input.index(x[len(x)-1]))+3:]
        # print(final)
           
    else:
        final = ' '.join(data)
    
    return final


def changequotes(input):
    prequots = "  ‘ ’ “ ” ‹ › « »"
    data = input.split()
    temp=""
    finalword=[]
    openq=True
    
    for elt in data:
        print(elt)
        for x in elt:
            if x in prequots:
                x = "\""
                if openq:
                    temp+=x
                    openq=False
                else:
                    temp+=x
            else:
                temp+=x
        finalword.append(temp)
        temp=""


    return ' '.join(finalword)
        








    






            


    
