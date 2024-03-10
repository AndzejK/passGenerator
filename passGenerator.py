# 28-02-2024
import random
from tkinter import ttk
from tkinter import font
from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
abc_low='a b c d e f g h i j k l m n o p q r s t u v w x y z'.replace(' ','')
abc_upper=abc_low.upper()
digits='0123456789'
symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
all_available_characters=abc_upper+abc_low+digits+symbols # total 94 char
max_default_val=25
# we wanna have a function that will accepts the length, min and max, if not provided then we can have default values 
# plus user can define what strenght of all pass should be like not having digits, or only digits and letters
# def testDisplayPassCheckBoxex(*args):
#     print(checkUpcaseInt.get(),checkNumberInt.get(),checkSymbolInt.get())
#     print(lengthEntry.get())
    
def generate_random_pass(max=max_default_val,uppercase=0,numbers=1,symbol=0):
    try:
        uppercase=checkUpcaseInt.get()
        numbers=checkNumberInt.get()
        symbol=checkSymbolInt.get()
        max=lengthEntry.get()
        # max=lengthEntry.set(max)
       
        # get_random_char=random.choices(all_available_characters,k=int(max))
        # convert_get_random_char_to_string=''.join(get_random_char)
        if symbol and numbers and uppercase:
            # use default settings, all options are ON
            get_random_char=random.choices(all_available_characters,k=int(max))
            convert_get_random_char_to_string=''.join(get_random_char)
            print('The pass was generated using ALL options.')
            print(convert_get_random_char_to_string)
            msgDisplayGenPassInit.set(convert_get_random_char_to_string)
        else: 
            # when one or more options OFF 
            # Need to find out which exactly option is OFF
            user_adjusted_char_list=abc_low # enabling a default option
            if uppercase:
                user_adjusted_char_list+=abc_upper
                print("Uppercase option was enabled")
                if numbers:
                    user_adjusted_char_list+=digits
                    print("Numbers option was enabled")
                    if symbol:
                        user_adjusted_char_list+=symbols
                        print("Symbols option was enabled")
                        # Generate the user password
                        get_random_char=random.choices(user_adjusted_char_list,k=int(max))
                        convert_user_adjusted_char_list_to_string=''.join(get_random_char)
                        print(convert_user_adjusted_char_list_to_string)
                        msgDisplayGenPassInit.set(convert_user_adjusted_char_list_to_string)
                    else:
                        # Generate the user password
                        get_random_char=random.choices(user_adjusted_char_list,k=int(max))
                        convert_user_adjusted_char_list_to_string=''.join(get_random_char)
                        print(convert_user_adjusted_char_list_to_string)
                        msgDisplayGenPassInit.set(convert_user_adjusted_char_list_to_string)
                else:
                    if symbol:
                        user_adjusted_char_list+=symbols
                        print("Symbols option was enabled")
                        # Generate the user password
                        get_random_char=random.choices(user_adjusted_char_list,k=int(max))
                        convert_user_adjusted_char_list_to_string=''.join(get_random_char)
                        print(convert_user_adjusted_char_list_to_string)
                        msgDisplayGenPassInit.set(convert_user_adjusted_char_list_to_string)
                    else:
                        # Generate the password the Uppercase + default
                        get_random_char=random.choices(user_adjusted_char_list,k=int(max))
                        convert_user_adjusted_char_list_to_string=''.join(get_random_char)
                        print(convert_user_adjusted_char_list_to_string)
                        msgDisplayGenPassInit.set(convert_user_adjusted_char_list_to_string)
            else:
                if numbers:
                    user_adjusted_char_list+=digits
                    print("Numbers option was enabled")
                    if symbol:
                        user_adjusted_char_list+=symbols
                        print("Symbols option was enabled")
                         # Generate the user password
                        get_random_char=random.choices(user_adjusted_char_list,k=int(max))
                        convert_user_adjusted_char_list_to_string=''.join(get_random_char)
                        print(convert_user_adjusted_char_list_to_string)
                        msgDisplayGenPassInit.set(convert_user_adjusted_char_list_to_string)
                    else:
                        # Generate the user password
                        get_random_char=random.choices(user_adjusted_char_list,k=int(max))
                        convert_user_adjusted_char_list_to_string=''.join(get_random_char)
                        print(convert_user_adjusted_char_list_to_string)
                        msgDisplayGenPassInit.set(convert_user_adjusted_char_list_to_string)
                else:
                    if symbol:
                        user_adjusted_char_list+=symbols
                        print("Symbols option was enabled")   
                        # Generate the user password
                        get_random_char=random.choices(user_adjusted_char_list,k=int(max))
                        convert_user_adjusted_char_list_to_string=''.join(get_random_char)
                        print(convert_user_adjusted_char_list_to_string)
                        msgDisplayGenPassInit.set(convert_user_adjusted_char_list_to_string)
                    else:
                        # Generate the user password (only having a default option)
                        get_random_char=random.choices(user_adjusted_char_list,k=int(max))
                        convert_user_adjusted_char_list_to_string=''.join(get_random_char)
                        print(convert_user_adjusted_char_list_to_string)
                        msgDisplayGenPassInit.set(convert_user_adjusted_char_list_to_string)
    
    except:
        print(f'Please enter the integers for "Max value", it was entered: {max}!')
