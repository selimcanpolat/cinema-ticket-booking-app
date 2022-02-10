from card import Card
from seat import Seat
from ticket import Ticket
from user import User
from id import ticket_id_generator

name_input = input("Name: ")
user_obj = User(name_input)

seat_id_input = input("Seat ID: ")
seat_obj = Seat("cinema.db", seat_id_input)


if not seat_obj.is_free():
    print(f"{seat_obj.seat_id} is occupied. Try another seat. ")
else:
    print("Seat is available.\n")
    card_type_input = input("Card Type: ")
    card_no_input = input("Card Number: ")
    CVC_input = input("CVC: ")
    cardholder_name_input = input("Cardholder name: ")

    card_obj = Card(card_type_input, card_no_input,
                    CVC_input, cardholder_name_input)

    if card_obj.validate():
        print("Card validated.")
        print("Checking balance...")
        if card_obj.get_balance() >= seat_obj.get_price():
            print("Purchasing...")
            user_obj.buy(seat_obj, card_obj)
            print("Success!")
            print(f"{seat_obj.get_price()} has been withdrawn from your account.")
            print("Generating your ticket PDF...")
            ticket_obj = Ticket(ticket_id_generator(), user_obj.name, seat_obj.get_price(), seat_obj.seat_id)
            ticket_obj.to_pdf(path="")
            print("Your digital ticket is ready.")
        else:
            print("Insufficient funds.")

    else:
        print("Incorrect credentials. Please enter valid card information.")


