# day07

class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 생성: ", end=' ')

    def info(self):
        print(f"{self.owner}의 포켓몬이 사용 가능한 스킬")
        for i in range(len(self.skills)):
            print(f'{i+1} : {self.skills[i]}')
#        for skill in self.skills:
#            print(skill)


    def attack(self, index):
        print(f'{self.skills[index]} 공격 시전!')

class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "피카츄"
        print(f"{self.name}")

    def attack(self, index):  # override(자식 class에서 method 재정의)
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


class Pairi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, index):
        print(f'{self.owner}의 {self.name}가 {self.skills[index]} 공격 시전!')


while True:
    menu = input('1) 포켓몬 생성 2) 프로그램 종료 : ')
    if menu == '4':
        print('프로그램을 종료합니다.')
        break;

    elif menu == '1':
        Pokemon = input('1) 피카츄 2) 꼬부기 3) 파이리 : ')

        if Pokemon == '1':
            name = input('플레이어 이름 입력 : ')
            skill = input('사용 가능한 기술 입력(/로 구분) : ')
            p = Pikachu(name, skill)

        elif Pokemon == '2':
            name = input('플레이어 이름 입력 : ')
            skill = input('사용 가능한 기술 입력(/로 구분) : ')
            p = Ggoboogi(name, skill)


        elif Pokemon == '3':
            name = input('플레이어 이름 입력 : ')
            skill = input('사용 가능한 기술 입력(/로 구분) : ')
            p = Pairi(name, skill)

        else:
            print('메뉴에서 선택해주세요.')

        info_attack = input('1) 정보 조회 2) 공격 : ')
        if info_attack == '1':
            p.info()

        elif info_attack == '2':
            p.info()
            menu_attack = int(input('공격 번호 선택 : '))
            p.attack(menu_attack - 1)

        else:
            print('메뉴에서 선택해주세요.')


    else:
        print('메뉴에서 선택해주세요.')


# pi1 = Pikachu('한지우', '번개/백만볼트')
# go1 = Ggoboogi('오바람', '고속스핀/거품/몸통박치기')

# go1.info()
# pi1.info()

# go1.attack(1)
# pi1.attack(1)

# go1.swim()  # 꼬부기 class의 객체가 사용할 수 있는 고유 method
# 피카츄가 사용할 경우 attribute error 발생

# p0 = Pokemon('아이리스', '어떤공격')
# p0.attack(0)
