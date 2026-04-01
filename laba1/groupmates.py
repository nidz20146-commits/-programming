# coding: utf-8

# Список студентов
groupmates = [
    {
        "name": "Василий",
        "group": "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": "Анна",
        "group": "912-1",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": "Георгий",
        "group": "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": "Валентина",
        "group": "912-1",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]
    },
    {
        "name": "Дмитрий",
        "group": "912-3",
        "age": 20,
        "marks": [4, 4, 4, 5, 4]
    }
]

def print_students(students):
    """
    Форматированный вывод списка студентов в виде таблицы.
    """
    print("Имя студента".ljust(15), 
          "Группа".ljust(8), 
          "Возраст".ljust(8), 
          "Оценки".ljust(20))
    
    for student in students:
        print(student["name"].ljust(15), 
              student["group"].ljust(8), 
              str(student["age"]).ljust(8), 
              str(student["marks"]).ljust(20))
    print("\n")

def filter_students(students, avg_mark):
    """
    Фильтрация студентов по средней оценке.
    Возвращает список студентов со средним баллом выше заданного.
    """
    filtered = []
    for student in students:
        # Считаем средний балл
        student_avg = sum(student["marks"]) / len(student["marks"])
        # Сравниваем с заданным параметром
        if student_avg >= avg_mark:
            filtered.append(student)
    return filtered

# --- Основная программа ---

if __name__ == '__main__':
    # 1. Вывод всех студентов
    print("=== Все студенты ===")
    print_students(groupmates)

    # 2. Фильтрация (пример: студенты со средним баллом >= 4.0)
    threshold = 4.0
    print(f"=== Студенты со средним баллом >= {threshold} ===")
    filtered_list = filter_students(groupmates, threshold)
    
    if filtered_list:
        print_students(filtered_list)
    else:
        print("Студентов с таким средним баллом не найдено.\n")