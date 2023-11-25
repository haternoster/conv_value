from converter import ConverterInterface
from converter import ConverterImpl


def main():
    pass

    source = input("Выберите валюту 'из': ")
    dest = input("Выберите валюту 'в': ")
    amount = float(input("Введите сумму: "))

    converter = ConverterImpl()
    print(f"Результат: {converter.convert(source, dest, amount)}")


if __name__ == '__main__':
    main()
