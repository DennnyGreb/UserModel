#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Give posibility of CRUD queries within methods.
Simple ORM, that gives posibility of using CRUD queries within python methods.
"""

import MySQLdb


class Driver(object):
    """Describe SQL queries through methods.

    Public methods: connect, close, execute_query, tuple_transform,
    insert, select, update, delete.
    
    """

    def connect(self, host, user_name, password, db):
        """Connect to database."""
        self.db = MySQLdb.connect(host, user_name, password, db)
        # Create cursor
        self.cursor = self.db.cursor(MySQLdb.cursors.Cursor)

    def close(self):
        """Close connection with database."""
        self.db.close()

    def execute_query(self, query):
        """Execute a sql query."""
        try:
            # Executing a sql query with execute() method
            self.cursor.execute(query)

            # Finalizing the changes using commit() method
            self.db.commit()

            # Returning all fetched values
            self.cursor.fetchall()
        except:
            # Rollback in case of error
            print "Error"
            self.db.rollback()

    def tuple_transform(self, _tuple):
        """Transform tuple into string."""
        loop_index = 1
        val = '('
        for field in _tuple:
            if isinstance(field, int):
                val += str(field)
                if loop_index < len(_tuple):
                    val += ', '
            elif isinstance(field, str):
                val += '"' + field + '"'
                if loop_index < len(_tuple):
                    val += ', '
            loop_index += 1
        val += ')'

        return val

    def insert(self, table_name, columns, vals):
        """Insert new records in a table."""
        insert_query = "INSERT INTO %s (%s) VALUES %s" \
            % (table_name, (', ').join(columns), self.tuple_transform(vals))

        # Use execute_query() method
        self.execute_query(insert_query)

    def select(self, table_name, columns):
        """Read the result of query."""
        select_query = "SELECT %s FROM %s" % ((', ').join(columns), table_name)

        try:
            # Execute query
            self.cursor.execute(select_query)

            # Fetch output of executing
            self.select_result = self.cursor.fetchall()

            # Return result
            return self.select_result
        except:
            # Rollback in case of error
            self.db.rollback()

    def update(self, table_name, changes, condition):
        """Update records in a table."""
        update_query = "UPDATE %s SET %s WHERE %s" % \
            (table_name, changes, condition)
        self.execute_query(update_query)

    def delete(self, table_name, condition):
        """Delete selected records."""
        delete_query = "DELETE FROM %s WHERE %s" % (table_name, condition)
        self.execute_query(delete_query)

# if __name__ == '__main__':

    # tmpDB = Driver()

    # Connecting to database
    # tmpDB.connect("localhost", "denny", "isurrender", "local_db")

    # print('Executing any query')
    # tmpDB.execute_query('DROP TABLE IF EXISTS Test')
    # tmpDB.execute_query('CREATE TABLE Test (Name VARCHAR(30), Age INT)')

    # print('Inserting values')
    # tmpDB.insert('Test', ('Name', 'Age'), ('Nick', 24))

    # print('Reading data')
    # print tmpDB.select('Test', ('Name', 'Age'))

    # print('Updating data')
    # tmpDB.update('EMPLOYEE', 'FIRST_NAME = "Denis"', 'LAST_NAME = "Mohan"')

    # print('Deleting data')
    # tmpDB.delete('EMPLOYEE', 'AGE = 21')

# tmpDB.close()