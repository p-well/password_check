import argparse

import requests

from os.path import exists
from re import findall


def create_args_parser(url):
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--password')
    parser.add_argument('-w', '--weblist', default = url)
    parser.add_argument('-u', '--userlist', nargs='?')
    return parser


def check_args(parser, args):
    if args.userlist is None:
        parser.error('--userlist is called with no arguments')
    if args.userlist is None:
        parser.error('Missing argument after --userlist')
    if not exists(args.userlist):
        parser.error('File not found.')
    #if not args.top_numb.isdigit():
    #    parser.error('Integer expected.')


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


def is_password_in_blacklist(password, 
                             web_blacklist,
                             user_blacklist):
    return (password in web_blacklist or password in user_blacklist)


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
              r'^(?!([8-9]{1}[0-9]{9}))'  #Doesn't contain phone number
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
    url = "https://raw.githubusercontent.com/skyzyx/bad-passwords/master/raw-mutated.txt"
    parser = create_args_parser(url)
    args = parser.parse_args()
    print(args)
    check_args(parser, args)
    # web_blacklist = fetch_web_blacklist(args.weblist)
    # user_blacklist = load_user_blacklist(args.userlist)
    # if is_password_in_blacklist(user_password,
    #                             web_blacklist,
    #                             user_blacklist):
    #      print('Extremely weak password that can be compromised. Try again.\n')
    #      exit()
    # else:
    #     regexs_list = store_regex()
    #     print(rate_password_strength(user_password, regexs_list))
