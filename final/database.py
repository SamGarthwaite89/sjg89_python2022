import json
import pymysql.cursors
from flask import Flask
import uuid

class Config:
    def __init__(self):
        self.db_conn = pymysql.connect(host="67.205.163.33",
                             user="sjg89",
                             port=3306,
                             password="InfSci1500_4336514",
                             db="sjg89",
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)

class User:
    def __init__(self,pk_user="", user_name="",joined_date="",first_name="",last_name=""):
        self.__pk_user = pk_user
        self.__user_name = user_name
        self.__joined_date=joined_date
        self.__first_name=first_name
        self.__last_name=last_name
        config = Config()
        con=config.db_conn
        if pk_user=="":
            self.__pk_user=str(uuid.uuid4())
            try:
                with con.cursor() as cur:
                    qry = 'INSERT INTO user (pk_user,user_name,joined_date,first_name,last_name)'
                    qry = qry + 'VALUES(%s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (pk_user,user_name,joined_date,first_name,last_name)) 
                    con.commit()
            finally:
                con.close()
        else:
            self.__pk_user=pk_user
            try:
                with con.cursor() as cur:
                    qry = "SELECT * FROM user WHERE pk_user = '" + self.__pk_user + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__user_name = row["user_name"]
                        self.__joined_date = row["joined_date"]
                        self.__first_name = row["first_name"]
                        self.__first_name = row["last_name"]
            finally:
                con.close()
    #getters
    def getPk_User(self):
        return self.__pk_user
    def getUser_name(self):
        return self.__user_name
    def getJoined_date(self):
        return self.__joined_date
    def getFirst_name(self):
        return self.__first_name
    def getLast_name(self):
        return self.__last_name
    #set
    def updateUser_name(self,text):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'UPDATE user SET user_name = %s WHERE pk_user = %s'

                cur.execute(qry, (text, self.__pk_user)) 
                con.commit()

        finally:

            con.close()

    def updateJoined_date(self,text):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'UPDATE user SET joined_date = %s WHERE pk_user = %s'

                cur.execute(qry, (text, self.__pk_user)) 
                con.commit()

        finally:

            con.close()
    def updateFirst_name(self,text):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'UPDATE user SET first_name = %s WHERE pk_user = %s'

                cur.execute(qry, (text, self.__pk_user)) 
                con.commit()

        finally:

            con.close()
    def updateLast_name(self,text):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'UPDATE user SET last_name = %s WHERE pk_user = %s'

                cur.execute(qry, (text, self.__pk_user)) 
                con.commit()

        finally:

            con.close()
    def delete(self):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'DELETE FROM user WHERE pk_user = %s'

                cur.execute(qry, (self.__pk_user)) 
                con.commit()
        finally:
            con.close()
    def to_json(self):
        fields_data = {
            "pk_user" : self.__pk_user,
            "user_name" : self.__user_name,
            "joined_date" : self.__joined_date,
            "first_name" : self.__first_name,
            "last_name" : self.__last_name
        }
        return json.dumps(fields_data,default=str)
    
