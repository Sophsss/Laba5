import requests

# Перед запуском этой программы запустить main.py!
if __name__ == '__main__':
    HOST = "localhost"
    PORT = 8081

    inWork = True
    print("Варианты действий: \n"
          "1 - создание заметки \n"
          "2 - чтение заметки \n"
          "3 - удаление заметки \n"
          "4 - обновление заметки \n"
          "5 - вывод списка id заметок \n"
          "6 - информация о времени создания/обновления \n"
          "7 - Прервать программу\n")

    while inWork:
        choice = int(input("Введите номер действия: "))
        if choice == 1:
            text = input("Введите text: ")
            token = input("Введите token: ")
            response = requests.post(f"http://{HOST}:{PORT}/create_note", params={"text": text, "token": token})
            print(response.text)
            print("Код состояния: ", response.status_code)

        elif choice == 2:
            id = input("Введите id: ")
            token = input("Введите token: ")
            response = requests.get(f"http://{HOST}:{PORT}/read_note", params={"id": id, "token": token})
            print(response.text)
            print("Код состояния: ", response.status_code)

        elif choice == 3:
            id = input("Введите id: ")
            token = input("Введите token: ")
            response = requests.delete(f"http://{HOST}:{PORT}/delete_note", params={"id": id, "token": token})
            print("Код состояния: ", response.status_code)

        elif choice == 4:
            id = input("Введите id: ")
            text = input("Введите text: ")
            token = input("Введите token: ")
            response = requests.put(f"http://{HOST}:{PORT}/update_note", params={"id": id, "text": text, "token": token})
            print("Код состояния: ", response.status_code)

        elif choice == 5:
            token = input("Введите token: ")
            response = requests.get(f"http://{HOST}:{PORT}/list_note", params={"token": token})
            print(response.text)
            print("Код состояния: ", response.status_code)

        elif choice == 6:
            id = input("Введите id: ")
            token = input("Введите token: ")
            response = requests.get(f"http://{HOST}:{PORT}/info_note", params={"id": id, "token": token})
            print(response.text)
            print("Код состояния: ", response.status_code)

        elif choice == 7:
            inWork = False

        else:
            print("Wrong choice")