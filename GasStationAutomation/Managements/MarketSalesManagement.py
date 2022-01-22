from Database import DatabaseContext

def List():
    cursor = DatabaseContext.connect.cursor()
    cursor.execute("SELECT * FROM dbo_MarketSales")
    rows = cursor.fetchall()

    for row in rows:
        print(f"""
        Id {row[0]},
        Product {row[1]},
        Number {row[2]},
        Price {row[3]}
        *************************************
        """)

def Create(productId,number,price):
    cursor = DatabaseContext.connect.cursor()
    cursor.execute("INSERT INTO dbo_MarketSales(ProductId,Number,Price) VALUES({},{},{});".format(productId,number,price))
    DatabaseContext.connect.commit()

def Remove(Id):
    if Id != None:
        cursor = DatabaseContext.connect.cursor()
        cursor.execute("DELETE FROM dbo_MarketSales WHERE Id = {};".format(Id))
    else:
        print("Id cannot be null!")