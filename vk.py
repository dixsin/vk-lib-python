import vk

# Данные для входа в вк чат
id = 1 # Айди для верификации чата ВК при использовании LongPool
token = 'token' # Ваш персональный токен ВК

print('Выполняется подключение к VK Api...')
session = vk.Session()
vk_api = vk.API(session)
vk_api.users.get(user_id=id)
session = vk.Session(access_token=token)
print('Выполнено подключение к VK Api!')

id_user = 1 # ID пользователя которому будет отправлено сообщение
while true:
  message_from_user = input('Ваше сообщение пользователю >>> ')
  vk_api.messages.send(users_id=id_user, messages=message_from_user)
