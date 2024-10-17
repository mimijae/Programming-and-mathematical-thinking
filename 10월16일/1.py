# 다음과 같이 문자열이 출력되도록 Fighter 클래스의 초기화 함수 init을 수정하고,
# bomb 메서드를 추가하시오.
# ... # 생략된 부분
# fighter = Fighter('F-22", "공대공미사일", "폭탄")
# fighter.attack()
# fighter.fire()
# fighter.bomb()
# >>> python my_code20.py
# F-22 출격!
# 공대공미사일 발사!
# 폭탄 투하!

class Fighter:
    def __init__(self, name, missile, bomb):
        self.name = name
        self.missile = missile
        self.bomb_type = bomb
    
    def attack(self):
        print(f'{self.name} 출격!')

    def fire(self):
        print(f'{self.missile} 발사!')

    def bomb(self):
        print(f'{self.bomb_type} 투하!')

fighter = Fighter('F-22', '공대공미사일', '폭탄')
fighter.attack()
fighter.fire()
fighter.bomb()
