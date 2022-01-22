from Database import DatabaseContext

def List():
    cursor = DatabaseContext.connect.cursor()
    cursor.execute("SELECT * FROM dbo_MarketProducts")
    rows = cursor.fetchall()

    for row in rows:
        print(f"""
        Id {row[0]},
        Name {row[1]},
        Number {row[2]},
        Price {row[3]}
        *************************************
        """)

def Create(name,number,price):
    cursor = DatabaseContext.connect.cursor()
    cursor.execute("INSERT INTO dbo_MarketProducts(Name,Number,Price) VALUES('{}',{},{});".format(name,number,price))
    DatabaseContext.connect.commit()

def Update(Id,name,number,price):
    cursor = DatabaseContext.connect.cursor()
    cursor.execute("UPDATE dbo_MarketProducts SET Name = '{}', Number = {}, Price = {} WHERE Id = {};".format(name,number,price,Id))
    DatabaseContext.connect.commit()

def Remove(Id):
    if Id != None:
        cursor = DatabaseContext.connect.cursor()
        cursor.execute("DELETE FROM dbo_MarketProducts WHERE Id = {};".format(Id))
    else:
        print("Id cannot be null!")