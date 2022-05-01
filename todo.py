import random
HELP ="""
help - вывести справку
add  - добавить задачу в список (название запрашиваем у пользователя)
show - напечатать все добавленные задачи 
random - добавлять случайную задачу на дату  Сегодня"""

RANDOM_TASK = "Сделать 100 приседаний"
RANDOM_TASKS =["50 отжиманий", "25 бурпи", "Ходьба - 1 час", "табата 4 мин", "40 подтягиваний"]
tasks = {

}

run = True
def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print("Задача ", task, " добавлена на дату ", date)

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("На какую дату показать задачи? ")
        if date in tasks:
            for task in tasks[date]:
                print('- ',task)
        else:
            print("Нет задач на эту дату.")
    elif command == "add":
        date = input("Введи дату добавления задачи: ")
        task = input("Введите задачу дня: ")
        add_todo(date, task)
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)
    else:
        print("Нет такой команды")
        run = False