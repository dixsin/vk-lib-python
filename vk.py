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
print('Выполнено подключение к VK Api!')

id_user = input('Введите ID пользователя которому будете писать сообщения >>> ')
while true:
  message_from_user = input('Ваше сообщение пользователю >>> ')
  vk_api.messages.send(users_id=id_user, messages=message_from_user)