# generate_random_pass(max='20x',uppercase=1,numbers=1,symbol=0)

# Setting up the window / root
mainWindow=Tk()
mainWindow.title("Password Generator")

# Variables related to the  GUI
msgLength='Enter length of password: '
msgAvailOptio='Available Options'
msgStatingPass='A new generated password:'
msgError='Wrong value was entered!'
# Display password, initial settings
msgDisplayGenPassInit=StringVar()
msgDefaultDisplayGenPass='<generated user password>'
# Set default value
msgDisplayGenPassInit.set(msgDefaultDisplayGenPass)
# msgDisplayGenPass=msgDisplayGenPassInit.get()


current_year=str(datetime.now().year)
msgAppCreated='Created by Krupoves ' + current_year

# Functions
def validate_length(new_val):
    return new_val.isdigit() and len(new_val)<=2

# def enter(e):
#     lengthEntry.get()
#     testDisplayPassCheckBoxex()

# Setting the container where all my content will be kept/glued togerther / content frame
mainFrame=ttk.Frame(mainWindow,padding="3 3 12 12")

# put content into the main frame
checkBoxFrame=ttk.Frame()
mainWindow.columnconfigure(0, weight=1) # tells Tk that the frame should expand to fill any extra space if the window is resized.
mainWindow.rowconfigure(0, weight=1) # # tells Tk that the frame should expand to fill any extra space if the window is resized.

# No more than two "characters"
validate_length_entry=mainWindow.register(validate_length)

# Widgets:
# (row,column)
# 1) Logo (1,1) 2) entry widget, Length (1,2), 3) Select options (1,3)

logoUpload=ImageTk.PhotoImage(Image.open("./logoPassGenRound.png"))

# Styles
label_font_bold=font.Font(weight="bold")
label_font_italic=font.Font(slant="italic")
# Labels
logoLabel=ttk.Label(mainFrame,image=logoUpload,padding=(10,5,50,0))
lengthLabel=ttk.Label(mainFrame,text=msgLength)
availableOptions=ttk.Label(mainFrame,text=msgAvailOptio,padding=(25,0,25,0),compound='top',font=label_font_bold,anchor='w') #50,5,0,10
staticLabelStatingPass=ttk.Label(mainFrame,text=msgStatingPass)

# displayLabelUserGenPass=ttk.Label(mainFrame,textvariable=msgDisplayGenPassInit,font=label_font_italic,borderwidth=1,relief="sunken")
createdLabel=ttk.Label(mainFrame,text=msgAppCreated,padding=(0,50,0,0))


# Entry Widgets
lengthEntry=StringVar()
lengthEntry.set(max_default_val)
length=ttk.Entry(mainFrame,width=2,validate='key',validatecommand=(validate_length_entry,"%P"),textvariable=lengthEntry)
length.focus()
displayEntryUserGenPass=ttk.Entry(mainFrame,textvariable=msgDisplayGenPassInit,state='readonly') # font=label_font_italic
# setLength=lengthEntry.set(6)
# getLength=lengthEntry.get()


# Checkboxes
checkUpcaseInt=IntVar()
checkNumberInt=IntVar()
checkSymbolInt=IntVar()

chUpc=Checkbutton(mainFrame,text="Uppercase letters",variable=checkUpcaseInt,onvalue=1,offvalue=0, anchor=W) # justify="right"
chNum=Checkbutton(mainFrame,text="Numbers",variable=checkNumberInt,onvalue=1,offvalue=0,anchor=W)
chSym=Checkbutton(mainFrame,text="Symbols",variable=checkSymbolInt,onvalue=1,offvalue=0,anchor=W)


# 4) displays the pass (2,2), where are 2 lables, L1 -> pass was generared and L2 -> something wrong
# 5) Button to generate a pass (2,3), the last label, L3 -> info, who, and current year, created
btnGenerate=ttk.Button(mainFrame,text="Generate",padding=25,command=generate_random_pass) # testDisplayPassCheckBoxex, generate_random_pass
mainWindow.bind('<Return>', generate_random_pass)

# Griding / Positioning of the Widgets
mainFrame.grid(column=0, row=0 ) #sticky=(N, W, E, S)
logoLabel.grid(row=0,column=0,rowspan=4,sticky="W")
lengthLabel.grid(row=0,column=1)
length.grid(row=0,column=2)
availableOptions.grid(row=0,column=3,sticky=W)
chUpc.grid(row=1,column=3,sticky='w',padx=25)
chNum.grid(row=2,column=3,sticky='w',padx=25)
chSym.grid(row=3,column=3,sticky='w',padx=25) #padding=(25,0,25,0)
btnGenerate.grid(column=3,row=4,rowspan=4)
staticLabelStatingPass.grid(column=1,row=3,columnspan=2)
# Display user password
displayEntryUserGenPass.grid(column=1,row=4,columnspan=2)
createdLabel.grid(column=1,row=5,rowspan=3)



# launch the app
mainWindow.mainloop()
