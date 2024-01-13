import telebot
import schedule

import time
import os
import sys

# import sys
# sys.path.append('/home/w0461585/domains/my.matrium.ru')

# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matrium.settings')
# import django
# django.setup()

# # Здесь можно импортировать модели Django
# from matrium_app.models import *


import os, sys
activate_this = '/home/w0461585/python/bin/activate_this.py'
with open(activate_this) as f:
     exec(f.read(), {'__file__': activate_this})


# Замените 'ВАШ_ТОКЕН_БОТА' на ваш реальный токен бота
bot = telebot.TeleBot('6094206173:AAEFXTPGaLkJdhEJ0jGHE7SUl3VloMOMtPk')

# Замените 'CHAT_ID_КАНАЛА' на реальный chat_id вашего канала
channel_id = '-1001770307515'

chat_id_to_kick_from = '-1001942494903' #Чат id ЧАТА обсуждение
chat_id_to_kick_from_second = '-1001871370964' #Чат id чата VIP длань господня


chat_id_to_ignore = '-1001942494903'

telebot.apihelper.SESSION_BASE_URL = 'https://api.telegram.org'


# Открываем файл terminal.txt в режиме записи (или создаем его, если он не существует)
terminal_log_file = open('/home/w0461585/domains/my.matrium.ru/tgbot/terminal.txt', 'w')

# Перенаправляем стандартный вывод в файл
sys.stdout = terminal_log_file

# Остальной код вашей программы



# ID чатов, в которых нужно банить пользователей
chat_id_1 = '-1001942494903'
chat_id_2 = '-1001871370964'

# Путь к файлу со списком заблокированных пользователей
banned_users_file = '/home/w0461585/domains/my.matrium.ru/tgbot/cheated_users_id.txt'

# Список заблокированных пользователей
banned_user_ids = set()

# Функция для загрузки и бана пользователей
def ban_users():
    global banned_user_ids
    try:
        with open(banned_users_file, 'r') as file:
            banned_user_ids = set(line.strip() for line in file if line.strip())
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    for user_id in banned_user_ids:
        try:
            # Бан пользователя навсегда
            bot.kick_chat_member(chat_id_1, user_id, until_date=0)
            bot.kick_chat_member(chat_id_2, user_id, until_date=0)
            print('Забанин')
        except Exception as e:
            print(f"Ошибка при бане пользователя {user_id}: {e}")


# # Обработчик сообщений
# @bot.message_handler(func=lambda message: message.from_user.id not in banned_user_ids)
# def handle_messages(message):
#     # Ваш код для обработки сообщений от незаблокированных пользователей
#     # ...

# # Планирование задачи
# schedule.every(10).seconds.do(ban_users)

# # Бесконечный цикл для выполнения задач
# while True:
#     schedule.run_pending()
#     time.sleep(1)










# Функция для загрузки списка chat_id пользователей из файла
def load_chat_ids_from_file(file_path):
    chat_ids = []
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                chat_ids.append(line.strip())
    return chat_ids

# Функция для сохранения списка chat_id пользователей в файл
def save_chat_ids_to_file(chat_ids, file_path):
    with open(file_path, "w") as f:
        for chat_id in chat_ids:
            f.write(str(chat_id) + "\n")

# Функция для удаления идентификатора чата из списка chat_ids
def remove_chat_id(chat_id, chat_ids):
    if chat_id in chat_ids:
        chat_ids.remove(chat_id)

