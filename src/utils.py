def money_sum(datas=[0]):
    money = {"earn":0, "expeness":0}
    earn=[]
    exp=[]
    for data in datas:
        if data[-1] == 0:
            money['expeness'] += int(data[0])
            exp.append(data)
        elif data[-1] == 1:
            money['earn'] += int(data[0])
            earn.append(data)
        else:
            print('Wrong data in db')
    return money,earn,exp


