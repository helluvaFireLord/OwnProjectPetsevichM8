# OwnProjectPetsevichM8

## Разработка интерактивного телеграм-бота для онлайн-школы

> Мы - онлайн-школа, стремящаяся обеспечить наших учеников удобными и эффективными инструментами для обучения. Нам нужен телеграмм-бот, который будет высылать расписание уроков нашим студентам. Студенты будут подписаны на бота, и для того, чтобы получить расписание - должны будут нажать на кнопку.

### Бот будет уметь:
> 1. Бот должен поддерживать интерактивные элементы - кнопки, для удобного взаимодействия со студентами.
> 2. Студенты должны иметь возможность запросить расписание всех уроков школы, нажав на соответствующую кнопку.
> 3. Разработчик должен предоставить документацию по использованию бота для администраторов онлайн-школы и их студентов.
> 4. Бот должен предоставлять простой и интуитивно понятный интерфейс для студентов.

#### Как работает бот

##### Описание
Бот предоставляет расписание уроков студентам онлайн-школы с учетом их учебной группы.

##### Инструкция для администраторов
1. **Добавление групп:**
   - Подключение к базе данных `school_schedule.db`.
   - Добавление записи в таблицу `Groups`:
  
2. **Добавление уроков:**
- Добавление записи в таблицу `Lessons` с указанием `group_id`:

3. **Запуск бота:**
- Назначение токена в `config.py`
- Запуск: `python main.py`

#### Инструкция для студентов
1. Нажать `/start`.
2. Нажать "🔄 Выбрать группу" и выбрать группу.
3. Нажать "📅 Получить расписание" для просмотра расписания группы.
