# 문제 7. 오른쪽과 같은 실행결과가 나오도록 왼쪽 코드의 Fighter 클래스를 수정하시오.
# F-22 출격!
# 공대공미사일 발사!
# 폭탄 투하!

class Fighter(object):
    def __init__(self, model, missile, b):
        self.model = model
        self.missile = missile
        self.b = b

    def attack(self):
        print(self.model + " 출격!")

    def fire(self):
        print(self.missile + " 발사!")

    def bomb(self):
        print(self.b + " 투하!")

fighter = Fighter("F-22", "공대공미사일", "폭탄")
fighter.attack()
fighter.fire()
fighter.bomb()

