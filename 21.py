import random


def init():
    deck = [1,2,3,4,5,6,7,8,9,10,11]
    pl_cards = random.choice(deck)
    deck.remove(pl_cards)
    dl_cards = random.choice(deck)
    deck.remove(dl_cards)
    return deck, pl_cards, dl_cards

def pl_turn(pl_cards, deck):
    print("Сумма карт =", pl_cards)
    pl_ch = int(input("Взять карту - 1, Пас - 2: "))
    if pl_ch == 1:
        pl_card = random.choice(deck)
        pl_cards += pl_card
        deck.remove(pl_card)
        return True, pl_cards, deck
    else:
        return False, pl_cards, deck

def dl_turn(dl_cards, deck):
    if dl_cards < 17:
        dl_card = random.choice(deck)
        dl_cards += dl_card
        deck.remove(dl_card)
        return True, dl_cards, deck
    else:
        return False, dl_cards, deck

deck = []
pl_cards = 0
dl_cards = 0

print("играем 21 нах")
deck, pl_cards, dl_cards = init()

# Ход игрока
while True:
    if pl_cards > 21:
        break
    continue_pl, pl_cards, deck = pl_turn(pl_cards, deck)
    if not continue_pl or not deck:
        break

# Ход дилера (только если игрок не перебрал)
if pl_cards <= 21:
    while dl_cards < 17 and deck:
        continue_dl, dl_cards, deck = dl_turn(dl_cards, deck)
        if not deck:
            break

# Определение результата
if (pl_cards > 21 and dl_cards > 21) or (pl_cards == dl_cards):
    print('ничья нах')
elif pl_cards > 21:
    print(f'ты проиграл нах, у тебя больше 21')
elif dl_cards > 21 or pl_cards > dl_cards:
    print('ты выиграл нах')
else:
    print('ты проиграл нах')
print(f'у тебя маленького {pl_cards}')
print(f'а у дилера ебаного {dl_cards}')