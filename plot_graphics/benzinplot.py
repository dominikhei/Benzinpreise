import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import lines
from matplotlib import patches
from matplotlib.patheffects import withStroke
import mysql.connector


# I have written the plotting script without a function, such that it can just
# get executed and two graphics will be plotted.

# If you wish to containerize the script, the database host has to be:
# host.docker.internal


db = mysql.connector.connect(
    user = 'root',
    password = '_______',
    host='localhost',
    database='Benzinpreise'
    )

db_cursor = db.cursor()

# The select statements to get the average prices and corresponding times,
# in the same order.

select_prices = """SELECT avg(price)
                   FROM benzinpreise
                   GROUP BY SUBSTRING(time,1,5)
                   ORDER BY SUBSTRING(time,1,5) ASC;"""

select_times = """SELECT SUBSTRING(time,1,5)
                  FROM benzinpreise
                  GROUP BY SUBSTRING(time,1,5)
                  ORDER BY SUBSTRING(time,1,5) ASC;"""

db_cursor.execute(select_prices)
prices1 = []
for i in db_cursor.fetchall():
    prices1.extend(i)

db_cursor.execute(select_times)
times1 = []
for i in db_cursor.fetchall():
    times1.extend(i)

# The data in the lists will be converted to a dataframe with two columns.

timeseries_data = { 'times' : times1,
                    'prices' : prices1}
dataframe = pd.DataFrame(timeseries_data,columns=['times', 'prices'])
dataframe = dataframe.set_index("times")

# Creation of the timeseries plot:


plt.plot(dataframe["prices"], color='#CD5C5C',linewidth=3)

plt.xlabel("Zeit", fontsize=11, fontweight='bold')
plt.ylabel("E5 Preis", fontsize=11, fontweight='bold')
plt.title("Benzinpreise in Freiburg", fontsize= 16, fontweight='bold', loc='left')
plt.axhline(y=np.nanmean(dataframe['prices']), color='#A4A4A4', linestyle='--', linewidth=1, label='Durchschnittspreis')
plt.axhline(y=1.98, color='#000000', linestyle='-', linewidth=1.5)
plt.grid(axis='y')
plt.legend(loc='upper right')
plt.xticks(rotation = 45)

plt.show()


#Boxplot:

vals, xs = [],[]
for i, col in enumerate(dataframe.columns):
    vals.append(dataframe[col].values)
    xs.append(np.random.normal(i + 1, 0.04, dataframe[col].values.shape[0]))

plt.boxplot(vals, showfliers=False)
palette = ['r']
for x, val, c in zip(xs, vals, palette):
    plt.scatter(x, val, alpha=0.4, color=c)

plt.title("Verteilung der Benzinpreise", fontsize= 16, fontweight='bold', loc='left')
plt.grid(axis='y')
plt.show()
