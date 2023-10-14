class 붕어빵:
    total = 0

    def __init__(self, contents, price):
        self.contents = contents
        self.price = price

    def sell(self):
        print(f"{self.contents} 붕어빵이 {self.price}원에 판매되었습니다.")
        붕어빵.total += self.price
        print(f"총 판매금: {붕어빵.total}원")

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")

슈크림_붕어빵 = 붕어빵("슈크림", 800)
팥_붕어빵 = 붕어빵("팥", 800)
김치_붕어빵 = 붕어빵("김치", 1000)

슈크림_붕어빵.sell()
슈크림_붕어빵.eat()
팥_붕어빵.sell()
팥_붕어빵.eat()
김치_붕어빵.sell()
김치_붕어빵.eat()
