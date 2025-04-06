import telebot
from config import BOT_TOKEN, DB_NAME
from database import Database
from keyboards import main_menu, group_menu

bot = telebot.TeleBot(BOT_TOKEN)
db = Database(DB_NAME)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username or "Unknown"
    db.add_user(user_id, username)
    bot.reply_to(message, 
                 "Добро пожаловать! Я бот онлайн-школы. Сначала выбери свою группу.",
                 reply_markup=main_menu())

@bot.message_handler(func=lambda message: message.text == "🔄 Выбрать группу")
def choose_group(message):
    groups = db.get_groups()
    if not groups:
        bot.reply_to(message, "Группы пока не добавлены. Обратитесь к администратору.")
        return
    bot.reply_to(message, "Выбери свою группу:", reply_markup=group_menu(groups))

@bot.message_handler(func=lambda message: message.text in [g[1] for g in db.get_groups()])
def set_group(message):
    user_id = message.from_user.id
    group_name = message.text
    groups = db.get_groups()
    group_id = next(g[0] for g in groups if g[1] == group_name)
    db.set_user_group(user_id, group_id)
    bot.reply_to(message, f"Ты выбрал группу: {group_name}. Теперь можешь запросить расписание!",
                 reply_markup=main_menu())

@bot.message_handler(func=lambda message: message.text == "📅 Получить расписание")
def send_schedule(message):
    user_id = message.from_user.id
    group_id = db.get_user_group(user_id)
    
    if not group_id:
        bot.reply_to(message, "Сначала выбери группу с помощью кнопки '🔄 Выбрать группу'.",
                    reply_markup=main_menu())
        return

    schedule = db.get_schedule(group_id)
    if not schedule:
        bot.reply_to(message, "Расписание для твоей группы пока пустое. Обратитесь к администратору.")
        return
    
    response = f"📅 Расписание уроков для группы {next(g[1] for g in db.get_groups() if g[0] == group_id)}:\n\n"
    for lesson in schedule:
        name, time, day = lesson
        response += f"📚 {name}\n⏰ {time}\n🗓️ {day}\n\n"
    
    bot.reply_to(message, response, reply_markup=main_menu())

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Пожалуйста, используй кнопки меню.", reply_markup=main_menu())

if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)