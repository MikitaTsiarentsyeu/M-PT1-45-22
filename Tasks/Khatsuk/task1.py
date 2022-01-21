def deposit(amount: 'начальная сумма'= 20_000, rate: 'годовой процент'= 15,
            period_eyars: 'срок вклада - количество лет' = 0, period_months: 'количество месяцев' = 0,
            period_days: 'количество месяцев'= 0, calc_period:'период капитализации - месяц, год, день' = 'месяц'):
    "Функция вычисляет сумму на счету в зависимости от условий депозита"
    rate /= 100
    #считаем количество периодов для капитализации и соответствующий процент
    if calc_period == 'месяц':
        periods, period_rate = 12 * period_eyars + period_months, rate / 12
    elif calc_period == 'день':
        periods, period_rate = 366 * period_eyars + 31*period_months + period_days, rate / 366
    else:
        periods, period_rate = period_eyars, rate
    #считаем по формуле сложных процентов
    amount *= (1 + period_rate)**periods
    return amount

period_list = ['месяц', 'день', 'год']
#посчитаем конечные суммы при разных периодах капитализации, остальные данные как в увсловии задачаи
for period in period_list:
    amount = divmod(deposit(period_eyars=5, calc_period=period), 1)
    print('cумма на счету {:.0f} рублей {:.0f} копеек при периоде капитализации {!s}'.format(amount[0],
            round(amount[1], 2) * 100, period))