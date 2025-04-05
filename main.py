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
    select_query = '''SELECT * FROM students;'''
    cursor.execute(select_query)  # Выполнение запроса с параметром
    records = cursor.fetchall()  # Извлечение записей

    print("Данные о студентах:")
    for s in records:
        print(f'{s[0]}. {s[1]} {s[2]} курс {s[4]}, возраст {s[3]}')


except Exception as error:
    print("Ошибка при подключении к Базе данных", error)

finally:
    # Закрытие соединения
    if connection:
        connection.close()
        print("Соединение с PostgreSQL закрыто")




# def student_list():
#             select_query = '''SELECT * FROM students;'''
#
#             cursor.execute(select_query)  # Выполнение запроса с параметром
#             records = cursor.fetchall()  # Извлечение записей
#
#             print("Данные о студентах:")
#             for row in records:
#                 print(row)  # Печать каждой записи
#
# def update_bd():
#         pass
#
# def add_student():
#         pass
#
# def delete_student():
#         pass
#
#
#
# def main():
#         while True:
#             choice = int(input("\nВыберите действие (0-5): "))
#             print("\n1. Добавить студента в базу данных")
#             print("2. Просмотреть список студентов")
#             print("3. Изменить/обновить данные студента")
#             print("4. Удалить студента из базы данных")
#             print("5. Выход")
#
#             if choice == 1:
#                 students_data = input(
#                     str(input("Имя: ")),
#                     str(input("Фамилия: ")),
#                     int(input("Возраст: ")),
#                     int(input("Курс: "))
#                 )
#                 add_student()
#                 print(f"Студент добавлен в базу данных")
#             elif choice == 2:
#                 student_list()
#
#             elif choice == 3:
#                 pass
#             elif choice == 4:
#                 pass
#             elif choice == 5:
#                 print("Программа завершена")
#                 break
#             else:
#                 print("Неверный выбор. Пожалуйста, выберите действие от 0 до 5")
#
# if name == "main":
#     main()



#
#
#     def update_data():# Обновление данных
#
#         update_data = '''
#         UPDATE students
#         SET name = %s
#         WHERE name = %s;
#         '''
#
#     # Данные для обновления
#
#         cursor_db.execute(update_data, new_student)  # Выполнение запроса с параметрами
#         connection_db.commit()  # Подтверждение изменений
#         print("Данные успешно обновлены в таблице 'employees'")
#
#         update_query = '''
#         UPDATE students
#         SET position = %s
#         WHERE hire_date > %s;
#         '''
#         new_position = ('Стажер', '2023-01-01')
#
#         cursor.execute(update_query, new_position)  # Выполнение запроса с параметрами
#         connection.commit()  # Подтверждение изменений
#
#
#         # SQL-запрос для выборки данных
#         select_query = 'SELECT * FROM employees;'
#
#         cursor.execute(select_query)  # Выполнение запроса
#         records = cursor.fetchall()  # Извлечение всех записей
#
#     print("Данные из таблицы 'employees':")
#     for row in records:
#         print(row)  # Печать каждой записи
#
#         # SQL-запрос с фильтром
#         select_query = "SELECT * FROM employees WHERE position = %s;"
#         position = ('Разработчик',)
#
#         cursor_db.execute(select_query, position)  # Выполнение запроса с параметром
#         records = cursor_db.fetchall()  # Извлечение записей
#
#
# def close_connection(): # Закрытие соединения
#
#     if connection_db():
#         connection_db.close()
#         print("Соединение с PostgreSQL закрыто")
#
#
# def main():
#     # manager = StudentManager()
#
#
#     while True:
#
#         print("\n1. Добавить студента в базу данных")
#         print("2. Просмотреть список студентов")
#         print("3. Изменить/обновить данные студента")
#         print("4. Удалить студента из базы данных")
#         print("5. Выход")
#
#         choice = int(input("\nВыберите действие (0-5): "))
#
#         if choice == "1":
#             students_data = input(
#                 input("Имя: "),
#                 input("Фамилия: "),
#                 int(input("Возраст: ")),
#                 int(input("Курс: "))
#             )
#             insert_data()
#             print(f"Студент добавлен в базу данных")
#         elif choice == "2":
#
#
#         elif choice == "3":
#             pass
#         elif choice == "4":
#             pass
#         elif choice == "5":
#
#             close_connection()
#             print("Программа завершена")
#             break
#         else:
#             print("Неверный выбор. Пожалуйста, выберите действие от 0 до 5")
#
# if name == "main":
#     main()
