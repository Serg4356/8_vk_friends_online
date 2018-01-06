# Watcher of Friends Online

Programm searches for friends who are online in [Vkontakte](https://vk.com) and displays list of their first and last names in concole.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

Example of programm output:

```bash
$ python vk_friends_online.py
Enter login: some_login
Password: # Prompt the user for a password without echoing
Friends online:
Ivan Ivanov
Petr Petrov
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
