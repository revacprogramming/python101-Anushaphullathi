import urllib.request, json

address = input('Enter location: ')
print('Retrieving', address)
with urllib.request.urlopen(address) as url:
    raw = json.loads(url.read().decode())

print('Retrieved', len(str(raw)), 'characters')
data = raw.get("comments")
#print(data)
num = total = 0
for i in range(len(data)):
    tmp = data[i]
    value = tmp.get("count")
    num = num + 1
    total = total + int(value)
print("Count:",num)
print("Sum:",total)
import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE Ages(
             name VARCHAR(128),
             age INTEGER
             )"""
         )
def add_people(sName, iAge):
    with conn:
        c.execute("INSERT INTO Ages VALUES (:name, :age)", {'name':sName, 'age':iAge})
    
