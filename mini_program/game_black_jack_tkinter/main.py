import tkinter as tk
import random

card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
}
suits = ["♦", "♥", "♣", "♠"]

def deal_card():
    return f"{random.choice(list(card_values.keys()))}{random.choice(suits)}"

def calculate_score(hand):
    score = sum(card_values[card[:-1]] for card in hand)
    aces = sum(1 for card in hand if card[:-1] == "A")
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

def update_ui():
    player_label.config(text=f"Ваши карты: {', '.join(player_hand)} ({calculate_score(player_hand)} очков)")
    if game_over:
        dealer_label.config(text=f"Карты дилера: {', '.join(dealer_hand)} ({calculate_score(dealer_hand)} очков)")
    else:
        dealer_label.config(text=f"Карта дилера: {dealer_hand[0]} и ?")

def hit():
    global game_over
    if not game_over:
        player_hand.append(deal_card())
        update_ui()
        if calculate_score(player_hand) > 21:
            result_label.config(text="Перебор! Вы проиграли.", fg="red")
            game_over = True
            update_ui()

def stand():
    global game_over
    if not game_over:
        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(deal_card())
            update_ui()
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        if dealer_score > 21 or player_score > dealer_score:
            result_label.config(text="Вы победили!", fg="green")
        elif player_score == dealer_score:
            result_label.config(text="Ничья!", fg="blue")
        else:
            result_label.config(text="Дилер выиграл!", fg="red")
        game_over = True
        update_ui()

def new_game():
    global player_hand, dealer_hand, game_over
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    game_over = False
    result_label.config(text="")
    update_ui()

root = tk.Tk()
root.title("Блэкджек")

player_hand = []
dealer_hand = []
game_over = False

dealer_label = tk.Label(root, text="", font=("Arial", 14))
dealer_label.pack()

player_label = tk.Label(root, text="", font=("Arial", 14))
player_label.pack()

hit_button = tk.Button(root, text="Взять карту", command=hit, font=("Arial", 12))
hit_button.pack()

stand_button = tk.Button(root, text="Остановиться", command=stand, font=("Arial", 12))
stand_button.pack()

new_game_button = tk.Button(root, text="Новая игра", command=new_game, font=("Arial", 12))
new_game_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
result_label.pack()

new_game()

root.mainloop()