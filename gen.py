import telebot
bot = telebot.TeleBot('5742949378:AAFvc34g6xB4IprPDMZSzp2XU4hUp2o77nA')


warn_counter = {}


@bot.message_handler(commands=['warn'])
def send_warn(message):
    chat_id = message.chat.id
    username = message.from_user.username
    user_id = message.from_user.id
    
    if user_id not in warn_counter:
        warn_counter[user_id] = 1
        bot.send_message('-1001895543248' , f'Модератор {message.from_user.username} прописал /warn. Количество действий сегодня {warn_counter[user_id]}.')
        
    else:
        warn_counter[user_id] += 1
        bot.send_message('-1001895543248' , f'Модератор {message.from_user.username} прописал /warn. Количество действий сегодня {warn_counter[user_id]}.')
    
@bot.message_handler(commands=['ban'])
def send_warn(message):
    chat_id = message.chat.id
    username = message.from_user.username
    user_id = message.from_user.id
    
    if user_id not in warn_counter:
        bot.send_message('-747039927' , f'Модератор {message.from_user.username} прописал /ban. Количество действий сегодня {warn_counter[user_id]}.')
            
    else:
        warn_counter[user_id] += 1
        bot.send_message('-747039927' , f'Модератор {message.from_user.username} прописал /ban. Количество действий сегодня {warn_counter[user_id]}.')
            


bot.polling()