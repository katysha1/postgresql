from idlelib.window import register_callback

import psycopg2

try:
    # Установить соединение с базой данных
    connection = psycopg2.connect(
        user="postgres",
        password="1234",
        host="127.0.0.1",
        port="5432",
        database="postgres"
    )
    print("Подключение к Базе данных 'Студенты' успешно выполнено")

    cursor = connection.cursor()

    # insert_students: str = '''
    # INSERT INTO students (first_name, second_name, age, course)
    # VALUES (%s, %s, %s, %s);
    # '''
    #
    #   # Данные для вставки
    # students_data = [   # ввод данных студентов
    #     ('Юлия', 'Попова', '25', '4'),
    #     ('Степан', 'Яковлев', '17', '1'),
    #     ('Елена', 'Сидорова', '23', '5')
    # ]
    # cursor.executemany(insert_students, students_data)  # Выполнение запроса с параметрами
    # connection.commit()  # Подтверждение изменений
    # print("Список студентов успешно добавлен в таблицу 'students'")

# # таблица создана, повторный вызов кода выдаст ошибку
# create_table_students = '''
    # CREATE TABLE students(
    #     id SERIAL PRIMARY KEY,
    #     first_name VARCHAR(100) NOT NULL,
    #     second_name VARCHAR(100) NOT NULL,
    #     age INTEGER CHECK(async_generator >=16),
    #     course INTEGER
    # );
    # '''
    # cursor.execute(create_table_students)
    # connection.commit()
    # print("Таблица 'employees' успешно создана")
    #
    # # Добавить данные в пустую Базу данных (Данные добавлены. Повторное добавление приведет к ошибке)
    #
    # insert_students: str = '''
    # INSERT INTO students (first_name, second_name, age, course)
    # VALUES (%s, %s, %s, %s);
    # '''
    # #
    # #   # Данные для вставки
    # students_data = [   # ввод данных студентов
    #     ('Наталья', 'Сидорова', '21', '1'),
    #     ('Иван', 'Коротков', '22', '2'),
    #     ('Петр', 'Шестаков', '18', '4')
    # ]
    # cursor.execute(insert_students, students_data)  # Выполнение запроса с параметрами
    # connection.commit()  # Подтверждение изменений
    # print("Данные успешно добавлены в таблицу 'students'")

# вывод списка студентов
#     select_query = '''SELECT * FROM students;'''
#     cursor.execute(select_query)  # Выполнение запроса с параметром
#     records = cursor.fetchall()  # Извлечение записей
#
#     print("Данные о студентах:")
#     for s in records:
#         print(f'{s[0]}. {s[1]} {s[2]} курс {s[4]}, возраст {s[3]}')

# Изменение/обновление данных
#     update_query = '''
#     UPDATE students
#     SET course = %s
#     WHERE age > %s;
#     '''
#     new_position = (6, 22)
#
#     cursor.execute(update_query, new_position)
#     connection.commit()

# Удаление данных
    delete_query = '''
    DELETE FROM students
    WHERE first_name = %s;
    '''
# Данные для удаления
    delete_name = ('Наталья',)
    cursor.execute(delete_query, delete_name)
    connection.commit()
    print(f'Студент {delete_name} удален(-а) из базы данных студентов')

except Exception as error:
    print("Ошибка при подключении к Базе данных", error)

finally:
    # Закрытие соединения
    if connection:
        connection.close()
        print("Соединение с PostgreSQL закрыто")
