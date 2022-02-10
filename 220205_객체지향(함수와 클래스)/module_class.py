class 카르텔멤버:
    def __init__(self):
        self.카르텔멤버리스트 = []

    def 멤버모두추가해줘(self, 멤버리스트):
        for 멤버 in 멤버리스트:
            self.카르텔멤버리스트.append(멤버)

    def 근무지알려줘(self, 이름):
        근무지 = "''"
        for i in self.카르텔멤버리스트:
            if i['이름'] == 이름:
                근무지 = i.get('근무지')
        return f"{이름}님의 근무지는 {근무지}입니다."

    def 이름알려줘(self, 근무지):
        이름 = "''"
        for i in self.카르텔멤버리스트:
            if i['근무지'] == 근무지:
                이름 = i.get('이름')
        return f"{근무지}에 계신 분은 {이름}님 입니다."