# Функция для проверки подписки пользователей в канале и выдачи бана
def check_subscriptions_and_ban():
    file_path = "/home/w0461585/domains/my.matrium.ru/tgbot/chat_id_users_status_active.txt"
    chat_ids = load_chat_ids_from_file(file_path)

    # Проверяем каждый chat_id из файла
    for chat_id in chat_ids:
        try:
            # Проверяем статус участника в канале
            member = bot.get_chat_member(channel_id, chat_id)
            if member.status not in ["member", "administrator", 'owner']:
                # Определяем, какие разрешения должны быть у пользователя после кика (в данном случае, все разрешения отключены)
                
                bot.kick_chat_member(chat_id_to_kick_from, chat_id, until_date=0)
                bot.kick_chat_member(chat_id_to_kick_from_second, chat_id, until_date=0)  # until_date=0 для окончательного исключения
                
                print(f"Пользователь с chat_id {chat_id} покинул канал, чат и VIP чат")
                try:
                    # Попробуйте отправить пользователю сообщение
                    bot.send_message(chat_id, 'Вы были исключены из канала и из чата. Чтобы вернуться, оплатите подписку и напишите в обратную связь по кнопке ниже.')
                except telebot.apihelper.ApiTelegramException as e:
                    # Если возникает ошибка, возможно, пользователь заблокировал бота
                    print(f"Ошибка при отправке сообщения пользователю с chat_id {chat_id}: {e}")
                remove_chat_id(chat_id, chat_ids)
            else:
                print(f"Пользователь с chat_id {chat_id} подписан на канал.")
        except telebot.apihelper.ApiTelegramException as e:
            if e.error_code == 403:
                # Этот пользователь заблокировал бота, удаляем его из списка чатов
                remove_chat_id(chat_id, chat_ids)
                print(f"Пользователь с chat_id {chat_id} заблокировал бота и был удален из списка.")
            # Если возникает ошибка, возможно, пользователь не подписан на канал
            print(f"Ошибка при проверке подписки для пользователя. Пользователь покинул канал и чат. chat_id {chat_id}: {e}")
            try:
                # Попробуйте отправить пользователю сообщение
                bot.send_message(chat_id, 'Вы были исключены из канала и из чата. Чтобы вернуться, оплатите подписку и напишите в обратную связь по кнопке ниже.')
            except telebot.apihelper.ApiTelegramException as e:
                # Если возникает ошибка, возможно, пользователь заблокировал бота
                print(f"Ошибка при отправке сообщения пользователю с chat_id {chat_id}: {e}")
            remove_chat_id(chat_id, chat_ids)

    # После проверки всех пользователей, перезаписываем файл с обновленным списком chat_id
    terminal_log_file.close()
    save_chat_ids_to_file(chat_ids, file_path)




# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        if str(message.chat.id) != chat_id_to_ignore:
            file_path = "/home/w0461585/domains/my.matrium.ru/tgbot/chat_id_users_status_active.txt"
            chat_ids = load_chat_ids_from_file(file_path)
            if str(message.chat.id) in chat_ids:
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = telebot.types.KeyboardButton("📞 Обратная связь")
                item2 = telebot.types.KeyboardButton("📝 Регистрация")
                item3 = telebot.types.KeyboardButton("📢 Предложить мем")
                markup.add(item1, item2, item3)
                bot.send_message(
                    message.chat.id,
                    f"Выберите, что вас интересует.<b> {message.from_user.first_name}.</b>\nВаш <b>id telegram</b> для регистрации: <b>{message.chat.id}</b>",
                    parse_mode='html',
                    reply_markup=markup
                )

                bot.send_message(message.chat.id, "Вы уже зарегистрированы.")
            else:
                # Передайте оба аргумента в функцию save_chat_ids_to_file()
                save_chat_ids_to_file(chat_ids + [str(message.chat.id)], file_path)
                username = message.from_user.username
                if username is not None:
                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item1 = telebot.types.KeyboardButton("📞 Обратная связь")
                    item2 = telebot.types.KeyboardButton("📝 Регистрация")
                    item3 = telebot.types.KeyboardButton("📢 Предложить мем")
                    markup.add(item1, item2, item3)
                    bot.send_message(message.chat.id, f"Добро пожаловать,  {message.from_user.first_name}.\nВаш <b>id telegram</b> для регистрации: <b>{message.chat.id}</b>",
                                    parse_mode='html', reply_markup=markup)
                else:
                    bot.send_message(message.chat.id, "К сожалению, у вас не установлен <b>username.</b> ")
    except ApiException as e:
        if e.error_code == 403:
            # Этот пользователь заблокировал бота, удаляем его из списка чатов
            remove_chat_id(message.chat.id, chat_ids)
            print(f"Пользователь с chat_id {message.chat.id} заблокировал бота и был удален из списка.")
        else:
            # Обработка других ошибок Telegram API
            print(f"Ошибка Telegram API при обработке команды /start: {e}")    

