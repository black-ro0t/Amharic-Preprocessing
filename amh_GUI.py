from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
import amharic_preprocessing as ap

def clicked():
    strs=inputtxt.get('1.0','end-1c')
    if state1.get():
        strs = ap.split_number_from_string(strs)
        strs = ap.split_punctuatioin_string(strs)

    if state2.get():

        strs = ap.find_merged_words(strs)
    if state3.get():
        strs = ap.spell_correction(strs)

    if state4.get():
        strs = ap.remove_unnecessary_punctuation(strs)
        strs = ap.changequotes(strs)

    if state5.get():
        strs = ap.remove_extra_spaces(strs)
    
    if state6.get():  
        strs = ap.split_sentence(strs)

    if state7.get():  
        strs = ap.split_sub_sentences(strs)

    outputtxt.delete('1.0','end-1c')
    outputtxt.insert('end-1c', strs)
       

if __name__ == "__main__":
    print("loading dictionary....")
    ap.spellcheck.load_dictionary(ap.dctpath,term_index=0,count_index=1)
    print("....dictionary loaded....")


    window = Tk()
    
    window.title("Amharic Pre-processing")
    lb1 = Label(window,text="Input")
    lb1.pack()
    inputtxt = scrolledtext.ScrolledText(window,width=60,height=10)
    inputtxt.pack()
    lb2 = Label(window,text="Output")
    lb2.pack()
    outputtxt = scrolledtext.ScrolledText(window,width=60,height=10)
    outputtxt.edit("modified")
    outputtxt.pack()
    
    state1 = BooleanVar()
    state2 = BooleanVar()
    state3 = BooleanVar()
    state4 = BooleanVar()
    state5 = BooleanVar()
    state6 = BooleanVar()
    state7 = BooleanVar()


    state1.set(False)
    state2.set(False)
    state3.set(False)
    state4.set(False)
    state5.set(False)
    state6.set(False)
    state7.set(False)

    check1 = Checkbutton(window,text='split word from number and punctuations',var=state1)
    check2 = Checkbutton(window,text='split merged words',var=state2)
    check3 = Checkbutton(window,text='spell correction',var=state3)
    check4 = Checkbutton(window,text='remove uncessary punctuations and change quotes',var=state4)
    check5 = Checkbutton(window,text='remove extra spaces',var=state5)
    check6 = Checkbutton(window,text='split sub sentences',var=state6)
    check7 = Checkbutton(window,text='split sub list',var=state7)

    check1.pack(fill=X)
    check2.pack(fill=X)
    check3.pack(fill=X)
    check4.pack(fill=X)
    check5.pack(fill=X)
    check6.pack(fill=X)
    check7.pack(fill=X)

    btn = Button(window, text="    Process   ", command=clicked)
    btn.pack()

    



    window.mainloop()