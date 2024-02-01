import os
import requests

def check_token_validity(token):
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get('https://id.twitch.tv/oauth2/validate', headers=headers)

    if response.status_code == 200:
        return True, None
    else:
        return False, response.status_code

def main():
    filename = 'Result.txt'
    valid_filename = 'Valid.txt'
    unvalid_filename = 'Unvalid.txt'
    log_filename = 'log.txt'

    if not os.path.exists(filename):
        print(f"Файл '{filename}' не найден")
        return

    with open(filename, 'r') as file:
        tokens = file.read().splitlines()

    valid_tokens = []
    unvalid_tokens = []

    with open(log_filename, 'w') as log_file:
        for token in tokens:
            is_valid, status_code = check_token_validity(token)
            if is_valid:
                valid_tokens.append(token)
                with open(valid_filename, 'a') as valid_file:
                    valid_file.write(token + '\n')
                log_file.write(f"Token {token} valid.\n")
                print(f"Токен {token} валид.")
            else:
                unvalid_tokens.append(token)
                with open(unvalid_filename, 'a') as unvalid_file:
                    unvalid_file.write(token + '\n')
                log_file.write(f"Token {token} unvalid.(Error code: {status_code})\n")
                print(f"Токен {token} невалид.(Код ошибки: {status_code})")

    print(f"\nРабота завершена. Всего валидных токенов: {len(valid_tokens)}\n")
    input("Нажмите 'Enter' для завершения.")


if __name__ == "__main__":
    main()
