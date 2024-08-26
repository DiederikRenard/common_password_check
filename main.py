def check_password(password: str):
    with open('passwords.txt', 'r') as file:
        common_password: list[str] = file.read().splitlines()
        # print(common_password)

    for i, common_password in enumerate(common_password, start=1):
        if password == common_password:
            print(f'{password}: ❌ (#{i})')
            return

    print(f'{password}: ✅ (Unique)')


def main():
    user_password: str = input('Enter a password: ')
    if user_password.strip() == '':
        print('Please enter a valid password.')
        return main()
    check_password(user_password)


if __name__ == '__main__':
    main()