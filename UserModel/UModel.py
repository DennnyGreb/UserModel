#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb

from flask import Flask

from ORM import Driver

class UserModel(Driver):

    def __init__(self):
        self.table_name = "Test"
        self.DB = Driver()

    def connect_to_db(self):
        self.DB.connect("localhost", "denny", "isurrender", "local_db")

    #def create_user_table(self):
    #   print('Creating Table')
    #   self.connect_to_db()
        #self.DB.execute_query('DROP TABLE IF EXISTS Test')
        #self.DB.execute_query('CREATE TABLE Test (id INT, fullName VARCHAR(100), email VARCHAR(100), password VARCHAR(10), avatar VARCHAR(100), isActive BOOLEAN, role_id INT, PRIMARY KEY(id))')

    def insert_user(self, columns, vals):
        print "Inserting"
        self.DB.insert(self.table_name, columns, vals)

    def select_user(self, columns):
        print "Reading"
        print self.DB.select(self.table_name, columns)

    def update_user(self, changes, condition):
        print "Updating"
        self.DB.update(self.table_name, changes, condition)

    def delete_user(self, condition):
        print "Deleting"
        self.DB.delete(self.table_name, condition)

if __name__ == '__main__':
    
    User = UserModel()
    
    print('Creating Table')
    User.connect_to_db()
    
    #User.DB.execute_query('DROP TABLE IF EXISTS Test')
    #User.DB.execute_query('CREATE TABLE Test (id INT NOT NULL AUTO_INCREMENT, fullName VARCHAR(100), email VARCHAR(100), password VARCHAR(10), avatar VARCHAR(100), isActive BOOLEAN, role_id INT, PRIMARY KEY(id))')

    #User.insert_user(('fullName', 'email', 'password', 'avatar', 'isActive', 'role_id'), ('Oleg', 'naumleg@urk.net', 'qweasdzxc', 'Uleshka', 1, 2))

    #User.select_user(('fullName', 'email'))

    #User.update_user('avatar = "Naumchuk"', 'fullName = "Oleg"')

    #User.delete_user('password = "hahaha"')