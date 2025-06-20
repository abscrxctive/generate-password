from random import shuffle

def generate_password(len_password: int) -> str:
    password_symbols = list('0123456789abcdefghjklmnopqrstyvwxyzABCDEFGHJKLMNOPQRSTUVWZYZ!@#$%^&*()?>:')
    shuffle(password_symbols)

    while len_password < 12 or len_password > 32:
        if len_password < 12:
            print('Пароль должен быть не менее 12 символов')
        elif len_password > 32:
            print('Пароль должен быть не более 32 символов')

        len_password = abs(int(input('Введите длину пароля: ')))

    return ''.join(password_symbols[:len_password])

length_password = abs(int(input('Введите длину пароля: ')))
print(generate_password(length_password))
