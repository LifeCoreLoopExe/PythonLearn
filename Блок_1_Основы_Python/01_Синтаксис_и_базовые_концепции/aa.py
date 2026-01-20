# def create_business_card():
#     name = input("Введите ваше имя: ")
#     position = input("Введите вашу должность: ")
#     company = input("Введите название компании: ")
#     email = input("Введите email: ")
#     phone = input("Введите номер телефона: ")
#
#     width = 40
#     border = "*" * width
#
#     card_content = (
#         f"\n{border}\n"
#         f"*{'Имя: ' + name: <36} *\n"
#         f"*{'Должность: ' + position: <36} *\n"
#         f"*{'Компания: ' + company: <36} *\n"
#         f"*{'Email: ' + email: <36} *\n"
#         f"*{'Телефон: ' + phone: <36} *\n"
#         f"{border}\n"
#     )
#
#
#     print(card_content)
#
#
#
# create_business_card()










# USD_RATE = 90.0
# EUR_RATE = 100.0
# CNY_RATE = 12.5
#
#
# def convert_currencies(rubles):
#     usd = rubles / USD_RATE
#     eur = rubles / EUR_RATE
#     cny = rubles / CNY_RATE
#     return usd, eur, cny
#
#
# def main():
#     try:
#
#         rubles = float(input("Введите сумму в рублях: "))
#
#
#         usd, eur, cny = convert_currencies(rubles)
#
#         print("\nКонвертация валют:")
#         print(f"{'Валюта':<10}{'Курс':<10}{'Сумма':<10}")
#         print("-" * 30)
#         print(f"{'Рубль':<10}{'-':<10}{rubles:,.2f} ₽")
#         print(f"{'Доллар':<10}{USD_RATE:,.2f} ₽<{usd:,.2f} $")
#         print(f"{'Евро':<10}{EUR_RATE:,.2f} ₽<{eur:,.2f} €")
#         print(f"{'Юань':<10}{CNY_RATE:,.2f} ₽<{cny:,.2f} ¥")
#
#     except ValueError:
#         print("Ошибка: введите числовое значение!")
#
#
# if __name__ == "__main__":
#     main()