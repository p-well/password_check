# Password Strength Validator

The scripts checks strength of your password and rates it on a 10-points scale.

Passwords strength calculated by criterions like as following:
- prohibition of words found in a password blacklist
- password lenght (3 levels)
- the use of both upper-case and lower-case letters (case sensitivity)
- inclusion of numerical digits
- inclusion of special characters, such as @, #, $
- absence of repeated symbols more than 2 time
- absence of phone number like <i>89********</i>
- absence of numerical year or date of birth (4 digits)


Pavel Kadantsev, 2018. <br/>
p.a.kadantsev@gmail.com


# Installation

Python 3.5 should be already installed. <br />
Clone this repo on your machnine and install dependencies using ```pip install -r requirements.txt``` in CLI. <br />
It is recommended to use virtual environment in order to keep your global scope clean.


# Usage

To run the script execute ```python password_checker.py``` in CLI. <br />
Then script expects you type your password (it will be hidden on your screen).

The first step is to define whether your password is found in blacklist or not.
By default the script uses list of prohibited passwords downloaded from [here](https://raw.githubusercontent.com/skyzyx/bad-passwords/master/raw-mutated.txt).

You may build and use your own list of bad passwords.</br> 
In this case you have to specify filepath as an additional agrument when call script:

<pre>
<b>>python password_checker.py -u my_blacklist.txt</b>
</pre>

Your passwords must be stored in a <i>.txt</i> file, each password on a new line.

The script will not perform additional evaluation of your password if it was found in blacklist.


In case of script can't get bad passwords list (no internet connection or your file is empty) it will just skip this check.

# Example of Script Launch

When using blacklist from the web:

<pre>
<b>>python password_checker.py</b>

Type your password:

Waiting for response...

Your password rating: 8
</pre>


When using your own blacklist and your password was found within prohibited password:
<pre>
<b>python password_checker.py -u blacklist.txt</b>

Type your password:

Extremely weak password. It can be compromised. Try again.
</pre>


When path to your blacklist is incorrect an error is raised:

<pre>
<b>>python password_checker.py -u black__list.txt</b>

usage: password_checker.py [-h] [-u USERLIST]
password_checker.py: error: File not found.
</pre>


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
    
