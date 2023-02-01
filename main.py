import time
from pprint import pprint
from modules import vk_access
import configparser
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
config = configparser.ConfigParser()
config.read("config.ini")
access_token = config['Tokens']['vk_token']
user_id1 = config['Tokens']['user_id']
group_token = config['Tokens']['group_token']
vk_group = vk_api.VkApi(token=group_token)
api_token = vk_group.get_api()
long_poll = VkLongPoll(vk_group)
vk_user = vk_api.VkApi(token=access_token)
session_api = vk_user.get_api()


def start(vk2, users_list):
    """Принимает сообщения/команды от пользователя и вызывает соответствующие функции"""
    i = 0
    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            vk_user = vk_access.BotEvents(vk_group, event.user_id) # Создаем экземпляр класса для обработки сообщений
            if event.to_me:
                request = event.text
                if request == "Привет":
                    vk_user.write_msg(f"Хай, {event.user_id}")
                    vk_user.keyboard_main_menu(api_token, 'Какие планы на сегодня?')
                elif request == 'Найти людей':
                    res = vk2.photos_info(users_list['items'][i])
                    vk_user.fast_search(api_token, f"{res['first_name']} {res['last_name']}\nПрофиль: https://vk.com/id{res['id']}\nФото:\n1 {res['first_photo']['link']}\n2 {res['second_photo']['link']}\n3 {res['third_photo']['link']}")
                elif request == 'Следующий':
                    res = vk2.photos_info(users_list['items'][i+1])
                    vk_user.fast_search(api_token, f"{res['first_name']} {res['last_name']}\nПрофиль: https://vk.com/id{res['id']}\nФото:\n1 {res['first_photo']['link']}\n2 {res['second_photo']['link']}\n3 {res['third_photo']['link']}")
                elif request == 'Предыдущий':
                    res = vk2.photos_info(users_list['items'][i-1])
                    vk_user.fast_search(api_token, f"{res['first_name']} {res['last_name']}\nПрофиль: https://vk.com/id{res['id']}\nФото:\n1 {res['first_photo']['link']}\n2 {res['second_photo']['link']}\n3 {res['third_photo']['link']}")
                elif request == "пока" or request == "Выход":
                    vk_user.write_msg("До новых встреч)")
                    exit()
                else:
                    vk_user.write_msg("Не поняла вашего ответа...")


if __name__ == "__main__":
    vk2 = vk_access.VK(access_token, user_id1)
    users_list = vk2.users_info_2(session_api)
    start(vk2, users_list)


