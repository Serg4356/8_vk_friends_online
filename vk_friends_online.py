import vk
import time
import getpass


APP_ID = 6322128


def get_user_login():
    return input('Enter login: ')


def get_user_password():
    return getpass.getpass()


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends = api.friends.get(fields='online')
    friends_online =[]
    for friend in friends:
        if friend['online'] == 1:
            friends_online.append('{} {}'.format(friend['first_name'], friend['last_name']))
    return friends_online


def output_friends_to_console(friends_online):
    print('Friends online:')
    for friend in friends_online:
        print(friend)


if __name__ == '__main__':
    try:
        login = get_user_login()
        password = get_user_password()
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError:
        print('Password is incorrect, please try again.')