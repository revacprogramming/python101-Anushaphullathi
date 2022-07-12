# Databases
# https://www.py4e.com/lessons/database
import sqlite3  #here u r importing sqlite3
con = sqlite.connect('emaildb.sqlite') #connecting to requite email that u want to analyse
cur = con.cursor()  #we send sql commands through cursor

cur.excecute('Drop a table if exists')
cur.excecute('''
CREATE TABLE Counts(email TEXT,count INTEGER)''')....



