amount_due = 50

print("Amount Due:", amount_due)

insert_coin = 0

amount_received = 0

while insert_coin < amount_due:
    insert_coin = int(input(f"Insert Coin: "))
    if insert_coin == 5 or insert_coin == 10 or insert_coin == 25:
        amount_received += insert_coin
        current_amount_due = amount_due - amount_received
        if amount_received < amount_due:
            print(f"Amount Due: {current_amount_due}")
        elif amount_received >= amount_due:
            change_owed = amount_received - amount_due
            print(f"Change Owed: {change_owed}")
            break
    else:
        print("Amount Due:", amount_due)
        continue



