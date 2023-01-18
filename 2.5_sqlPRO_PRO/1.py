from datetime import datetime, timedelta
import psycopg2
import psycopg2.extensions


class DataBase():
    """A class used to create tables in the database. Inherits from
    psycopg2.extensions.connection in order to gain access to the cursor,
    commit, close, and many other features from the pyscopg module.
    """
    def __init__(self):
        self.my_connection = psycopg2.connect(database="public", user="public",
                                  password="general", host="127.0.0.1",
                                  port="5432")
        self.my_cursor = self.my_connection.cursor()

    def query_database(self, sql_statement, *args):
        return self.my_cursor.execute(sql_statement, *args)

    def commit_query(self):
        return self.my_connection.commit()

    def fetch_one(self, sql_statement, *args):
        result = self.query_database(sql_statement, *args)
        if result is None:
            return False
        return result.fetchone()

    def fetch_all(self, sql_statement, *args):
        result = self.query_database(sql_statement, *args)
        if result is None:
            return False
        return result.fetchall()

    def __del__(self):
        self.my_cursor.close()
        self.my_connection.close()


############################################################################
class CreateTables(DataBase):
    def create_user_table(self):
        """Helper function used to create the user_table"""
        sql_statement = '''CREATE TABLE IF NOT EXISTS USERS
                (ID                 SERIAL    PRIMARY KEY,
                FIRSTNAME           TEXT      NOT NULL,
                LASTNAME            TEXT      NOT NULL,
                USERNAME            TEXT      NOT NULL UNIQUE,
                EMAIL               TEXT      NOT NULL UNIQUE,
                PASSWORD            TEXT      NOT NULL,
                DATETIMEREGISTERED  TIMESTAMP NOT NULL);'''
        user_table = DataBase.query_database(self, sql_statement)
        DataBase.commit_query(self)
        return user_table

    def create_entries_table(self):
        """Helper function used to create an entries table."""
        sql_statement = '''CREATE TABLE IF NOT EXISTS ENTRIES
                        (ID             SERIAL      PRIMARY KEY,
                        TITLE           TEXT        NOT NULL,
                        DRINK           TEXT        NOT NULL,
                        DATEOFORDER     TIMESTAMP   NOT NULL,
                        TIMETODELIVERY  TIMESTAMP   NOT NULL,
                        SETREMINDER     TIMESTAMP   NOT NULL,
                        USERID      INT REFERENCES USERS ON DELETE CASCADE);'''
        entries_table = DataBase.query_database(self, sql_statement)
        DataBase.commit_query(self)
        print("entries table created.")
        return entries_table

# test = CreateTables() This is working well
# print(test.create_entries_table())

#####################################################################

class OperateDatabase(CreateTables):

    def create_user(self, email, username, *args):
        """Helper function used to create a user"""
        sql_statement = """SELECT ID FROM USERS WHERE EMAIL = %s OR
                         USERNAME = %s;"""
        user_in_database = CreateTables.fetch_one(self, sql_statement,
                                                  (email, username,))
        print("the user in database is :>>", user_in_database)

        sql_statement2 = """INSERT INTO USERS (FIRSTNAME, LASTNAME, USERNAME,
                         EMAIL, PASSWORD, DATETIMEREGISTERED)
                         VALUES (%s, %s, %s, %s, %s, %s);"""
        if not user_in_database:
            CreateTables.query_database(self,sql_statement2, *args)
            CreateTables.commit_query(self)
            return True
        return False

data = ("Jkdai", "Jkdal", "Jkdai", "jkdai@gmail.com", "password", datetime.now())
test = OperateDatabase()
print(test.create_user("jkdai@gmail.com", "jkdai", data))