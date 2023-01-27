import requests
from random import randrange
from .keyboards import kb_main_menu


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

    def users_info_2(self, session_api):
        url = 'https://api.vk.com/method/users.get'
        user_params = {'user_ids': self.id, 'fields': 'bdate, city, sex, counters'}
        params = {'access_token': self.token, 'v': self.version}
        params2 = {**params, **user_params}
        response = requests.get(url, params2).json()
        """Собираем данные клиента: ФИО, дату рождения, город, пол
        Год рождения выдергивать через try, может быть пустым на splite посыпится
        """
        first_name = response['response'][0]['first_name']
        last_name = response['response'][0]['last_name']
        city = response['response'][0]['city']['title']
        byear = str(response['response'][0]['bdate']).split('.', 2)[2]
        profile = 'https://vk.com/id' + self.id
        sex = response['response'][0]['sex']
        print(response)
        print(first_name, last_name, byear, city, sex, profile)
        """Поиск пользователей по нужным критериям"""
        users = session_api.users.search(sex=sex, birth_year=byear, count=1000, field='domain')
        print(users)
        # users = api_token.users.search(city=CITY, age_from=AGE_FROM, age_to=AGE_TO, fields='domain')
        # print(users)
        # res_users = requests.get(f'https://api.vk.com/method/users.get?user_ids={self.id}&fields=bdate, city&access_token={self.token}&v={self.version}')
        # print(res_users.json())



class BotEvents:
    def __init__(self, vk, user_id):
        self.vk = vk
        self.user_id = user_id

    def write_msg(self, message):
        """Отправляем сообщение"""
        self.vk.method('messages.send', {
            'user_id': self.user_id,
            'message': message,
            'random_id': randrange(10 ** 7),
        })

    def keyboard_main_menu(self, api_token, message, random_id=randrange(10 ** 7)):
        """Отправляем клавиатуру"""
        api_token.messages.send(user_id=self.user_id,
                                message=message, random_id=random_id,
                                keyboard=kb_main_menu.get_keyboard())
