import random
import time


class Player:
    cards = '가위', '바위', '보'

    def __init__(self, name, energy):
        self.__name = name
        self.__energy = energy

    def name(self):
        return self.__name

    def energy(self):
        return self.__energy

    def status(self):
        print('{}의 남은 에너지: {}'.format(self.__name, self.__energy))

    # 가위, 바위, 보 중 임의로 선택
    def pick(self):
        return random.choice(Player.cards)

    def lose(self):
        # 패배했을때 에너지 하나 차감
        self.__energy -= 1
        # 남은 에너지가 0보다 작아지지 않도록
        self._energy = self.__energy if self.__energy > 0 else 0


def play(pick1, pick2):
    '''
    0 => 무승부
    1 => 첫 번째 선수 승
    2 => 두 번째 선수 승
    '''
    to_number = {'가위': -1, '바위': 0, '보': 1}
    pick1 = to_number[pick1]
    pick2 = to_number[pick2]

    if pick1 == pick2:
        return 0
    elif pick1 * pick2 == 0:
        return 1 if pick1 > pick2 else 2
    else:
        return 1 if pick1 < pick2 else 2

# --------------------------게임 시작------------------------


player1 = Player('네오', 3)
player2 = Player('무지', 3)

player1.status()
player2.status()

# 게임 횟수 기록
count = 0

# 선수중 한명이 에너지가 0이 아닐 경우
while player1.energy() * player2.energy() != 0:
    count += 1
    print("[ {}회차 게임 ]".format(count))

    pick1, pick2 = player1.pick(), player2.pick()

    print('| {0}({1})=>{2:2} vs {5:2}<={3}({4}) |'.format(
        player1.name(), player1.energy(), pick1,
        player2.name(), player2.energy(), pick2
    ))
    # 2:2 에서 :2 는 뭐지? =>2자리 공간확보(숫자 그대로의 의미)
    # 2:2, 5:2

    winner = play(pick1, pick2)
    if winner == 1:
        player2.lose()
        print("> {}의 승리!".format(player1.name()))
    elif winner == 2:
        player1.lose()
        print("> {}의 승리!".format(player2.name()))
    else:
        print("> 무승부!")

    time.sleep(2)
    print()

    if player1.energy() == 0:
        print("!!! {}회의 승부 끝에 {}의 승리!!!".format(count, player2.name()))
    else:
        print("!!! {}회의 승부 끝에 {}의 승리!!!".format(count, player1.name()))
