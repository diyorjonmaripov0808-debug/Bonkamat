from psycopg2 import connect
import psycopg2

class Data_Connect:
    def __init__(self,dbname,user,password,host='localhost',port = 5432):
        self.connection = psycopg2.connect(
            dbname = dbname,
            user = user,
            password = password,
            host = host,
            port = port
        )
        self.cursor = self.connection.cursor()
        # self.cursor.close()

    def view_users(self):
            query = "SELECT * FROM Users"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)


    def add_user(self,full_name,age,phone,address,fax):
        query = """
        INSERT INTO Users(full_name,age,phone,address,fax)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(query,(full_name,age,phone,address,fax))
        self.connection.commit()

    def delete_user(self,user_id):
        query = """ DELETE FROM Users WHERE user_id = %s"""
        self.cursor.execute(query,(user_id,))
        self.connection.commit()
        print(f"User with ID {user_id} deleted successfully.")



connector  = Data_Connect('Contact_manager', 'User', '123')


def manager():
    while True:
        kod = input("1. View all Users\n2. Add a User\n3. Delete a user\n4. Exit")
        if kod == '1':
            print('============== USERS ================')
            connector.view_users()
        if kod == '2':
            print('============== Add User =============')
            full_name = input("Enter a name: ")
            age = input("Enter your age: ")
            phone = input("Enter your phone: ")
            address = input("Enter your address: ")
            fax = input("Enter your fax: ")
            connector.add_user(full_name, age, phone, address, fax)
        if kod == '3':
            print("============== Delete User ============")
            user_id = input("Enter a user ID to delete: ")
            connector.delete_user(user_id)
        if kod == '4':
            break
manager()
