import sqlite3
connection = sqlite3.connect("banking.db")
cursor = connection.cursor()
cursor.execute("""
SELECT "balance" FROM "Card" WHERE "number"="23456789"
""")
balance = cursor.fetchall()
connection.close()
# connection.execute("""
# UPDATE "Card" SET "balance"=? WHERE "number"=?
# """, [(balance-self.price), self.number])
print(balance[0][0])