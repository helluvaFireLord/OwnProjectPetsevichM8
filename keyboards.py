from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_schedule = KeyboardButton("📅 Получить расписание")
    btn_change_group = KeyboardButton("🔄 Выбрать группу")
    markup.add(btn_schedule, btn_change_group)
    return markup

def group_menu(groups):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for group_id, group_name in groups:
        markup.add(KeyboardButton(f"{group_name}"))
    return markup