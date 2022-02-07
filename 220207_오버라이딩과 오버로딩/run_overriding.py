'''
오버라이딩과 오버로딩을 쉽게 풀어보자면
Overriding은 상속 내용을 덮어쓰기
Overloding은 함수가 인수에 따라 다양하게 작동하기
라고 할 수 있다.
'''


class ParentMoney:
    def introduce(self, name):
        self.money = 1000
        self.name = name
        self.word = "어때 부럽지?"
        return f"내 이름은 {self.name}, {self.money}원을 가지고 있지. {self.word}"


class ChildMoney(ParentMoney):
    def introduce(self, name):
        super().introduce(name)
        self.money = 50
        self.name = name
        return f"내 이름은 {self.name}, {self.money}원을 가지고 있지. {self.word}"


parent_object = ParentMoney()
parent_answer = parent_object.introduce("김부모")
print(parent_answer)

child_object = ChildMoney()
child_answer = child_object.introduce("박자식")
print(child_answer)


'''
<결과>
내 이름은 김부모, 1000원을 가지고 있지. 어때 부럽지?
내 이름은 박자식, 50원을 가지고 있지. 어때 부럽지?
------

self.money는 기존 상속 값을 따르지 않고 50으로 수정되었지만
self.word는 상속 값을 그대로 따르는 것을 볼 수 있다.
새로 지정한 값에 대해서 기존 상속 값을 덮어쓰기 하는 것이다.
'''
