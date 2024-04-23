def read(users: list[dict[str, str]]) -> None:
    for user in users[1:]:
        print(f'twój znamjomy {user["name"]} opublikował {user["post"]} posty ')


def add_user(lista: list) -> None:
    user_name = input('Podaj imię:')
    user_surname = input(' Podaj Nazwisko:')
    user_post = input('Podaj ile postów:')
    lista.append({"name": user_name, "surname": user_surname, "post": user_post})


def search(users: list[dict[str, str]]) -> None:
    user_name = input('Kogo szukasz?: ')
    for user in users[1:]:
        if user['name'] == user_name:
            print(f'Znaleziono użytkownika {user}')


def remove_user(users: list[dict[str, str]]) -> None:
    user_name = input('Kogo usunąć?: ')
    for user in users[1:]:
        if user['name'] == user_name:
            print(f'Znaleziono użytkownika {user['name']}')
            users.remove(user)


def update_user(users: list[dict[str, str]]) -> None:
    user_name = input('Kogo zaktualizować?: ')

    for user in users[1:]:
        if user['name'] == user_name:
            new_username = input('Podaj nowe imię:')
            new_surname = input('Podaj nowe nazwisko:')
            new_post = input('Podaj nową liczbę postów:')

            user['name'] = new_username
            user['surname'] = new_surname
            user['post'] = new_post