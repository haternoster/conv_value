
from converter import Rate_Converter


def main():
    source = input("Выберите валюту 'из': ")
    dest = input("Выберите валюту 'в': ")
    amount = float(input("Введите сумму: "))

    converter = Rate_Converter()
    print(f"Результат: {converter.convert(source, dest, amount)}")

if __name__ == '__main__':
    main()
