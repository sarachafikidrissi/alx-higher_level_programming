#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000}
    my_list = list(roman_string.upper())
    result = 0
    prev = 0
    for letter in my_list:
        if letter in my_dict:
            result += my_dict[letter]
            if my_dict[letter] > prev:
                result -= prev *2
            prev = my_dict[letter]
        else:
            return (0)
    return (result)
