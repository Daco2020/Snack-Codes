'''
오버라이딩과 오버로딩을 쉽게 풀어보자면,

Overriding은 덮어쓰기
Overloding은 여러방법으로 사용하기
'''


class ParentMoney:
    def introduce(self, name='익명', money='10'):
        self.money = money
        self.name = name
        self.word = "어때 부럽지?"
        return f"내 이름은 {name}, {self.money}원을 가지고 있지. {self.word}"


class ChildMoney(ParentMoney):
    def introduce(self, name):
        super().introduce(name)
        self.money = 50
        self.name = name
        return f"내 이름은 {name}, {self.money}원을 가지고 있지. {self.word}"


parent_object = ParentMoney()
parent_answer = parent_object.introduce("김부모")
print(parent_answer)

child_object = ChildMoney()
child_answer = child_object.introduce("박자식")
print(child_answer)
