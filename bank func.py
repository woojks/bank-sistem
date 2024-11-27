def register_user(users):
    login = input('Пожалуйста, введите логин: >>> ')
    name = input('Пожалуйста, введите своё имя: >>> ')
    phone = input('Пожалуйста, введите номер телефона: >>> ')
    password = input('Создайте пароль: >>> ')
    password1 = input('Повторите свой пароль: >>> ')
    
    while password != password1 or len(password) < 8:
        password = input('Создайте пароль не менее 8 символов: >>> ')
        password1 = input('Повторите свой пароль: >>> ')
    
    users[login] = {
        'name': name,
        'phone': phone,
        'balance': 100,
        'password': password
    }
    
    print('Вы успешно зарегистрированы ')
    return login


def login_user(users):
    login = input('Введите свой логин: >>> ')
    password = input('Введите пароль: >>> ')
    
    if login in users and password == users[login]['password']:
        print('Вы прошли верификацию ')
        return login
    else:
        print('Неверный логин или пароль ')
        return None


def transfer_balance(users, current_user):
    recipient_login = input('Введите логин получателя  ')
    amount = int(input('Введите сумму перевода  '))
    
    if recipient_login in users:
        if amount <= users[current_user]['balance']:
            users[current_user]['balance'] -= amount
            users[recipient_login]['balance'] += amount
            print('Перевод выполнен успешно ')
        else:
            print('У вас недостаточно средств для перевода ')
    else:
        print('Пользователь не найден ')


def display_user_info(users, current_user):
    user_info = users[current_user]
    print(f'''
    Имя: {user_info['name']}
    Логин: {current_user}
    Баланс: {user_info['balance']}
    ''')


def display_phone_number(users, current_user):
    if current_user is not None:
        print('Номер телефона:', users[current_user]['phone'])
    else:
        print('Сначала авторизуйтесь, чтобы узнать номер телефона ')


def main():
    users = {
        'Endless': {
            'phone': '+996999090998',
            'name': 'marselle',
            'balance': 999999,
            'password': 'endlesskey'
        },
        'zerotwo': {
            'phone': '+996555666777',
            'name': 'Zerotwo',
            'balance': 499999,
            'password': 'zerotwo'
        }
    }

    userSession = None

    while True:
        if userSession is not None:
            print(f'Здравствуйте, уважаемый клиент {users[userSession]["name"]} ')

        m = input('''
        1 >>> Зарегистрироваться
        2 >>> Авторизоваться
        3 >>> Перевод баланса
        4 >>> Список пользователей
        5 >>> Информация
        6 >>> Номер телефона
        7 >>> Выйти

        >>> ''')

        if m == '1':
            userSession = register_user(users)
        elif m == '2':
            if userSession is None:
                userSession = login_user(users)
            else:
                print('Вы уже авторизованы')
        elif m == '3':
            if userSession is not None:
                transfer_balance(users, userSession)
            else:
                print('Сначала авторизуйтесь, а потом переводите деньги')
        elif m == '4':
            print(users)
        elif m == '5':
            if userSession is not None:
                display_user_info(users, userSession)
            else:
                print('Сначала авторизуйтесь, чтобы получить информацию')
        elif m == '6':
            display_phone_number(users, userSession)
        elif m == '7':
            userSession = None
            print('Вы вышли из авторизации ')
        else:
            print('Неверный ввод ')

if __name__ == '__main__':
    main()
