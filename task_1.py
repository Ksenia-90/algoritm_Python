from collections import defaultdict


companies = defaultdict()
company = int(input("Введите количество предприятий: "))

while company:
    name = input("Введите название предприятия: ")
    companies[name] = float(input("Введите годовую прибыль предприятия: "))
    company -= 1


average_profit = sum(companies.values()) / len(companies)

print(f"Среднегодовая прибыль {len(companies)} предприятий составляет {average_profit} руб")

for name, profit in companies.items():
    if profit < average_profit:
        print(f"Предприятие {name} имеет доход ниже среднегодового")
    elif profit > average_profit:
        print(f"Предприятие {name} имеет доход выше среднегодового")
