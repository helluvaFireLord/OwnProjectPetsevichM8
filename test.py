import sqlite3
from config import DB_NAME  

def add_test_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()


    cursor.execute("INSERT INTO Groups (group_name) VALUES ('Группа 1')")
    cursor.execute("INSERT INTO Groups (group_name) VALUES ('Группа 2')")
    cursor.execute("INSERT INTO Groups (group_name) VALUES ('Группа 3')")


    cursor.execute("INSERT INTO Lessons (lesson_name, lesson_time, lesson_day, group_id) VALUES ('Математика', '10:00', 'Понедельник', 1)")
    cursor.execute("INSERT INTO Lessons (lesson_name, lesson_time, lesson_day, group_id) VALUES ('Русский язык', '11:00', 'Понедельник', 1)")
    cursor.execute("INSERT INTO Lessons (lesson_name, lesson_time, lesson_day, group_id) VALUES ('Физика', '12:00', 'Вторник', 2)")
    cursor.execute("INSERT INTO Lessons (lesson_name, lesson_time, lesson_day, group_id) VALUES ('Химия', '14:00', 'Среда', 2)")
    cursor.execute("INSERT INTO Lessons (lesson_name, lesson_time, lesson_day, group_id) VALUES ('История', '09:00', 'Четверг', 3)")


    cursor.execute("INSERT INTO Users (user_id, username, group_id, subscription_date) VALUES (123456, 'test_user', 1, datetime('now'))")

    conn.commit()
    conn.close()
    print("Тестовые данные успешно добавлены!")

if __name__ == "__main__":
    add_test_data()