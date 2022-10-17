import pymysql.cursors
import uuid


class Hospital:
    def __init__(self):
        self.__patients = []
        self.__doctor = []
        

class Config:
    def __init__(self):
        self.db_conn = pymysql.connect(host="67.205.163.33",
                             user="sjg89",
                             port="3306"
                             password="InfSci1500_4336514",
                             db="python_assignment",
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)

class Patient:
    def __init__(self, fname="", lname="", age="",patient_id=""):
        self.__lname = lname
        self.__fname = fname
        self.__age = age
        #creates a new user
        config = Config()
        con = config.db_conn
        if patient_id == "":
            self.__patient_id = str(uuid.uuid4())
            print(patient_id)
            try:
                with con.cursor() as cur:
                    qry = 'INSERT INTO patient (patient_id, fname, lname)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__patient_id, self.__fname, self.__lname)) 
                    con.commit()
            finally:
                con.close()
        #reads a user from uuid
        else:
            self.__patient_id = patient_id
            try:
                with con.cursor() as cur:
                    qry = "SELECT * FROM patient WHERE patient_id = '" + patient_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__patient_id = row["user_id"]
                        self.__fname = row["first_name"]
                        self.__lname = row["last_name"]
            finally:
                con.close()

user = Patient(fname="Julia", lname="Garthwaite", age="21",patient_id="")
