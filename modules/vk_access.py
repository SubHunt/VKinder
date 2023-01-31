import requests
from random import randrange
from .keyboards import kb_main_menu
import time
from pprint import pprint


class VK:
    URL = 'https://api.vk.com/method/'

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
        user_data = {}
        user_data['first_name'] = response['response'][0]['first_name']
        user_data['last_name'] = response['response'][0]['last_name']
        user_data['city'] = response['response'][0]['city']['id']
        user_data['byear'] = str(response['response'][0]['bdate']).split('.', 2)[2]
        profile = 'https://vk.com/id' + self.id
        user_data['sex'] = response['response'][0]['sex']

        """Поиск пользователей по таким же критериям: пол, город и год рождения"""
        users = session_api.users.search(sex=user_data['sex'], city=user_data['city'], birth_year=user_data['byear'], count=1000, field='domain')

        """Возможно, этот блок нужно перенести в отдельную функцию или передавать/возвращать список пользователей"""
        id_list = []
        for user in users['items']:
            """Просмотр всех пользователей в сокращенном формате"""
        #     print(user['id'], user['first_name'], user['last_name'])
            """Добавляем id всех найденных пользователей в список, для дальнейшего перемещения влево-вправо стрелками по индексам"""
            id_list.append(user['id'])
        return id_list


    def photos_info(self, id_list):
        """Цикл по всем найденным профилям. Перебираем фотографии профилей"""
        for user in id_list:
            print('---------------------new user---------------------------------------------')
            """Здесь находятся все фото каждого профиля"""
            """Профиль может быть закрыт, чтобы избежать ошибку, делаем обход через блок try"""
            try:
                items = self.photos_get(user)['response']['items']
                photos_info = []
                """Здесь по очереди перебираются все фото во всех доступных размерах"""
                for item in items:
                    """На первом этапе забираем каждое фото в максимальном разрешении и ссылку на нее"""
                    info = {
                        'size': item['sizes'][-1]['type'],
                        'link': item['sizes'][-1]['url'],
                        'likes': item['likes']['count'],
                        # 'file_name': f"{item['sizes'][-1]['url']}.file" # Пока неизвестно нужнео ли имя файла, его можно сгенерить датой и врменем создания
                    }
                    photos_info.append(info)

                """ Сортируем наш список словарей с фото по убыванию лайков. Каждый словарь - это данные одного фото"""
                sort_photos_likes = sorted(photos_info, key=lambda d: d['likes'], reverse=True)
                """Нам нужно только первые 3 фото с наибольшими лайками, остальные не берем"""
                photo_best_3 = sort_photos_likes[:3]
                pprint(photo_best_3)
                """Если профиль закрыт или получаем какую-то ошибку, переходим к следующему профилю"""
            except:
                continue

    def photos_get(self, user):
        """Функция заходит к пользователю из списка и забирает с его профиля все фотографии
        (по умолчанию кол-во ограничено 200 фотографиями если столько есть в его профиле)"""
        photos_url = self.URL + 'photos.get'
        photos_params = {
            'owner_id': user,
            'album_id': 'profile',
            'rev': 0,
            'extended': 1,
            'count': 200
        }

        params = {**self.params, **photos_params}
        response = requests.get(photos_url, params).json()
        """С задержкой надо поэскпериментировать, 
        если убрать, то сервер блокирует выдачу собщением слишком много запросов"""
        time.sleep(2)
        return response


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

    def fast_search(self):
        pass

    def next_user(self):
        pass

    def previous_user(self):
        pass

    def back(self):
        pass
