from re import findall
import requests


def fetch_web_blacklist(url):
    try:
        return requests.get(url).text.split('\n')
    except ConnectionError:
        return []


def load_user_blacklist(filepath):
    with open(filepath, mode='r', encoding='utf-8') as blacklist_data:
        return blacklist_data.read().split('\n')


def is_password_in_blacklist(password, 
                             web_blacklist,
                             user_blacklist):
    return password in web_blacklist or password in user_blacklist


def store_positive_check_regex():
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


def store_negative_check_regex():
    regexs = [
              r'[8-9]{1}[0-9]{9}', # contain phone number
             ]


def rate_password_strength(user_password, regexs_list):
    rating = 0
    for template in regexs_list:
        if findall(template, user_password):
            print(template)
            rating += 1
    return rating

if __name__ == '__main__':
    url = "https://raw.githubusercontent.com/skyzyx/bad-passwords/master/raw-mutated.txt"
    web_blacklist = fetch_web_blacklist(url)
    user_blacklist = load_user_blacklist('blacklist.txt')
    user_password = input('Type your password here: ')
    if is_password_in_blacklist(
                                user_password,
                                web_blacklist,
                                user_password
                                ):
         print('Extremely weak password that can be compromised. Try again.')
    regexs_list = store_positive_check_regex()
    print(rate_password_strength(user_password, regexs_list))
    