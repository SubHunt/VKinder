from modules import vk_access
import configparser
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
config = configparser.ConfigParser()
config.read("config.ini")
access_token = config['Tokens']['vk_token']
user_id1 = config['Tokens']['user_id']
group_token = config['Tokens']['group_token']
vk = vk_api.VkApi(token=group_token)
api_token = vk.get_api()
long_poll = VkLongPoll(vk)
vk1 = vk_api.VkApi(token=access_token)
session_api = vk1.get_api()


def start():
    """Принимает сообщения/команды от пользователя и вызывает соответствующие функции"""
    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            vk_user = vk_access.BotEvents(vk, event.user_id) # Создаем экземпляр класса для обработки сообщений
            if event.to_me:
                request = event.text
                if request == "1":
                    vk_user.write_msg(f"Хай, {event.user_id}")
                    vk_user.keyboard_main_menu(api_token, 'Какие планы на сегодня?')
                elif request == "пока" or request == "Выход":
                    vk_user.write_msg("До новых встреч)")
                    exit()
                else:
                    vk_user.write_msg("Не поняла вашего ответа...")


if __name__ == "__main__":
    # start()
    # vk = vk_access.VK(access_token, user_id1)
    vk = vk_access.VK(access_token, user_id1)
    us_info = vk.users_info_2(session_api)
    vk.photos_info(us_info)

    # users = session_api.users.search(sex=2, birth_year=1981, count=1000, field='domain', from_group=1)
    # print(users)
    # print(build_url())
    # print(vk.users_info_2())

