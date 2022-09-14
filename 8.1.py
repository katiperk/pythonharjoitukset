import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database="flight_game",
    user='root',
    password='kissa',
    autocommit=True
)

icao = input("Anna lentokentän ICAO-koodi : ")
sql = "SELECT name, municipality FROM airport WHERE ident = '" + icao + "'"
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
print(tulos)