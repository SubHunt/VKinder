import requests
# import vk_api
from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


class VK:

    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

#
#
# # token = input('Token: ')
# token = 'vk1.a.CasC3sJWxqhRV7k54DcK-m76JdA25FdxKrj0661UxDZPeXLXBnR6i6hXR7vaNH3lIDJFWMEnLmChj41WJhK46kwl5CtraL6T4D4IzNO9SAmMU6EbyJzuW1dcWlNmxoU6oVQt3FxM7KLIAv-Hax9Y99Qzx89nb3XkOOjT15wQgcMqd-5H0vHx_N-fDGqvmEYps-NLJok4oKBU8DMif21ndQ'
# vk = vk_api.VkApi(token=token)
# longpoll = VkLongPoll(vk)
#
#
# def write_msg(user_id, message):
#     vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})
#
#
# for event in longpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW:
#
#         if event.to_me:
#             request = event.text
#
#             if request == "привет":
#                 write_msg(event.user_id, f"Хай, {event.user_id}")
#             elif request == "пока":
#                 write_msg(event.user_id, "Пока((")
#             else:
#                 write_msg(event.user_id, "Не поняла вашего ответа...")