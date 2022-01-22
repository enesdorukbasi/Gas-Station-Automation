import psycopg2

connect = psycopg2.connect(
    host = "localhost",
    database = "GasStationAutomationDB",
    user = "postgres",
    password = "031100")