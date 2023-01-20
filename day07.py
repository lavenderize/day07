# day07

class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 생성: ", end=' ')

    def info(self):
        print(f"{self.owner}의 포켓몬이 사용 가능한 스킬")
        for skill in self.skills:
            print(skill)

#    def attack(self, index):
#        print(f'{self.skills[index]} 공격 시전!')

class Pikachu(Pokemon):     # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "피카츄"
        print(f"{self.name}")


    def attack(self, index):    # override(자식 class에서 method 재정의)
        print(f'{self.owner}의 {self.name}가 {self.skills[index]} 공격 시전!')


class Ggoboogi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f"{self.name}")


    def attack(self, index):
        print(f'{self.owner}의 {self.name}가 {self.skills[index]} 공격 시전!')

    def swim(self):
        print(f'{self.name}가 수영을 합니다')

pi1 = Pikachu('한지우', '번개/백만볼트')
go1 = Ggoboogi('오바람', '고속스핀/거품/몸통박치기')

# go1.info()
# pi1.info()

go1.attack(1)
pi1.attack(1)

go1.swim()  # 꼬부기 class의 객체가 사용할 수 있는 고유 method
            # 피카츄가 사용할 경우 attribute error 발생

# p0 = Pokemon('아이리스', '어떤공격')
# p0.attack(0)

