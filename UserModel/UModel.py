#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask

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



if __name__ == '__main__':
	
	User = UserModel()
	
	User.create_user_table()
	User.insert_user(('fullName', 'email', 'password', 'avatar', 'isActive', 'role_id'), ('Denis', 'dendendengrebenets@gmail.com', 'srsrf', 'sfr', 1, 1))
	




