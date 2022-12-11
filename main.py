import datetime
import json



def save_json(path, task):
    tasks = load_json(path)
    tasks.insert(0, task)
    with open(path, "w", encoding='UTF-8') as file:
        json.dump(tasks, file, ensure_ascii=False)


def del_from_json(path, i):
    tasks = load_json(path)
    del tasks[i]
    with open(path, "w", encoding='UTF-8') as file:
        json.dump(tasks, file, ensure_ascii=False)


def replace_from_json(path, i):
    tasks = load_json(path)
    task = tasks[i]
    del tasks[i]
    tasks.insert(0, task)
    with open(path, "w", encoding='UTF-8') as file:
        json.dump(tasks, file, ensure_ascii=False)


def load_json(path):
    with open(path, "r", encoding='UTF-8') as file:
        return json.load(file)


def set_task(task_text):
    task_date = str(datetime.datetime.now()).split(" ")[0]
    return {"text": task_text, "date": task_date}


def main():
    print("Что вы хотите?\n"
          "1. Добавить задачу\n"
          "2. Посмотреть задачи\n"
          "3. Выйти")
    user_input = int(input())
    if user_input == 3:
        quit()
    elif user_input == 1:
        text = input("Введите текст задачи: \n")
        save_json(PATH, set_task(text))
    elif user_input == 2:
        tasks = load_json(PATH)
        for i in range(len(tasks)):
            print(f"{i + 1}: {tasks[i]['text']}\n"
                  f"{tasks[i]['date']}")
        user_input = int(input("0. Выход\n"
                               "Индекс для перемещения: "))
        if user_input == 0:
            quit()
        replace_from_json(PATH, user_input - 1)


if __name__ == "__main__":
    main()
