class Carpbread:
    def __init__(self, name, price2):
        self.contents = name
        self.price = price2
        self.total = 0

    def sell(self):

        print(self.contents + "붕어빵이 판매 되었습니다.")

cream_carpbread = Carpbread("슈크림", 1000)
redbean_carpbread = Carpbread("팥", 1000)

#print(cream_carpbread.contents, cream_carpbread.price)
#print(redbean_carpbread.contents, redbean_carpbread.price)

cream_carpbread.sell()
redbean_carpbread.sell()




