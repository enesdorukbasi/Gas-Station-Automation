import sys
import Managements.FuelTankManagement
import Managements.FuelDeliveredManagement
import Managements.MarketProductManagement
import Managements.MarketSalesManagement

MainMenu = """
(1)Fuel Tank Transactions
(2)Fuel Delivered Transactions
(3)Market Product Transactions
(4)Market Sales Transactions
(5)Exit
Please select an action...
"""
FuelTankMenu = """
You have selected Fuel Tank operations
(1)List
(2)Refueling
"""
FuelDeliveredMenu = """
You have selected Fuel Delivered operations
(1)List
(2)Create
(3)End Of The Day
"""
MarketProductMenu = """
You have selected Market Product operations
(1)List
(2)Create
(3)Update
(4)Remove
"""
MarketSalesMenu = """
You have selected Market Sales operations
(1)List
(2)Create
(3)Remove
"""

while True:
    print(MainMenu)
    process = int(input(""))
    if process == 1:
        print(FuelTankMenu)
        FuelTankProcess = int(input(""))
        if FuelTankProcess == 1:
            Managements.FuelTankManagement.List()
        elif FuelTankProcess == 2:
            FuelTypeId = int(input("Select the tank you want to refuel : "))
            Liter = float(input("How many liters of fuel will be added to the tank : "))
            Managements.FuelTankManagement.Refueling(FuelTypeId,Liter)
        else:
            print("You entered an incorrect transaction code.")
    elif process == 2:
        print(FuelDeliveredMenu)
        FuelDeliveredProcess = int(input(""))
        if FuelDeliveredProcess == 1:
            Managements.FuelDeliveredManagement.List()
        elif FuelDeliveredProcess == 2:
            LicensePlate = input("Enter the License Plate of the 'FuelDelivered' to be added : ")
            FuelTypeId = input("Enter the Fuel Type Id of the 'FuelDelivered' to be added : ")
            Liter = input("Enter the Liter of the 'FuelDelivered' to be added : ")
            Managements.FuelDeliveredManagement.Create(LicensePlate,FuelTypeId,Liter)
        elif FuelDeliveredProcess == 3:
            fuelTypeId = input("Select the fuel type to be purchased at the end of the day : ")
            Managements.FuelDeliveredManagement.EndOfTheDay(fuelTypeId)
        else:
            print("You entered an incorrect transaction code.")
    elif process == 3:
        print(MarketProductMenu)
        MarketProductProcess = int(input(""))
        if MarketProductProcess == 1:
            Managements.MarketProductManagement.List()
        elif MarketProductProcess == 2:
            name = input("Enter the name of the 'MarketProduct' to be added : ")
            number = int(input("Enter the number of the 'MarketProduct' to be added : "))
            price = float(input("Enter the price of the 'MarketProduct' to be added : "))
            Managements.MarketProductManagement.Create(name,number,price)
        elif MarketProductProcess == 3:
            Id = int(input("Enter the id of the 'MarketProduct' to be update : "))
            name = input("Enter the name of the 'MarketProduct' to be update : ")
            number = int(input("Enter the number of the 'MarketProduct' to be update : "))
            price = float(input("Enter the price of the 'MarketProduct' to be update : "))
            Managements.MarketProductManagement.Update(Id,name,number,price)
        elif MarketProductProcess == 4:
            Id = int(input("Enter the id of the 'MarketProduct' to be remove : "))
            Managements.MarketProductManagement.Remove(Id)
        else:
            print("You entered an incorrect transaction code.")
    elif process == 4:
        print(MarketSalesMenu)
        MarketSalesProcess = int(input(""))
        if MarketSalesProcess == 1:
            Managements.MarketSalesManagement.List()
        elif MarketSalesProcess == 2:
            productId = input("Enter the productId of the 'MarketSales' to be added : ")
            number = input("Enter the number of the 'MarketSales' to be added : ")
            price = float(input("Enter the price of the 'MarketSales' to be added : "))
            Managements.MarketSalesManagement.Create(productId,number,price)
        elif MarketSalesProcess == 3:
            Id = int(input("Enter the id of the 'MarketSales' to be remove : "))
            Managements.MarketSalesManagement.Remove(Id)
        else:
            print("You entered an incorrect transaction code.")
    elif process == 5:
        print("Checking out...")
        sys.exit()
    else:
        print("You entered an incorrect transaction code.")