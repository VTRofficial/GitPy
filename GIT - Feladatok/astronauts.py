def data_input():
    with open('astronauts.csv', 'r', encoding='utf-8') as sourcefile:
        return sourcefile.read().strip().split(',')


def select_dates():
    file = data_input()
    new_list = [date.split('\n') for date in file if '\n' in date]
    dates = []
    for n in new_list:
        if n[0] != 'Birth Date':
            dates.append(n[0])
    return dates


def select_months(dates):
    months = []
    for n in dates:
        month = [n.split('/')]
        months.append(month[0][0])
    return months


def month_calculate(months):
    pcs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for n in months:
        n = int(n)
        pcs[n - 1] += 1
    months_pcs = []
    for n in enumerate(pcs):
        months_pcs.append(n)
    sorted_months = sorted(months_pcs, key=lambda x: (x[1], x[0]), reverse=True)
    # https://www.geeksforgeeks.org/python-sorted-function/
    return sorted_months


def months_percentage(sorted_months, months):
    print('Ez a százalékos összetétele az asztronauták születési hónapjainak:')
    for e in range(3):
        n = sorted_months[e]
        print(f"{n[0] + 1}.: {round(n[1] / len(months) * 100, 1)}%")
        # https://www.geeksforgeeks.org/round-function-python/


def main():
    dates = select_dates()
    months = select_months(dates)
    sorted_months = month_calculate(months)
    months_percentage(sorted_months, months)


main()
