import argparse

import requests
import getpass

from os.path import exists
from re import findall


def create_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--userlist')
    return parser


def check_args(parser, args):
    if args.userlist is not None and not exists(args.userlist):
        parser.error('File not found.')


def fetch_web_blacklist(url):
    try:
        web_blacklist = requests.get(url).text.split('\n')
    except ConnectionError:
         web_blacklist = []
    finally:
        return web_blacklist


def load_user_blacklist(filepath):
    with open(filepath, mode='r', encoding='utf-8') as blacklist_data:
        return blacklist_data.read().split('\n')


def is_password_in_blacklist(password, blacklist):
    return password in blacklist


def store_regex():
    regexs = [
              r'\S{8,}',  # Lenght check - at least 8 symbols
              r'\S{10,}',  # Lenght check - at least 10 symbols
              r'\S{12,}',  # Lenght check - at least 12 symbols
              r'[a-z]',  # Contains lower case letters
              r'[A-Z]',  # Contains upper case letters
              r'[0-9]',  # Contains digits 
              r'[!,?,@,#,$,%,^,&,*,-,_]',  # Contains any of listed special symbols
              r'^(?!\S*(\S)\1{2,})',  # Doesn't contain symbols repeated more than 2 times in succession
              r'^(?!([8-9]{1}[0-9]{9}))',  #Doesn't contain phone number
              r'^(?!.*(1|2)(\d)(\d)(\d)).*'  #Doesn't contain a
              ]
    return regexs


def rate_password_strength(user_password, regexs_list):
    rating = 0
    for template in regexs_list:
        if findall(template, user_password):
            print(template)
            rating += 1
    return rating


if __name__ == '__main__':
    URL = "https://raw.githubusercontent.com/skyzyx/bad-passwords/master/raw-mutated.txt"
    parser = create_args_parser()
    args = parser.parse_args()
    check_args(parser, args)
    user_password = getpass.getpass('\nType password:')
    print(user_password)
    if args.userlist is None:
        blacklist = fetch_web_blacklist(URL)
    else:
        blacklist = load_user_blacklist(args.userlist)
    if is_password_in_blacklist(user_password, blacklist):
         print('\nExtremely weak password. It can be compromised. Try again')
    else:
        regexs_list = store_regex()
        rating = rate_password_strength(user_password, regexs_list)
        print('Your passworn rating: {}'.format(rating))