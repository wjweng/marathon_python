import random

# project: blackjack
# create a deck of 52 cards
# jack/queen/king count as 10
# ace counts as 1 or 11
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

# create a function to randomly deal a card
# remove the card when it is drawn
def deal_card():
    card = random.choice(cards)
    cards.remove(card)
    return card

# create a function to calculate total points of the cards
def calculate_points(cards):
    total_points = sum(cards)

    # 2 cards
    if len(cards) == 2:
        return total_points

    # more than 2 cards
    if total_points > 21:
        if 11 in cards:
            cards.remove(11)
            cards.append(1)
            total_points = sum(cards)

    return total_points

def play_blackjack():
    # create lists of dealer's and user's cards
    user_cards = []
    dealer_cards = []

    # 1. deal a card to user
    # 2. deal a card to dealer
    # 3. deal another card to user
    # 4. deal another card to dealer
    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    print(f"玩家的牌：{user_cards}")
    print(f"莊家的明牌：{dealer_cards[1]}")

    # user's card
    ask_for_card = ""
    while ask_for_card != "n":
        ask_for_card = input("輸入y加牌、輸入n看結果：")

        if ask_for_card == "y":
            user_cards.append(deal_card())
            user_points = calculate_points(user_cards)
            if user_points > 21:
                ask_for_card = "n"
            else:
                print(f"玩家的牌：{user_cards}")
        elif ask_for_card == "n":
            user_points = calculate_points(user_cards)
        else:
            print("請重新輸入！輸入y加牌、輸入n看結果：")

    # dealer's cards
    dealer_points = calculate_points(dealer_cards)
    while dealer_points < 17:
        dealer_cards.append(deal_card())
        dealer_points = calculate_points(dealer_cards)

    # show cards
    print(f"玩家的牌：{user_cards}，共{user_points}點")
    print(f"莊家的牌：{dealer_cards}，共{dealer_points}點")

    # decide who wins
    if user_points > 21:
        print("你輸了!")
    elif dealer_points > 21:
        print("你贏了!")
    elif user_points == dealer_points:
        print("平手!")
    elif user_points > dealer_points:
        print("你贏了!")
    else:
        print("你輸了!")

# main program
play_game = True
print("歡迎來到21點遊戲！")
play_blackjack()

while play_game == True:
    print("=======================================")
    user_input = input("重新進行遊戲？請輸入y開始、輸入n結束：")
    if user_input == "y":
        play_blackjack()
    elif user_input == "n":
        play_game = False
        print("Bye~")
    else:
        continue
