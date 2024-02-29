# 28-02-2024
import tkinter,random

abc_low='a b c d e f g h i j k l m n o p q r s t u v w x y z'.replace(' ','')
abc_upper=abc_low.upper()
digits='0123456789'
punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
all_available_characters=abc_upper+abc_low+digits+punctuations # total 94 char

# we wanna have a function that will accepts the length, min and max, if not provided then we can have default values 
# plus user can define what strenght of all pass should be like not having digits, or only digits and letters

def generate_random_pass(max=55,lowercase=True,uppercase=True,numbers=True,symbols=True):
    try:
        get_55_random_char=random.choices(all_available_characters,k=int(max))
        convert_get_55_random_char_to_string=''.join(get_55_random_char)
        print(convert_get_55_random_char_to_string)
    except:
        print(f'Please enter the integers for "Max value", it was entered: {max}!')