chat_id = '-1001867534700' #Рабочий чат , куда будут приходить уведомления


@bot.message_handler(func=lambda message: message.from_user.id not in banned_user_ids, content_types=['text'])
def message_handler(message):
    if message.chat.type == 'private':
        if message.chat.id != chat_id_to_ignore:
        # is_subscribed = bot.get_chat_member('https://t.me/+r-0QhaZroJowMmVi', message.chat.id).status == 'member' or bot.get_chat_member('https://t.me/+r-0QhaZroJowMmVi', message.chat.id).status == 'administrator' or bot.get_chat_member('https://t.me/+r-0QhaZroJowMmVi', message.chat.id).status == 'creator'
        # if is_subscribed is True:
            if message.text == '📞 Обратная связь':
                feedback = bot.send_message(message.chat.id, 'Остались вопросы? Напиши нам!')
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                back_button = telebot.types.KeyboardButton('Назад')
                markup.add(back_button)
                bot.send_message(chat_id=message.chat.id, text="Нажмите кнопку 'Назад', если хотите вернуться.", reply_markup=markup)
                bot.register_next_step_handler(feedback, feedback_send)
                print('Обратная связь.', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))


            if message.text == 'Назад':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = telebot.types.KeyboardButton("📞 Обратная связь")
                item2 = telebot.types.KeyboardButton("📝 Регистрация")
                item3 = telebot.types.KeyboardButton("📢 Предложить мем")
                markup.add(item1, item2, item3)
                bot.send_message(message.chat.id, "Возвращаю...".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


            if message.text == '📝 Регистрация':
                feedback = bot.send_message(message.chat.id, 'Напишите и отправьте сообщение со своими данными в формате:\n- Имя\n- Фамилия\n- Номер телефона\n- Email\n- Город (откуда Вы)\n- Пол')
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                back_button = telebot.types.KeyboardButton('Назад')
                markup.add(back_button)
                bot.send_message(chat_id=message.chat.id, text="Нажмите кнопку 'Назад', если хотите вернуться.", reply_markup=markup)
                bot.register_next_step_handler(feedback, register_send)
                print('Обратная связь.', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))
                      
            if message.text == '📢 Предложить мем':
                feedback = bot.send_message(message.chat.id, 'Пришлите фото ( если фото нет, поставьте - )')
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                back_button = telebot.types.KeyboardButton('Назад')
                markup.add(back_button)
                bot.send_message(chat_id=message.chat.id, text="Нажмите кнопку 'Назад', если хотите вернуться.", reply_markup=markup)
                bot.register_next_step_handler(feedback, mem_photo_send)
                print('Мем.', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))


def feedback_send(message):
    if message.chat.id != chat_id_to_ignore:
        if message.text == 'Назад':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton("📞 Обратная связь")
            item2 = telebot.types.KeyboardButton("📝 Регистрация")
            item3 = telebot.types.KeyboardButton("📢 Предложить мем")
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, "Возвращаю...".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
        else:
            feedback_sms = str(message.text)
            print(f'Пользователь оставил сообщение: {feedback_sms}')
            username = message.from_user.username
            user_id = message.from_user.id

            bot.send_message(message.chat.id, '''Ваш вопрос успешно получен! Ожидайте, в течение 24 часов менеджер с вами свяжется.''')
            # Отправляем сообщение в группу
            bot.send_message(chat_id, f'''*Сообщение от **@{username}** ;*\n*ID: {user_id};*\n{feedback_sms}''', parse_mode='markdown')





