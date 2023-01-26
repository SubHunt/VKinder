import requests
import vk_api

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


access_token = 'vk1.a.CasC3sJWxqhRV7k54DcK-m76JdA25FdxKrj0661UxDZPeXLXBnR6i6hXR7vaNH3lIDJFWMEnLmChj41WJhK46kwl5CtraL6T4D4IzNO9SAmMU6EbyJzuW1dcWlNmxoU6oVQt3FxM7KLIAv-Hax9Y99Qzx89nb3XkOOjT15wQgcMqd-5H0vHx_N-fDGqvmEYps-NLJok4oKBU8DMif21ndQ'
user_id = '179864387'
vk = VK(access_token, user_id)
# print(vk.users_info())