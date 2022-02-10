import sqlite3

class Card():

    database = "banking.db"

    def __init__(self, type, number, cvc, holder):
        self.holder = holder
        self.cvc = cvc
        self.number = number
        self.type = type

    def get_balance(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
                SELECT "balance" FROM "Card" WHERE "number"=?
                """, [self.number])
        balance = cursor.fetchall()[0][0]
        connection.close()
        return balance

    def validate(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
                        SELECT "number" FROM "Card" WHERE "holder"=?
                        """, [self.holder])
        number_checker = cursor.fetchall()[0][0]  # TODO: improve this checking method
        if number_checker == self.number:
            return True
        else:
            return False

    def checkout(self, seat_price):
        self.seat_price = seat_price
        connection = sqlite3.connect(self.database)
        connection.execute("""
        UPDATE "Card" SET "balance"=? WHERE "number"=?
        """, [self.get_balance()-self.seat_price,self.number])
        connection.commit()
        connection.close()