def register_send(message):
    if message.chat.id != chat_id_to_ignore:
        if message.text == 'Назад':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton("📞 Обратная связь")
            item2 = telebot.types.KeyboardButton("📝 Регистрация")
            item3 = telebot.types.KeyboardButton("📢 Предложить мем")
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, "Возвращаю...".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
        else:
            feedback_sms = str(message.text)
            username = message.from_user.username
            user_id = message.from_user.id

            bot.send_message(message.chat.id, '''Супер! Ваша заявка получена. Ожидайте, в течение 24 часов Вам напишет менеджер и предоставит логин и пароль для входа. Ссылка для входа: https://my.matrium.ru/''')
            # Отправляем сообщение в группу
            bot.send_message(chat_id, f'''*Сообщение от **@{username}** ;*\n*ID: {user_id};*\n*Регистрация! *\n\n{feedback_sms}''', parse_mode='markdown')
            
user_data = {}
# Обработчик для получения фотографии
def mem_photo_send(message):
    user_id = message.from_user.id
    # Получите file_id фотографии
    if message.photo:
        file_id = message.photo[-1].file_id
        user_data[user_id] = {'file_id': file_id}
        bot.send_message(user_id, 'Отлично! Теперь отправьте текст для мема (Если его нет, поставьте -)')
        bot.register_next_step_handler(message, mem_message_send)  # Зарегистрируйте следующий шаг для обработки текста
    if message.text:
        if message.text == 'Назад':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton("📞 Обратная связь")
            item2 = telebot.types.KeyboardButton("📝 Регистрация")
            item3 = telebot.types.KeyboardButton("📢 Предложить мем")
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, "Возвращаю...".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
        else:
            bot.send_message(user_id, 'Отлично! Теперь отправьте текст для мема.')
            bot.register_next_step_handler(message, mem_message_send)  # Зарегистрируйте следующий шаг для обработки текста

# Обработчик для получения текста
def mem_message_send(message):
    if message.text == 'Назад':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton("📞 Обратная связь")
            item2 = telebot.types.KeyboardButton("📝 Регистрация")
            item3 = telebot.types.KeyboardButton("📢 Предложить мем")
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, "Возвращаю...".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
    else:
        user_id = message.from_user.id
        feedback_sms = message.text
        username = message.from_user.username
        if user_id in user_data and 'file_id' in user_data[user_id]:
            file_id = user_data[user_id]['file_id']
            bot.send_message(user_id, 'Ваш мем отправлен. Спасибо!')
            bot.send_photo(user_id, file_id, caption=feedback_sms, parse_mode='markdown')

            bot.send_message(chat_id, f'''*Сообщение от **@{username}** ;*\n*ID: {user_id};*\n*Мем *\n''', parse_mode='markdown')  
            bot.send_photo(chat_id, file_id, caption=feedback_sms, parse_mode='markdown')

            del user_data[user_id]  # Удаляем данные пользователя


        else:
            bot.send_message(user_id, f'Ваш мем отправлен. Спасибо!\nТекст: {feedback_sms}')  

            bot.send_message(chat_id, f'''*Сообщение от **@{username}** ;*\n*ID: {user_id};*\n*Мем *\n\nТекст: {feedback_sms}''', parse_mode='markdown')  






# Функция для запуска опроса каждые 300 секунд
def run_polling():
    while True:
        schedule.run_pending()
        time.sleep(240)



# Планирование проверки подписок каждые 300 секунд (5 минут)
terminal_log_file = open('/home/w0461585/domains/my.matrium.ru/tgbot/terminal.txt', 'w')
schedule.every(240).seconds.do(check_subscriptions_and_ban)
schedule.every(10).seconds.do(ban_users)


# Запуск опроса и проверки подписок в отдельном потоке
import threading
polling_thread = threading.Thread(target=run_polling)
polling_thread.daemon = True  # Установите daemon в True, чтобы поток работал в фоновом режиме
polling_thread.start()

# Отсюда начинается основной поток, в котором обрабатываются сообщения
bot.infinity_polling()


