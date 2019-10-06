#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:13:29 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""
# sqlite3 comes with python, (can use other databases)
# always commit() after any change in the database

import sqlite3 # python library for sqlite3

def main():
    db = sqlite3.connect('test.db') # create if not exists, connect to the database. db is a database object
    db.row_factory = sqlite3.Row # row_factory allows you to specify how rows will be returned from the cursor, can execute without this line which will show tuple
    db.execute('drop table if exists test') # sql to execute. Dropping previous table if exists and create a new table each time (Name = test)
    db.execute('create table test (t1 text, i1 int)') # table name = test, fileds: t1 (type = text), i1 (type = integer)
    db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1)) # ? is a placeholders, allows us to give tuples with values .
    db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into test (t1, i1) values (?, ?)', ('three', 3))
    db.execute('insert into test (t1, i1) values (?, ?)', ('four', 4))
    db.commit() # sqlite is a transactional database, it will buffer these values in case you are going to be using in a transactional mode
    cursor = db.execute('select * from test order by t1') # standard sql to collect data from database, and place in the cursor object
    for row in cursor: # cursor object is an iterator
        #print(row) # show the data without row_factory
        print(dict(row)) # creating dictionary object based on row (iterable).
        print(row['t1']) # get only t1 objects
        print(row['t1'], row['i1']) # all the data

if __name__ == "__main__": main()