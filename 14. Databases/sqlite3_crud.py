#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:46:18 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""
# CRUD (C = Create, R = Retrieve, U = Update, D = Delete)
# Shown here in a simpler way but not in an object oriented way (no error checking and related stuffs)

import sqlite3

def insert(db, row): # takes database object and dictionary object, row is a dictionary object
    db.execute('insert into test (t1, i1) values (?, ?)', (row['t1'], row['i1'])) # passes individual elements (has to be a list/tuple) into the placeholders in the sqlite3 execute() method
    db.commit() # commit is necessary after every change into the database

def retrieve(db, t1): # takes database object and key (dictionary key)
    cursor = db.execute('select * from test where t1 = ?', (t1,)) # sql to show data based on given key, here one element tuple
    return cursor.fetchone() # fatchone() method for cursor object. Will fetch one result

def update(db, row): # takes database object and dictionary object, row is a dictionary object
    db.execute('update test set i1 = ? where t1 = ?', (row['i1'], row['t1']))
    db.commit() # commit is necessary after every change into the database

def delete(db, t1): # takes database object and key (dictionary key)
    db.execute('delete from test where t1 = ?', (t1,))
    db.commit() # commit is necessary after every change into the database

def disp_rows(db):
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print('  {}: {}'.format(row['t1'], row['i1']))

def main():
    db = sqlite3.connect('test.db') # db is a database object
    db.row_factory = sqlite3.Row
    print('Create table test')
    db.execute('drop table if exists test')
    db.execute('create table test ( t1 text, i1 int )')
    
    print('Create rows')
    insert(db, dict(t1 = 'one', i1 = 1)) # dictionary has the data that will be inserted
    insert(db, dict(t1 = 'two', i1 = 2))
    insert(db, dict(t1 = 'three', i1 = 3))
    insert(db, dict(t1 = 'four', i1 = 4))
    disp_rows(db) # calling disp_rows() function to display data in screen
    
    print('Retrieve rows')
    print(dict(retrieve(db, 'one')), dict(retrieve(db, 'two')))
    
    print('Update rows')
    update(db, dict(t1 = 'one', i1 = 101))
    update(db, dict(t1 = 'three', i1 = 103))
    disp_rows(db)
    
    print('Delete rows')
    delete(db, 'one')
    delete(db, 'three')
    disp_rows(db)

if __name__ == "__main__": main()