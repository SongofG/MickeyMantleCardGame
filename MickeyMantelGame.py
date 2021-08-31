#이렇게 커맨트 처리를 합니다.
#카드를 만들때 굳이 클래스를 만들 필요가 없다.
#전체적인 프로그램 구조를 잡아본다.
    #프로그램을 생각을 할 때, 오프라인에 있는 게임을 구현하는 것이기 때문에 추상화라는 과정을 거처야 한다
    #추상화는 전체적인 큰 그림을 메서드, 자료구조 등등의 단위로 쪼개는 것을 말한다.

#필요한 전역변수들
  #카드를 내는 보드들
from random import randint
class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

    def __str__(self):
        if self.num == 0:
            return "A{}".format(self.suit)
        elif self.num == 10:
            return 'J{}'.format(self.suit)
        elif self.num == 11:
            return 'Q{}'.format(self.suit)
        elif self.num == 12:
            return 'K{}'.format(self.suit)
        else:
            return '{}{}'.format(self.num + 1, self.suit)

    def __repr__(self):    #질문: 왜 __str__만 있을 때는 안되는데 __repr__가 같이 있으니까 제대로 프린트가 되는지?
        return str(self)

acard = Card(10, "S")

clubs = ["   ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
diamonds = ["   ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
hearts = ["   ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
spades = ["   ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]

player_1 = []
player_2 = []
player_3 = []
player_4 = []

#함수들
  #카드덱을 만들어 주는 함수
def CardGenerator():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    suits = ['C', 'D', 'H', 'S']
    Deck = []
    for i in suits:
        for j in numbers:
            card = Card(j, i)
            Deck.append(str(card))    #여기서 어떻게 Card Object가 바로 str()를 통해서 내가 지정한 __str__ 모양으로 변할 수 있는지?
    return Deck
  #카드를 섞어서 덱에 나눠줌
# Deck = CardGenerator()
# print(Deck)
def DistributeCard(numofplayer):
    #전 게임에서 남은 카드의 잔량을 제거 해줍니다.
    player_1.clear()
    player_2.clear()
    player_3.clear()
    player_4.clear()
    if numofplayer == "2":
        #플레이어가 세 명일 경우에는 한 사람에게 18장의 카드가 가야 하기에, 랜덤으로 18장을 가질 사람을 골라줍니다.
        Deck = CardGenerator()
        player_shuffle = [player_1, player_2, player_3]
        random_playerpick = randint(0, 2)
        for i in range(18):
            random_cardpick = randint(0, len(Deck) - 1)
            player_shuffle[random_playerpick].append(Deck[random_cardpick])
            Deck.pop(random_cardpick)
        player_shuffle.pop(random_playerpick)

        for i in player_shuffle:
            for j in range(17):
                random_cardpick = randint(0, len(Deck) - 1)
                i.append(Deck[random_cardpick])
                Deck.pop(random_cardpick)

    elif numofplayer == "3" or numofplayer == "4":
        Deck = CardGenerator()
        player_shuffle = [player_1, player_2, player_3, player_4]
        for i in player_shuffle:
            for j in range(13):
                random_cardpick = randint(0, len(Deck) - 1)
                i.append(Deck[random_cardpick])
                Deck.pop(random_cardpick)

  #보여지는 출력을 담당한 함수
def GameSummary(game_mode, num_of_player):
    print("*** Game Summary ***\n")
    if game_mode == "1":

        if num_of_player == "2":
            print("Human: ", "[%s]"%(', '.join(player_1)))
            print("Computer #1 has", len(player_2), "cards left")
            print("Computer #2 has", len(player_3), "cards left\n")

        elif num_of_player == "3":
            print("Human: ", "[%s]"%(', '.join(player_1)))
            print("Computer #1 has", len(player_2), "cards left")
            print("Computer #2 has", len(player_3), "cards left")
            print("Computer #3 has", len(player_4), "cards left\n")

        elif num_of_player == "4":
            print("Computer #1 has", len(player_1), "cards left")
            print("Computer #2 has", len(player_2), "cards left")
            print("Computer #3 has", len(player_3), "cards left")
            print("Computer #4 has", len(player_4), "cards left\n")

    elif game_mode == "2":

        if num_of_player == "2":
            print("Human:       " + "[%s]"%(', '.join(player_1)))
            print("Computer #1: " + "[%s]"%(', '.join(player_2)))
            print("Computer #2: " + "[%s]\n"%(', '.join(player_3)))

        elif num_of_player == "3":
            print("Human:       " + "[%s]"%(', '.join(player_1)))
            print("Computer #1: " + "[%s]"%(', '.join(player_2)))
            print("Computer #2: " + "[%s]"%(', '.join(player_3)))
            print("Computer #3: " + "[%s]\n"%(', '.join(player_1)))

        elif num_of_player == "4":
            print("Computer #1: " + "[%s]"%(', '.join(player_1)))
            print("Computer #2: " + "[%s]"%(', '.join(player_2)))
            print("Computer #3: " + "[%s]"%(', '.join(player_3)))
            print("Computer #4: " + "[%s]\n"%(', '.join(player_4)))

    print("Clubs:    " + "[%s]"%(", ".join(clubs)))
    print("Diamonds: " + "[%s]" % (", ".join(diamonds)))
    print("Hearts:   " + "[%s]" % (", ".join(hearts)))
    print("Spades:   " + "[%s]\n" % (", ".join(spades)))
def SeekForThePossible(player_deck):
    collect_list = []

    #Club 루프
    for i in range(len(clubs)):  # 앞에서 뒤로 검사
        if clubs[i] == "   " or clubs[i] == "  ":
            if i == 12:  # 끝 번호 인덱스 까지 검사를 했는데 아무것도 없는 경우
                collect_list.append('7C')
        else:
            if i == 0:
                pass
            else:
                if i == 1:
                    collect_list.append("AC")
                    break
                else:
                    collect_list.append(str(i) + "C")
                    break
    for i in range(len(clubs) - 1, 5, -1):  # 뒤에서 앞으로 검사
        if clubs[i] == '  ':
            pass
        else:
            if i == 9:
                collect_list.append("JC")
                break
            elif i == 10:
                collect_list.append("QC")
                break
            elif i == 11:
                collect_list.append("KC")
                break
            elif i == 12:
                if collect_list.count("AC") == 0:
                    collect_list.append("AC")
                    break
                else:
                    break
            else:
                collect_list.append(str(i + 2) + "C")
                break

    #Diamonds loop
    for i in range(len(diamonds)):    # 앞에서 뒤로 검사
        if diamonds[i] == "   " or diamonds[i] == "  ":
            if i == 12:    # 끝 번호 인덱스 까지 검사를 했는데 아무것도 없는 경우
                collect_list.append('7D')
        else:
            if i == 0:
                pass
            else:
                if i == 1:
                    collect_list.append("AD")
                    break
                else:
                    collect_list.append(str(i) + "D")
                    break
    for i in range(len(diamonds) - 1, 5, -1):    # 뒤에서 앞으로 검사
        if diamonds[i] == '  ':
            pass
        else:
            if i == 9:
                collect_list.append("JD")
                break
            elif i == 10:
                collect_list.append("QD")
                break
            elif i == 11:
                collect_list.append("KD")
                break
            elif i == 12:
                if collect_list.count("AD") == 0:
                    collect_list.append("AD")
                    break
                else:
                    break
            else:
                collect_list.append(str(i + 2) + "D")
                break

    #Hearts loop
    for i in range(len(hearts)):  # 앞에서 뒤로 검사
        if hearts[i] == "   " or hearts[i] == "  ":
            if i == 12:  # 끝 번호 인덱스 까지 검사를 했는데 아무것도 없는 경우
                collect_list.append('7H')
        else:
            if i == 0:
                pass
            else:
                if i == 1:
                    collect_list.append("AH")
                    break
                else:
                    collect_list.append(str(i) + "H")
                    break
    for i in range(len(hearts) - 1, 5, -1):  # 뒤에서 앞으로 검사
        if hearts[i] == '  ':
            pass
        else:
            if i == 9:
                collect_list.append("JH")
                break
            elif i == 10:
                collect_list.append("QH")
                break
            elif i == 11:
                collect_list.append("KH")
                break
            elif i == 12:
                if collect_list.count("AH") == 0:
                    collect_list.append("AH")
                    break
                else:
                    break
            else:
                collect_list.append(str(i + 2) + "H")
                break

    #Spades loop
    for i in range(len(spades)):  # 앞에서 뒤로 검사
        if spades[i] == "   " or spades[i] == "  ":
            if i == 12:  # 끝 번호 인덱스 까지 검사를 했는데 아무것도 없는 경우
                collect_list.append('7S')
        else:
            if i == 0:
                pass
            else:
                if i == 1:
                    collect_list.append("AS")
                    break
                else:
                    collect_list.append(str(i) + "S")
                    break
    for i in range(len(spades) - 1, 5, -1):  # 뒤에서 앞으로 검사
        if spades[i] == '  ':
            pass
        else:
            if i == 9:
                collect_list.append("JS")
                break
            elif i == 10:
                collect_list.append("QS")
                break
            elif i == 11:
                collect_list.append("KS")
                break
            elif i == 12:
                if collect_list.count("AS") == 0:
                    collect_list.append("AS")
                    break
                else:
                    break
            else:
                collect_list.append(str(i + 2) + "S")
                break

    # 이제 여기다가 위에 검사를 통해서 받은 카드들과 현재 플레이어가 가지고 있는 카드를 비교
    # 그리고 겹치는 것들만 살려서 실제로 낼 수 있는 카드만 리턴
    result_list = []
    for i in range(len(collect_list)):
        for j in range(len(player_deck)):
            if collect_list[i] == player_deck[j]:
                result_list.append(player_deck[j])
            else:
                pass

    return result_list
def GameOverCheck(bot_num):
    if bot_num == 2:
        if len(player_1) == 0:
            print('GAME OVER - Human is the Winner!')
            return False
        elif len(player_2) == 0:
            print('GAME OVER - Computer #1 is the Winner!')
            return False
        elif len(player_3) == 0:
            print('GAME OVER - Computer #2 is the Winner!')
            return False
    elif bot_num == 3:
        if len(player_1) == 0:
            print('GAME OVER - Human is the Winner!')
            return False
        elif len(player_2) == 0:
            print('GAME OVER - Computer #1 is the Winner!')
            return False
        elif len(player_3) == 0:
            print('GAME OVER - Computer #2 is the Winner!')
            return False
        elif len(player_4) == 0:
            print('GAME OVER - Computer #3 is the Winner!')
            return False
    elif bot_num == 4:
        if len(player_1) == 0:
            print('GAME OVER - Computer #1 is the Winner!')
            return False
        elif len(player_2) == 0:
            print('GAME OVER - Computer #2 is the Winner!')
            return False
        elif len(player_3) == 0:
            print('GAME OVER - Computer #3 is the Winner!')
            return False
        elif len(player_4) == 0:
            print('GAME OVER - Computer #4 is the Winner!')
            return False
def GameRunning(bot_num):
    game_end = True  # 게임 루프 끝내는 조건
    if bot_num == "2":
        while game_end == True:
            #사람 차례.
            MyTurn = SeekForThePossible(player_1)
            if len(SeekForThePossible(player_1)) == 0:
                print('YOU HAVE NO CARDS THAT CAN BE PLAYED \nYOUR TURN WILL BE SKIPPED')
                GameSummary(menu_input, bot_num)
                input("<ENTER to Continue>")
                game_end = GameOverCheck(bot_num)
            else:
                random_card_index = randint(0, len(SeekForThePossible(player_1)) - 1)  # 낼 수 있는 카드 중에서 랜덤으로 하나를 return 해준다.
                random_card = SeekForThePossible(player_1)[random_card_index]
                print('Enter a Card to Play,')
                print('X to Quit, or')
                print('R to Randomly Choose a Card: ' + random_card)
                user_choice = input()
                if user_choice == 'X' or user_choice == 'x':
                    print("Thank you for play. Good bye.")
                    game_end = False
                elif user_choice == "R" or user_choice == 'r':
                    #Clubs
                    if random_card[len(random_card) - 1] == 'C':
                        if random_card[0] == 'A':    # 여기 앞에다 A 넣을지 뒤에다 넣을지 if로 처리 해줘야함.
                            clubs[0] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == '1':
                            clubs[9] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == 'J':
                            clubs[10] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == 'Q':
                            clubs[11] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == 'K':
                            clubs[12] = random_card
                            player_1.remove(random_card)
                        else:
                            clubs[int(random_card[0]) - 1] = random_card
                            player_1.remove(random_card)

                    #Diamonds
                    elif random_card[len(random_card) - 1] == 'D':
                        if random_card[0] == 'A':    # 여기 앞에다 A 넣을지 뒤에다 넣을지 if로 처리 해줘야함.
                            diamonds[0] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == '1':
                            diamonds[9] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == 'J':
                            diamonds[10] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == 'Q':
                            diamonds[11] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == 'K':
                            diamonds[12] = random_card
                            player_1.remove(random_card)
                        else:
                            diamonds[int(random_card[0]) - 1] = random_card
                            player_1.remove(random_card)

                    #Hearts
                    elif random_card[len(random_card) - 1] == 'H':
                        if random_card[0] == 'A':    # 여기 앞에다 A 넣을지 뒤에다 넣을지 if로 처리 해줘야함.
                            hearts[0] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == '1':
                            hearts[9] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == 'J':
                            hearts[10] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == 'Q':
                            hearts[11] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == 'K':
                            hearts[12] = random_card
                            player_1.remove(random_card)
                        else:
                            hearts[int(random_card[0]) - 1] = random_card
                            player_1.remove(random_card)

                    #Spades
                    elif random_card[len(random_card) - 1] == 'S':
                        if random_card[0] == 'A':    # 여기 앞에다 A 넣을지 뒤에다 넣을지 if로 처리 해줘야함.
                            spades[0] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == '1':
                            spades[9] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == 'J':
                            spades[10] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == 'Q':
                            spades[11] = random_card
                            player_1.remove(random_card)
                        elif random_card[0] == 'K':
                            spades[12] = random_card
                            player_1.remove(random_card)
                        else:
                            spades[int(random_card[0]) - 1] = random_card
                            player_1.remove(random_card)
                #여기다가 else로 뭐를 넣든지 result_list 랑 비교해서 엔터 칠 수 있게 기능 만들어야 한다!


menu_loop = True
# 메뉴 게임 루
while menu_loop == True:
    print("*** Welcome to Haein Park's Implementation of the Mickey Mantle Card Game ***" + "\n")
    print("Main Menu")
    print("1) New Game")
    print("2) New Game in Cheat Mode")
    print("3) View Stats")
    print("Q) Exit")

    menu_input = input("Enter: ")
    # 치트가 없는 게임
    if menu_input == "1":
        bot_num = input("\nHow many AI players (2-4)? ")
        DistributeCard(bot_num)
        print("\n")
        #여기에 게임 루프가 들어와야 함.
        GameSummary(menu_input, bot_num)
        game_end = True    # 게임 루프 끝내는 조건
        while game_end == True:
            MyTurn = SeekForThePossible(player_1)
            if len(SeekForThePossible(player_1)) == 0:
                print('YOU HAVE NO CARDS THAT CAN BE PLAYED \nYOUR TURN WILL BE SKIPPED')
                GameSummary(menu_input, bot_num)
                input("<ENTER to Continue>")
                game_end = GameOverCheck(bot_num)
            else:
                random_card_index = randint(0, len(SeekForThePossible(player_1)) - 1)   # 낼 수 있는 카드 중에서 랜덤으로 하나를 return 해준다.
                random_card = SeekForThePossible(player_1)[random_card_index]
                print('Enter a Card to Play,')
                print('X to Quit, or')
                print('R to Randomly Choose a Card: ' + random_card)
                user_choice = input()
                if user_choice == 'X' or user_choice == 'x':
                    print("Thank you for play. Good bye.")
                    game_end = False
                elif user_choice == "R" or user_choice == 'r':
                    if random_card[len(random_card) - 1] == 'C':
                        if random_card[0] == 'A':
                            clubs[0] = random_card
                            player_1.remove(random_card)

        menu_loop = False

    # 치트가 있는 게임: 상대방이 무슨 패를 가지고 있는지 보여줌
    elif menu_input == "2":
        bot_num = input("\nHow many AI players (2-4)? ")
        DistributeCard(bot_num)
        print("\n")
        GameSummary(menu_input, bot_num)
        menu_loop = False

    # 기록 전산표
    elif menu_input == "3":
        print("functionality being ready" + "\n")

    # 게임을 종료
    elif menu_input == "Q" or menu_input == "q":
        print("Thank you for play. Good bye.")
        menu_loop = False

    # 지정된 키 외에 다른 것을 입력할 때를 위해서 있는 조건문
    else:
        print("invalid input. Please try again" + "\n")