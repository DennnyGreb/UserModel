#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask

import MySQLdb

from ORM import Driver

class UserModel(Driver):

	def __init__(self):
		self.table_name = "Test"
		self.DB = Driver()

	def connect_to_db(self):
		self.DB.connect("localhost", "denny", "isurrender", "local_db")

	def create_user_table(self):
		print('Creating Table')
		self.connect_to_db()
		self.DB.execute_query('DROP TABLE IF EXISTS Test')
		self.DB.execute_query('CREATE TABLE Test (id INT, fullName VARCHAR(100), email VARCHAR(100), password VARCHAR(10), avatar VARCHAR(100), isActive BOOLEAN, role_id INT, PRIMARY KEY(id))')

	def insert_user(self, columns, vals):
		print "Inserting"
		self.DB.insert(self.table_name, columns, vals)

	def select_user(self, columns):
		print "Reading"
		self.DB.select(self.table_name, columns)

	def update_user(self, changes, condition):
		print "Updating"
		self.DB.update(self.table_name, changes, condition)

	def delete_user(self, condition):
		print "Deleting"
		self.DB.delete(self.table_name, condition)

if __name__ == '__main__':
	
	User = UserModel()
	
	User.create_user_table()

	User.execute_query(User.insert(User.table_name, ('fullName', 'email', 'password', 'avatar', 'isActive', 'role_id'), ('Denis', 'dendendengrebenets@gmail.com', 'srsrf', 'sfr', 1, 1)))




