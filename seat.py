import sqlite3


class Seat:

    database = "cinema.db"

    def __init__(self, database, seat_id):
        self.seat_id = seat_id
        self.database = database

    def get_price(self):
        connection = sqlite3.connect(database=self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "price" FROM "Seat" WHERE "seat_id"=?
        """, [self.seat_id])
        price = cursor.fetchall()[0][0]
        connection.close()
        return price

    def is_free(self):
        connection = sqlite3.connect(database=self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id"=?
        """, [self.seat_id])
        result = cursor.fetchall()[0][0]
        if result == 1:
            connection.close()
            return False
        else:
            connection.close()
            return True

    def occupy(self):
        connection = sqlite3.connect(database=self.database)
        connection.execute("""
        UPDATE "Seat" SET "taken"=1 WHERE "seat_id"=?
        """, [self.seat_id])
        connection.commit()
        connection.close()
