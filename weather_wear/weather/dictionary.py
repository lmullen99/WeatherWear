# this file creates the static data dictionary of what outfits correspond to certain weather conditions
# this will be called upon by the website when making forecasts
import sqlite3


# create new database
conn = sqlite3.connect('OUTFITS.db')
# create Cursor to execute queries
cur = conn.cursor()

# drop table statement
try:
    conn.execute('''Drop table OUTFITS''')
    conn.commit()
    print('Outfits table dropped.')
except:
    print('Outfits table did not exist.')

# create table in database
cur.execute(''' CREATE TABLE OUTFITS(
Temp INTEGER PRIMARY KEY NOT NULL,
Top STRING NOT NULL,
Bottom STRING NOT NULL,
Outerwear STRING NOT NULL,
Accessories STRING NOT NULL,
Footwear STRING NOT NULL);
''')

print('Outfit table created.')

# save changes
conn.commit()

# add 30 degree window
temp = 30
top = "thick sweater"
bottoms = "jeans or sweatpants"
outer = "winter coat"
access = "beanie, scarf, thick socks, and gloves"
foot = "boots"
cur.execute("Insert Into OUTFITS (Temp, Top, Bottom, Outerwear, Accessories, Footwear) Values (?, ?, ?, ?, ?, ?)",
            (temp, top, bottoms, outer, access, foot))
conn.commit()

# add 40 degree
temp = 40
top = "sweater/sweatshirt"
bottoms = "jeans or leggings"
outer = "windbreaker?"
access = "beanie, thick socks, and gloves"
foot = "boots or sneakers"
cur.execute("Insert Into OUTFITS (Temp, Top, Bottom, Outerwear, Accessories, Footwear) Values (?, ?, ?, ?, ?, ?)",
            (temp, top, bottoms, outer, access, foot))
# add 50 degrees
conn.commit()
temp = 50
top = "long sleeve shirts or light sweaters"
bottoms = "jeans or leggings"
outer = "vest or windbreaker"
access = "umbrella"
foot = "sneakers"
cur.execute("Insert Into OUTFITS (Temp, Top, Bottom, Outerwear, Accessories, Footwear) Values (?, ?, ?, ?, ?, ?)",
            (temp, top, bottoms, outer, access, foot))
conn.commit()
# add 60 degrees
temp = 60
top = "long sleeve shirt or t-shirt"
bottoms = "jeans or leggings"
outer = "pullover or cardigan"
access = "umbrella"
foot = "sneakers or boat shoes"
cur.execute("Insert Into OUTFITS (Temp, Top, Bottom, Outerwear, Accessories, Footwear) Values (?, ?, ?, ?, ?, ?)",
            (temp, top, bottoms, outer, access, foot))
conn.commit()

# add 70 degrees
temp = 70
top = "short sleeves or tanks"
bottoms = "leggings, shorts, or skirts"
outer = "cardigan"
access = "umbrella"
foot = "sneakers or sandals"
cur.execute("Insert Into OUTFITS (Temp, Top, Bottom, Outerwear, Accessories, Footwear) Values (?, ?, ?, ?, ?, ?)",
            (temp, top, bottoms, outer, access, foot))
conn.commit()

# add 80 degrees
temp = 80
top = "short sleeves, tanks, or dresses"
bottoms = "shorts or skirts"
outer = ""
access = "umbrella"
foot = "sneakers or sandals"
cur.execute("Insert Into OUTFITS (Temp, Top, Bottom, Outerwear, Accessories, Footwear) Values (?, ?, ?, ?, ?, ?)",
            (temp, top, bottoms, outer, access, foot))
conn.commit()

# add 90 degrees
temp = 90
top = "short sleeves, tanks, or dresses"
bottoms = "shorts or skirts"
outer = " "
access = "umbrella"
foot = "sneakers or sandals"
cur.execute("Insert Into OUTFITS (Temp, Top, Bottom, Outerwear, Accessories, Footwear) Values (?, ?, ?, ?, ?, ?)",
            (temp, top, bottoms, outer, access, foot))
conn.commit()

print('Outfit Table\n')
for row in cur.execute('SELECT * FROM OUTFITS'):
    print(row)

# close database connection
conn.close()
print('Connection closed')
