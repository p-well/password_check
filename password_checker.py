from re import findall
import os


def load_blacklist():
    with open('blacklist.txt', mode='r', encoding='utf-8') as blacklist_data:
        return blacklist_data.read().split('\n')


def store_regexs_for_checks():
    regexs = [
              r'\S{8,}', # lenght check - at least 8 symbols
              r'\S{10,}', # lenght check - at least 10 symbols
              r'\S{12,}', # lenght check - at least 12 symbols
              r'[a-z]', # contains lower case letters
              r'[A-Z]', # contains upper case letters
              r'[0-9]', # contains digits 
              r'[!, ?, @, #, $, %, &, *, _]' # contains any of listed special symbols
              ]
    return regexs


def rate_password_strength(user_password, regexs_list):
    rating = 0
    for template in regexs_list:
        if findall(template, user_password):
            rating += 1
    return rating

if __name__ == '__main__':
    #typed_password = input()
    #regexs_list = store_regexs_for_checks()
    #print(rate_password_strength(typed_password, regexs_list))
    print(load_blacklist())