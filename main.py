from modules import vk_access
import configparser
from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

config = configparser.ConfigParser()
config.read("config.ini")
access_token = config['Tokens']['vk_token']
group_token = config['Tokens']['group_token']
user_id1 = config['Tokens']['user_id']
vk = vk_api.VkApi(token=group_token)
longpoll = VkLongPoll(vk)
# Клавиатура
keyboard = VkKeyboard(one_time=True)
# keyboard = VkKeyboard(inline=True)  # Inline-режим
keyboard.add_button('Найти людей', color=VkKeyboardColor.SECONDARY)
keyboard.add_line()
keyboard.add_button('Просмотр избранных', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button('Выход', color=VkKeyboardColor.NEGATIVE)
vk_session = vk_api.VkApi(token=group_token)
vk2 = vk_session.get_api()
# Callback клавиатура
# from vk_api.keyboard import VkKeyboardButton
# keyboard_callback = VkKeyboardButton()
# keyboard_callback.CALLBACK('Something')


def write_msg(user_id, message):
    vk.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'random_id': randrange(10 ** 7),
    })


def sender(user_id, text):
    vk2.messages.send(user_id=user_id, message=text, random_id=0, keyboard=keyboard.get_keyboard())


if __name__ == "__main__":
    vk1 = vk_access.VK(access_token, user_id1)
    first_name = vk1.users_info()['response'][0]['first_name']  # Получаем имя пользователя

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:
                request = event.text

                if request == "привет":
                    write_msg(event.user_id, f"Хай, {first_name}")
                    sender(event.user_id, 'Какие планы на сегодня?')
                elif request == "пока":
                    write_msg(event.user_id, "До новых встреч)")
                else:
                    write_msg(event.user_id, "Не поняла вашего ответа...")
