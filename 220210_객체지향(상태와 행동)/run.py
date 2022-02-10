class Man:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def buy(self, money):
        if self.money < money:
            return "비싸 안살래!"
        self.money = self.money - money
        return "좋은 거래였다."

    def sell(self, money):
        self.money = self.money + money
        return "팔아버리자."


class toss:
    def __init__(self):
        self.cost = 0
        self.name = '토스'

    def add_cost(self):
        self.cost += 1000
        return "1000원 올랐군"


kakao = 5000
naver = 4000
coupang = 3000


toss = toss()
man = Man('은찬', 10000)


# --------------------------------------------
print(f"내 이름은 {man.name}, 회사를 인수할 생각이야.")
print("------------------------")
print(f"카카오, {man.buy(kakao)}")
print(f"네이버, {man.buy(naver)}")
print(f"쿠팡, {man.buy(coupang)}")
print("------------------------")
print(f"이제 {toss.name} 사볼까?")
print(f"{toss.name}, {toss.add_cost()}")
print(f"{toss.name}, {toss.add_cost()}")
print(f"{toss.name}, 지금 {toss.cost}원 이군")
print("------------------------")
print(f"내가 가진 돈은 {man.money}원이야.")
print(f"{toss.name}, {man.buy(toss.cost)}")
print(f"카카오, {man.sell(kakao)}")
print(f"내가 가진 돈은 {man.money}원이야.")
print(f"{toss.name}, {man.buy(toss.cost)}")
print("------------------------")
print(f"회사를 모두 인수했어. 이제 {man.money}원 남았네.")
# --------------------------------------------
