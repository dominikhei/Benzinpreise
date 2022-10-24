import requests
import mysql.connector
from datetime import datetime
from datetime import date
import pandas as pd
from benzinpreis_secrets import *

# The host will not be set to localhost but to host.docker.interal,
# which points to the hosts IP, since we are trying to connect from
# within a docker container.

db = mysql.connector.connect(
        user = 'root',
        password = DB_PW,
        host='host.docker.internal',
        port='3306',
        database='Benzinpreise'
        )
db_cursor = db.cursor()

#Function to create the table in MySQL, if it does not exist yet.

def create_table():

    CREATE_TABLE='''CREATE TABLE IF NOT EXISTS benzinpreise(
                        load_id BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    			        price FLOAT(4),
                        time VARCHAR(8),
                        date VARCHAR(10));'''


    db_cursor.execute(CREATE_TABLE)

    db.commit()


#Method to load the current price in the database.

def load_prices(latitude, longitude, Radius, key):


    link = 'https://creativecommons.tankerkoenig.de/json/list.php?lat='+latitude+'&lng='+longitude+'&rad='+str(Radius)+'&sort=price&type=e5&apikey='+key

    r = requests.get(link)
    data = r.json()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    todays_date = str(date.today())

# The loop checks if a station is even open. If it is not,
# it will not add the price, because the price will be from a few hours ago.

    pricelist = []
    occurences = 0
    for element in data['stations']:
        if element['isOpen']==True:
            occurences+=1
            pricelist.append(element['price'])

    avg_price = sum(pricelist)/occurences

    #Here I am making sure, that the price is actually >0. If not, I will insert
    #The average for this time. If the retrieved average from the db is null,
    #the script will termiante.

    if avg_price > 0:
        avg_price = avg_price
    else:
        SELECT = """SELECT avg(price) FROM benzinpreise WHERE SUBSTRING(time,1,5)
                     = '{0}';""".format(current_time[0:4])
        db_cursor.execute(SELECT)
        price = db_cursor.fetchall()
        avg_price = price
        if avg_price is Null:
            print("Could not retrieve any possible price, thus the script is terminating")
            exit()

    #The price, date and time will be stored in a dictionary and from there on
    #be inserted in the table.

    gas_dict = {
                'price' : avg_price,
                'time' : current_time,
                'date' : todays_date
    }


    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in gas_dict.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in gas_dict.values())
    INSERT = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('benzinpreise', columns, values)

    try:
        db_cursor.execute(INSERT)
        print('Inserted values in the table')
        db.commit()
    except Exception as e:
        print('Could not insert values due to exception:', e)


def main():
    create_table()
    load_prices('47.997791', '7.842609', 20, API_KEY)


if __name__ == "__main__":
    main()
