
import moneny


def select():
    send_money = moneny.send_money
    if send_money == True:
        print("发了1000，现在存款2000块了")
    else:
        print("只有存款1000块")