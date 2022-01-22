from Database import DatabaseContext
from Managements import FuelTankManagement
import datetime

def List():
    cursor = DatabaseContext.connect.cursor()
    cursor.execute("SELECT * FROM dbo_FuelDelivered")
    rows = cursor.fetchall()

    for row in rows:
        print(f"""
        Id {row[0]},
        LicensePlate {row[1]},
        FuelTypeId {row[2]},
        Liter {row[3]},
        Date Of {row[4]},
        Time Of {row[5]}
        *************************************
        """)

def Create(LicensePlate,FuelTypeId,Liter):
    cursor = DatabaseContext.connect.cursor()

    cursor2 = DatabaseContext.connect.cursor()
    cursor2.execute("SELECT PriceL FROM dbo_FuelTank WHERE Id = {};".format(FuelTypeId))
    rows = cursor2.fetchall()
    for row in rows:
        price = float(row[0])

    cursor.execute("INSERT INTO dbo_FuelDelivered(LicensePlate,FuelTypeId,Liter,totalPrice,DateOf,TimeOf) VALUES('{}',{},{},{},'{}','{}');".format(LicensePlate,int(FuelTypeId),float(Liter),float(Liter)*price,str(datetime.datetime.now().date()),str(datetime.datetime.now().time())))
    FuelTankManagement.Update(FuelTypeId,Liter)
    DatabaseContext.connect.commit()

def EndOfTheDay(fuelTypeId):
    cursor = DatabaseContext.connect.cursor()
    cursor.execute("SELECT SUM(TotalPrice) FROM dbo_FuelDelivered WHERE DateOf = '{}' AND FuelTypeId = {};".format(str(datetime.datetime.now().date()),int(fuelTypeId)))
    rows = cursor.fetchall()
    for row in rows:
        print(f"""End Of The Day
                  Total Price : {row[0]}""")
