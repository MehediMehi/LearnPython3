#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:22:31 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""
# custom class for working with a specific database, major 4 functions (CRUD) and couple of other things

import sqlite3

class database: # class to handle particular schema
    def __init__(self, **kwargs): # constractor takes arguments where first one is the database file name and second one is the table name
        self.filename = kwargs.get('filename') # using decorators
        self.table = kwargs.get('table', 'test') # using decorators 
    
    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit() # to save changes
    
    def insert(self, row): # takes the row as a dictionary object
        self._db.execute('insert into {} (t1, i1) values (?, ?)'.format(self._table), (row['t1'], row['i1'])) # {} to insert table name and tuples to insert in place of ?
        self._db.commit() # to save changes
    
    def retrieve(self, key):
        cursor = self._db.execute('select * from {} where t1 = ?'.format(self._table), (key,)) # ? takes tuple (Here (key,) is a single element tuple)
        return dict(cursor.fetchone()) # returns a dictionary object using fetchone() method of the database cursor 
    
    def update(self, row): # takes the row as a dictionary object
        self._db.execute(
            'update {} set i1 = ? where t1 = ?'.format(self._table),
            (row['i1'], row['t1']))
        self._db.commit() # to save changes
    
    def delete(self, key):
        self._db.execute('delete from {} where t1 = ?'.format(self._table), (key,)) # ? takes tuple (Here (key,) is a single element tuple)
        self._db.commit() # to save changes
    
    def disp_rows(self): # print out the data/table
        cursor = self._db.execute('select * from {} order by t1'.format(self._table))
        for row in cursor:
            print('  {}: {}'.format(row['t1'], row['i1']))
    
    def __iter__(self): # __iter__() is a special method (geneator) in python, it allows class object to be used as a iterator 
        cursor = self._db.execute('select * from {} order by t1'.format(self._table))
        for row in cursor:
            yield dict(row)
    # proparties for settng the file name that make it easy to change files if you want to
    @property # Decorators to allow file names to assign like those up there (in constructors etc)
    def filename(self): return self._filename
    
    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.connect(fn) # when the filename is assigned it connects to the database 
        self._db.row_factory = sqlite3.Row # and sets up the row factor 
    
    @filename.deleter
    def filename(self): self.close() # when you delete the file name it closes the database
    
    @property
    def table(self): return self._table
    @table.setter
    def table(self, t): self._table = t # sets the table name
    @table.deleter
    def table(self): self._table = 'test' # because, if the table name is blank that will raise error while deleting a table
    
    def close(self):
            self._db.close()
            del self._filename

def main():
    db = database(filename = 'test.db', table = 'test') # creating a database (object) by passing file name and table name, constructor does the rest
    
    print('Create table test')
    db.sql_do('drop table if exists test') # creating  table with sql
    db.sql_do('create table test ( t1 text, i1 int )')
    
    print('Create rows')
    db.insert(dict(t1 = 'one', i1 = 1)) # inserting rows into the table using dictionary objects
    db.insert(dict(t1 = 'two', i1 = 2))
    db.insert(dict(t1 = 'three', i1 = 3))
    db.insert(dict(t1 = 'four', i1 = 4))
    for row in db: print(row) # prints because of __iter__() method above
    
    print('Retrieve rows')
    print(db.retrieve('one'), db.retrieve('two')) # retrieve rows using keys (dictionary objects)
    
    print('Update rows')
    db.update(dict(t1 = 'one', i1 = 101)) # update rows using dictionary objects
    db.update(dict(t1 = 'three', i1 = 103))
    for row in db: print(row)
    
    print('Delete rows')
    db.delete('one') # update rows using keys (dictionary objects)
    db.delete('three')
    for row in db: print(row)

if __name__ == "__main__": main() # bacause of this pattern, this entire file will work as a module, you can import this database-class file so you have the access of this class and methods
# main() will be completely ignored if imported, because if __name__ == "__main__": is no longer true, so main will not be called