import vk

# Ваш цифровой ID VK
id = 1
# Ваш токен VK
token = 'token'

print('Выполняется подключение к VK Api...')
session = vk.Session()
vk_api = vk.API(session)
vk_api.users.get(user_id=id)
session = vk.Session(access_token=token)
print('Выполнено подключение к VK Api...')

vk_api.messages.send(users_id=0, messages=’hello’)
