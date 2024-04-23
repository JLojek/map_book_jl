from models.data import users
from utils.crud import read, add_user, search, update_user

if __name__ == '__main__':
    print(f'witaj {users[0]["name"]}')

    while True:

        print('0. Zakończ program')
        print('1. Wyświetl znajomych')
        print('2. Dodaj znajomego')
        print('3. Usuń znajomego ')
        print('4. Szukaj znajomego ')
        print('5. Kogo zaktualizować? ')
        menu_option = input('Wybierz opcje menu:')
        if menu_option == '0': break
        if menu_option == '1': read(users)
        if menu_option == '2': add_user(users)
        if menu_option == '4': search(users)
        if menu_option == '3': remove_user(users)
        if menu_option == '5': update_user(users)
