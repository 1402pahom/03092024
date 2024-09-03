first=int(input('Введите первое число: '))
seconds=int(input('Введите второе число: '))
third=int(input('Введите третье число: '))
if first==seconds and seconds==third:
    print(3)
elif first==seconds or first==third or seconds==third:
    print(2)
elif first!=seconds and seconds!=third:
    print(0)
