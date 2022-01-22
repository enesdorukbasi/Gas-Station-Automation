from Database import DatabaseContext

def List():
    cursor = DatabaseContext.connect.cursor()
    cursor.execute("SELECT * FROM dbo_FuelTank")
    rows = cursor.fetchall()

    for row in rows:
        print(f"""
        Id {row[0]},
        Name {row[1]},
        PriceL {row[2]},
        Fullness {row[3]}
        *************************************
        """)

def Update(FuelTypeId,Liter):
    cursor = DatabaseContext.connect.cursor()
    cursor2 = DatabaseContext.connect.cursor()
    cursor2.execute("SELECT Fullness FROM dbo_FuelTank WHERE Id = {};".format(FuelTypeId))
    rows = cursor2.fetchall()
    for row in rows:
        oldFullness = float(row[0])

    cursor.execute("UPDATE dbo_FuelTank SET Fullness = {} WHERE Id = {};".format(float(oldFullness-float(Liter)),int(FuelTypeId)))
    DatabaseContext.connect.commit()

def Refueling(FuelTypeId,Liter):
    cursor = DatabaseContext.connect.cursor()
    cursor2 = DatabaseContext.connect.cursor()
    cursor2.execute("SELECT Fullness FROM dbo_FuelTank WHERE Id = {};".format(FuelTypeId))
    rows = cursor2.fetchall()
    for row in rows:
        oldFullness = float(row[0])

    cursor.execute("UPDATE dbo_FuelTank SET Fullness = {} WHERE Id = {};".format(float(oldFullness + float(Liter)),FuelTypeId))
    DatabaseContext.connect.commit()