'''
오버라이딩과 오버로딩을 쉽게 풀어보자면
Overriding은 상속 내용을 덮어쓰기
Overloading은 함수가 인수에 따라 다양하게 작동하기
라고 할 수 있다.
'''


class Money:
    def introduce(self, name="익명", money=10):
        self.name = name
        self.money = money
        self.word = "어때 부럽지?"
        return f"내 이름은 {self.name}, {self.money}원을 가지고 있지. {self.word}"


object = Money()
answer1 = object.introduce(name="변덕순")
print(answer1)

answer2 = object.introduce(money=10000)
print(answer2)

answer3 = object.introduce("마동규", 5000)
print(answer3)

answer4 = object.introduce()
print(answer4)


'''
<결과>
내 이름은 변덕순, 10원을 가지고 있지. 어때 부럽지?
내 이름은 익명, 10000원을 가지고 있지. 어때 부럽지?
내 이름은 마동규, 5000원을 가지고 있지. 어때 부럽지?
내 이름은 익명, 10원을 가지고 있지. 어때 부럽지?
-----

인수로 어떤 것을 넣어도 introduce 메서드를 사용할 수 있고
거기에 따라 다양한 결과 값을 얻을 수 있다.
'''