class recipe:
    def __init__(self,pk_recipe,name,serving_size,cooking_time,makes):
        self.__name = name
        self.__serving_size = serving_size
        self.__cooking_time = cooking_time
        self.__makes = makes
        config = Config()
        con = config.db_conn
        if pk_recipe == "":
            self.__pk_recipe = str(uuid.uuid4())
            try:
                with con.cursor() as cur:
                    qry = 'INSERT INTO recipe (recipe, name, serving_size, cooking_time,makes)'
                    qry = qry + 'VALUES(%s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__pk_recipe, self.__name, self.__serving_size,self.__cooking_time, self.__makes)) 
                    con.commit()
            finally:
                con.close()    
        else:
            self.__pk_recipe = pk_recipe
            try:
                with con.cursor() as cur:
                    qry = "SELECT * FROM recipe WHERE pk_recipe = '" + self.__pk_recipe + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__pk_recipe = row["pk_recipe"]
                        self.__name = row["name"]
                        self.__serving_size = row["serving_size"]
                        self.__cooking_time = row["cooking_time"]
                        self.cooking_time = row["makes"]
            finally:
                con.close()
    def getPk_recipe(self):
        return self.__pk_recipe
    def getName(self):
        return self.__name
    def getServing_size(self):
        return self.__serving_size
    def getCooking_time(self):
        return self.cooking_time
    def getMakes(self):
        return
    def update_name(self,text):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'UPDATE recipe SET name = %s WHERE pk_recipe = %s'

                cur.execute(qry, (text, self.__pk_recipe)) 
                con.commit()

        finally:

            con.close()
    def updateServing_size(self,text):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'UPDATE recipe SET serving_size = %s WHERE pk_recipe = %s'

                cur.execute(qry, (text, self.__pk_recipe)) 
                con.commit()

        finally:
            con.close()
    def updateCooking_time(self,text):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'UPDATE recipe SET cooking_time = %s WHERE pk_recipe = %s'

                cur.execute(qry, (text, self.__pk_recipe)) 
                con.commit() 
        finally:
            con.close()       
    def updateMakes(self,text):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'UPDATE recipe SET makes = %s WHERE pk_recipe = %s'

                cur.execute(qry, (text, self.__pk_recipe)) 
                con.commit()

        finally:

            con.close()
    def delete(self):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'DELETE FROM recipe WHERE pk_recipe = %s'

                cur.execute(qry, (self.__pk_recipe)) 
                con.commit()
        finally:
            con.close()
            
    def to_json(self):
        fields_data = {
            "pk_recipe": self.__pk_recipe,
            "name" : self.__name,
            "serving_size" : self.__serving_size,
            "cooking_time" : self.__cooking_time,
            "makes" : self.__makes
        }
        return json.dumps(fields_data)

class store:
    def __init__(self,pk_store="",name="",address="",hours="",employee_count=""):
        self.__name = name
        self.__address = address
        self.__hours = hours
        self.__employee_count = employee_count
        config = Config()
        con = config.db_conn
        if pk_store == "":
            self.__pk_store = str(uuid.uuid4())
            try:
                with con.cursor() as cur:
                    qry = 'INSERT INTO store (pk_store,name,address,hours,employee_count)'
                    qry = qry + 'VALUES(%s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__pk_store,self.__name,self.__address,self.__hours,self.__employee_count)) 
                    con.commit()
            finally:
                con.close()
        else:
            self.__pk_store = pk_store
            try:
                with con.cursor() as cur:
                    qry = "SELECT * FROM store WHERE pk_store = '" + self.__pk_store + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__name = row["name"]
                        self.__address = row["address"]
                        self.__hours = row["hours"]
                        self.__employee_count = row["employee_count"]
            finally:
                con.close()
    def getPk_store(self):
        return self.__pk_store
    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    def getHours(self):
        return self.__hours
    def getEmployee_count(self):
        return self.__employee_count
    def updateName(self,text):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'UPDATE store SET name = %s WHERE pk_store = %s'

                cur.execute(qry, (text, self.__pk_store)) 
                con.commit()

        finally:

            con.close()
    def updateAddress(self,text):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'UPDATE store SET address = %s WHERE pk_store = %s'

                cur.execute(qry, (text, self.__pk_store)) 
                con.commit()

        finally:

            con.close()
    def updateHours(self,text):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'UPDATE store SET hours = %s WHERE pk_store = %s'

                cur.execute(qry, (text, self.__pk_store)) 
                con.commit()

        finally:

            con.close()
    def updateEmployee_count(self,text):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'UPDATE store SET employee_count = %s WHERE pk_store = %s'

                cur.execute(qry, (text, self.__pk_store)) 
                con.commit()

        finally:

            con.close()
    def delete(self):
        config = Config()
        con = config.db_conn
        try: 
            with con.cursor() as cur:
                qry = 'DELETE FROM store WHERE pk_store = %s'

                cur.execute(qry, (self.__pk_store))
                con.commit()
        finally:
            con.close()
    def to_json(self):
        fields_data = {
            "pk_store" : self.__pk_store,
            "name" : self.__pk_store,
            "address" : self.__address,
            "hours" : self.__hours,
            "employee_count" : self.__employee_count
        }
        return json.dumps(fields_data)


app = Flask(__name__)

@app.route("/")
def index():
    user = User("1")
    var = user.to_json()
    return var
