import random

MIN_NUMBER: int = 1
MAX_NUMBER: int = 100
MAX_ATTEMPTS: int = 10

# Генерирует случайное целое число в заданном диапазоне
def generate_secret_number(min_val: int, max_val: int) -> int:
    return random.randint(min_val, max_val)

# Запрашивает у пользователя число и проверяет ввод.
# Повторяет запрос до получения корректного значения в диапазоне.
def read_user_guess(min_val: int, max_val: int) -> int:
    while True:
        user_input = input(f"Введите число от {min_val} до {max_val}: ")

        try:
            guess = int(user_input)
        except ValueError:
            print("Ошибка: нужно ввести целое число без посторонних символов.")
            continue

        if guess < min_val or guess > max_val:
            print(f"Ошибка: число должно находиться в диапазоне от {min_val} до {max_val}.")
            continue

        return guess

# Сравнивает предположение пользователя с загаданным числом
# Возвращает строку-результат: 'correct', 'too_low', 'too_high'
def check_guess(guess: int, secret: int) -> str:
    if guess == secret:
        return "correct"
    elif guess < secret:
        return "too_low"
    else:
        return "too_high"

# Основная логика игры
def play_game() -> None:
    secret_number = generate_secret_number(MIN_NUMBER, MAX_NUMBER)
    attempts_left = MAX_ATTEMPTS

    print(f"\n=== Игра 'Угадай число' ===")
    print(f"Я загадал число от {MIN_NUMBER} до {MAX_NUMBER}.")
    print(f"У вас есть {MAX_ATTEMPTS} попыток. Удачи!\n")

    while attempts_left > 0:
        print(f"[Осталось попыток: {attempts_left}]")
        guess = read_user_guess(MIN_NUMBER, MAX_NUMBER)
        result = check_guess(guess, secret_number)

        if result == "correct":
            print(f"\nПоздравляю! Вы угадали число {secret_number}.")
            print(f"Потрачено попыток: {MAX_ATTEMPTS - attempts_left + 1}.")
            return

        elif result == "too_low":
            print("Слишком маленькое число. Попробуйте больше.\n")
        else:
            print("Слишком большое число. Попробуйте меньше.\n")

        attempts_left -= 1

    print(f"\nК сожалению, попытки закончились.")
    print(f"Загаданное число было: {secret_number}.")


def main() -> None:
    try:
        play_game()
    except (KeyboardInterrupt, EOFError):
        print("\nИгра прервана пользователем. До встречи!")


if __name__ == "__main__":
    main()