deck = input().split(' ')
shuffles = int(input())
shuffled_deck = []
count = 0
while count != shuffles:
    shuffled_deck = []
    shuffled_deck.append(deck[0])
    for i in range(int(len(deck) / 2 - 1)):
        shuffled_deck.append(deck[int(len(deck) / 2) + i])
        shuffled_deck.append(deck[i + 1])
    shuffled_deck.append(deck[len(deck) - 1])
    deck = shuffled_deck
    count += 1
print(shuffled_deck)
