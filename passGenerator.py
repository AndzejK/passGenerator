# 28-02-2024
import tkinter,random

abc_low='a b c d e f g h i j k l m n o p q r s t u v w x y z'.replace(' ','')
abc_upper=abc_low.upper()
digits='0123456789'
symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
all_available_characters=abc_upper+abc_low+digits+symbols # total 94 char

# we wanna have a function that will accepts the length, min and max, if not provided then we can have default values 
# plus user can define what strenght of all pass should be like not having digits, or only digits and letters

def generate_random_pass(max=55,uppercase=1,numbers=1,symbol=1):
    try:
        # get_random_char=random.choices(all_available_characters,k=int(max))
        # convert_get_random_char_to_string=''.join(get_random_char)
        if symbol and numbers and uppercase:
            # use default settings, all options are ON
            get_random_char=random.choices(all_available_characters,k=int(max))
            convert_get_random_char_to_string=''.join(get_random_char)
            print('The pass was generated using ALL options.')
            print(convert_get_random_char_to_string)
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
                    else:
                        # Generate the user password
                        get_random_char=random.choices(user_adjusted_char_list,k=int(max))
                        convert_user_adjusted_char_list_to_string=''.join(get_random_char)
                        print(convert_user_adjusted_char_list_to_string)
                else:
                    if symbol:
                        user_adjusted_char_list+=symbols
                        print("Symbols option was enabled")
                        # Generate the user password
                        get_random_char=random.choices(user_adjusted_char_list,k=int(max))
                        convert_user_adjusted_char_list_to_string=''.join(get_random_char)
                        print(convert_user_adjusted_char_list_to_string)
                    else:
                        # Generate the password the Uppercase + default
                        get_random_char=random.choices(user_adjusted_char_list,k=int(max))
                        convert_user_adjusted_char_list_to_string=''.join(get_random_char)
                        print(convert_user_adjusted_char_list_to_string)
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
                    else:
                        # Generate the user password
                        get_random_char=random.choices(user_adjusted_char_list,k=int(max))
                        convert_user_adjusted_char_list_to_string=''.join(get_random_char)
                        print(convert_user_adjusted_char_list_to_string)
                else:
                    if symbol:
                        user_adjusted_char_list+=symbols
                        print("Symbols option was enabled")   
                        # Generate the user password
                        get_random_char=random.choices(user_adjusted_char_list,k=int(max))
                        convert_user_adjusted_char_list_to_string=''.join(get_random_char)
                        print(convert_user_adjusted_char_list_to_string)
                    else:
                        # Generate the user password (only having a default option)
                        get_random_char=random.choices(user_adjusted_char_list,k=int(max))
                        convert_user_adjusted_char_list_to_string=''.join(get_random_char)
                        print(convert_user_adjusted_char_list_to_string)
    
    except:
        print(f'Please enter the integers for "Max value", it was entered: {max}!')
generate_random_pass(max='20x',uppercase=1,numbers=1,symbol=0)
