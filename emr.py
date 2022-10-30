import uuid
import json
import pymysql.cursors
import unittest

class Config:
    '''iniciates the sql connection'''
    def __init__(self):
        self.db_conn = pymysql.connect(host="67.205.163.33",
                             user="sjg89",
                             port=3306,
                             password="InfSci1500_4336514",
                             db="sjg89",
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)

class Patient:
    '''represents patient table'''
    def __init__(self, fname="", lname="", age="",patient_id=""):
        self.__lname = lname
        self.__fname = fname
        self.__age = age
        #creates a new user
        config = Config()
        con = config.db_conn
        if patient_id == "":
            self.__patient_id = str(uuid.uuid4())
            print(self.__patient_id)
            try:
                with con.cursor() as cur:
                    qry = 'INSERT INTO patient (patient_id, fname, lname, age)'
                    qry = qry + 'VALUES(%s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__patient_id, self.__fname, self.__lname, self.__age))
                    con.commit()
            finally:
                con.close()
        #reads a user from uuid
        else:
            self.__patient_id = patient_id
            try:
                with con.cursor() as cur:
                    qry = "SELECT * FROM patient WHERE patient_id = '" + self.__patient_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__patient_id = row["patient_id"]
                        self.__fname = row["fname"]
                        self.__lname = row["lname"]
            finally:
                con.close()
        #Read
    def get_patient_id(self):
        return self.__patient_id
    def get_fname(self):
        return self.__fname
    def get_lname(self):
        return self.__lname
    def get_age(self):
        return self.__age
    #set
    def update_fname(self,text):
        config = Config()
        self.__fname = text
        con = config.db_conn
        try:
            with con.cursor() as cur:
                qry = 'UPDATE patient SET fname = %s WHERE patient_id = %s'

                cur.execute(qry, (text, self.__patient_id))
                con.commit()

        finally:

            con.close()
    def update_lname(self,text):
        self.__lname = text
        config = Config()
        con = config.db_conn
        try:

            with con.cursor() as cur:
                qry = 'UPDATE patient SET lname = %s WHERE patient_id = %s'

                cur.execute(qry, (text, self.__patient_id))
                con.commit()

        finally:

            con.close()
    def update_age(self,num):
        self.__age = num
        config = Config()
        con = config.db_conn
        try:

            with con.cursor() as cur:
                qry = 'UPDATE patient SET age = %s WHERE patient_id = %s'

                cur.execute(qry, (num, self.__patient_id))
                con.commit()

        finally:

            con.close()
    def delete(self):
        config = Config()
        con = config.db_conn
        try:
            with con.cursor() as cur:
                qry = 'DELETE FROM patient WHERE patient_id = %s'

                cur.execute(qry, (self.__patient_id))
                con.commit()
        finally:
            con.close()

    def to_json(self):
        fields_data = {
            "patient_id" : self.__patient_id,
            "fname" : self.__fname,
            "lname" : self.__lname,
            "age"   : self.__age
        }
        return json.dumps(fields_data)


class Doctor:
    '''represents doctor table'''
    def __init__(self, fname="", lname="", age="",doctor_id=""):
        self.__lname = lname
        self.__fname = fname
        self.__age = age
        #creates a new user
        config = Config()
        con = config.db_conn
        if doctor_id == "":
            self.__doctor_id = str(uuid.uuid4())
            try:
                with con.cursor() as cur:
                    qry = 'INSERT INTO doctor (doctor_id, fname, lname, age)'
                    qry = qry + 'VALUES(%s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__doctor_id, self.__fname, self.__lname, self.__age))
                    con.commit()
            finally:
                con.close()
        #reads a user from uuid
        else:
            self.__doctor_id = doctor_id
            try:
                with con.cursor() as cur:
                    qry = "SELECT * FROM doctor WHERE doctor_id = '" + self.__doctor_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__doctor_id = row["doctor_id"]
                        self.__fname = row["fname"]
                        self.__lname = row["lname"]
                        self.__age = row["age"]
            finally:
                con.close()
        #Read
    def get_doctor_id(self):
        return self.__doctor_id
    def get_fname(self):
        return self.__fname
    def get_lname(self):
        return self.__lname
    def get_age(self):
        return self.__age
    #set
    def update_fname(self,text):
        self.__fname = text
        config = Config()
        con = config.db_conn
        try:

            with con.cursor() as cur:
                qry = 'UPDATE doctor SET fname = %s WHERE doctor_id = %s'

                cur.execute(qry, (text, self.__doctor_id))
                con.commit()

        finally:

            con.close()
    def update_lname(self,text):
        self.__lname = text
        config = Config()
        con = config.db_conn
        try:

            with con.cursor() as cur:
                qry = 'UPDATE doctor SET lname = %s WHERE doctor_id = %s'

                cur.execute(qry, (text, self.__doctor_id))
                con.commit()

        finally:

            con.close()
    def update_age(self,num):
        self.__age = num
        config = Config()
        con = config.db_conn
        try:

            with con.cursor() as cur:
                qry = 'UPDATE doctor SET age = %s WHERE doctor_id = %s'

                cur.execute(qry, (num, self.__doctor_id))
                con.commit()

        finally:

            con.close()

    def delete(self):
        config = Config()
        con = config.db_conn
        try:
            with con.cursor() as cur:
                qry = 'DELETE FROM doctor WHERE doctor_id = %s'

                cur.execute(qry, (self.__doctor_id))
                con.commit()
        finally:

            con.close()
    def to_json(self):
        fields_data = {
            "doctor_id" : self.__doctor_id,
            "fname" : self.__fname,
            "lname" : self.__lname,
            "age"   : self.__age
        }
        return json.dumps(fields_data)

class Visit:
    def __init__(self, fk_patient_id ,fk_doctor_id,successful=True,refferal_name="",visit_id=""):
        self.__fk_patient_id = fk_patient_id
        self.__fk_doctor_id = fk_doctor_id
        self.__successful = successful
        self.__refferal_name = refferal_name
        config = Config()
        con = config.db_conn
        if visit_id == "":
            self.__visit_id = str(uuid.uuid4())
            try:
                with con.cursor() as cur:
                    qry = 'INSERT INTO visit '
                    qry += '(visit_id,fk_patient_id,fk_doctor_id,successful,refferal_name)'
                    qry = qry + 'VALUES(%s, %s, %s,%s,%s)'
                    print(qry)
                    cur.execute(qry, (self.__visit_id,self.__fk_patient_id,
                    self.__fk_doctor_id,self.__successful,self.__refferal_name))
                    con.commit()
            finally:
                con.close()
        else:
            self.__visit_id = visit_id
            try:
                with con.cursor() as cur:
                    qry = "SELECT * FROM visit WHERE visit_id = '" + self.__visit_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__fk_patient_id = row["fk_doctor_id"]
                        self.__fk_doctor_id = row["fk_doctor_id"]
                        self.__successful = row["successful"]
                        self.__refferal_name = row["refferal_name"]
            finally:
                con.close()
    #read
    def get_patient_id(self):
        return self.__fk_patient_id
    def get_doctor_id(self):
        return self.__fk_doctor_id
    def get_visit_id(self):
        return self.__visit_id
    def get_successful(self):
        return self.__successful
    def get_refferal_name(self):
        return self.__refferal_name
    #update
    def update_successful(self,result):
        self.__successful = result
        config = Config()
        con = config.db_conn
        try:

            with con.cursor() as cur:
                qry = 'UPDATE visit SET successful = %s WHERE visit_id = %s'

                cur.execute(qry, (self.__successful, self.__visit_id))
                con.commit()

        finally:

            con.close()
    def update_refferal_name(self,name):
        self.__refferal_name = name
        config = Config()
        con = config.db_conn
        try:

            with con.cursor() as cur:
                qry = 'UPDATE visit SET refferal_name = %s WHERE visit_id = %s'

                cur.execute(qry, (self.__refferal_name, self.__visit_id))
                con.commit()

        finally:

            con.close()
    def delete(self):
        config = Config()
        con= config.db_conn
        try:
            with con.cursor() as cur:
                qry = 'DELETE FROM visit WHERE visit_id = %s'

                cur.execute(qry, (self.__visit_id))
                con.commit()
        finally:

            con.close()
    def to_json(self):
        fields_data = {
            "visit_id" : self.__visit_id,
            "fk_patient_id" : self.__fk_patient_id,
            "fk_doctor_id" : self.__fk_doctor_id,
            "successful"   : self.__successful,
            "refferal_name": self.__refferal_name
        }
        return json.dumps(fields_data)

class Diagnosis:
    def __init__(self,diagnosis_id="",name="",emergency=False):
        self.__name = name
        self.__emergency = emergency
        config = Config()
        con = config.db_conn
        if diagnosis_id == "":
            self.__diagnosis_id = str(uuid.uuid4())
            try:
                with con.cursor() as cur:
                    qry = 'INSERT INTO diagnosis (diagnosis_id, name, emergency)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__diagnosis_id, self.__name, self.__emergency))
                    con.commit()
            finally:
                con.close()
        else:
            self.__diagnosis_id = diagnosis_id
            try:
                with con.cursor() as cur:
                    qry="SELECT * FROM diagnosis WHERE diagnosis_id = '"+ self.__diagnosis_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__name = row["name"]
                        self.__emergency = row["emergency"]
            finally:
                con.close()

    def get_diagnosis_id(self):
        return self.__diagnosis_id
    def get_name(self):
        return self.__name
    def get_emergency(self):
        return self.__emergency
    def update_name(self,name):
        self.__name = name
        config = Config()
        con = config.db_conn
        try:
            with con.cursor() as cur:
                qry = 'UPDATE diagnosis SET name = %s WHERE diagnosis_id = %s'

                cur.execute(qry, (self.__name, self.__diagnosis_id))
                con.commit()

        finally:
            con.close()
    def update_emergency(self, val):
        self.__emergency = val
        config = Config()
        con = config.db_conn
        try:

            with con.cursor() as cur:
                qry = 'UPDATE diagnosis SET emergency = %s WHERE diagnosis_id = %s'

                cur.execute(qry, (self.__emergency, self.__diagnosis_id))
                con.commit()

        finally:

            con.close()
    def delete(self):
        config = Config()
        con = config.db_conn
        try:
            with con.cursor() as cur:
                qry = 'DELETE FROM diagnosis WHERE diagnosis_id = %s'

                cur.execute(qry, (self.__diagnosis_id))
                con.commit()
        finally:

            con.close()
    def to_json(self):
        fields_data = {
            "diagnosis_id" : self.__diagnosis_id,
            "name" : self.__name,
            "emergency" : self.__emergency,
        }
        return json.dumps(fields_data)
class Procedure:
    def __init__(self,procedure_id="",name="",price=0):
        self.__name = name
        self.__price = price
        config = Config()
        con = config.db_conn
        if procedure_id == "":
            self.__procedure_id = str(uuid.uuid4())
            try:
                with con.cursor() as cur:
                    qry = 'INSERT INTO procedure (procedure_id, name, price)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__procedure_id, self.__name, self.__price))
                    con.commit()
            finally:
                con.close()
        else:
            self.__procedure_id = procedure_id
            try:
                with con.cursor() as cur:
                    qry="SELECT * FROM procedure WHERE procedure_id = '" + self.__procedure_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__name = row["name"]
                        self.__price = row["price"]
            finally:
                con.close()

    def get_procedure_id(self):
        return self.__procedure_id
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def update_name(self,name):
        self.__name = name
        config = Config()
        con = config.db_conn
        try:

            with con.cursor() as cur:
                qry = 'UPDATE dianosis SET name = %s WHERE procedure_id = %s'

                cur.execute(qry, (self.__name, self.__procedure_id))
                con.commit()

        finally:

            con.close()
    def update_price(self, val):
        self.__price = val
        config = Config()
        con = config.db_conn
        try:

            with con.cursor() as cur:
                qry = 'UPDATE procedure SET price = %s WHERE procedure_id = %s'

                cur.execute(qry, (self.__price, self.__procedure_id))
                con.commit()

        finally:

            con.close()
    def delete(self):
        config = Config()
        con = config.db_conn
        try:
            with con.cursor() as cur:
                qry = 'DELETE FROM procedure WHERE procedure_id = %s'

                cur.execute(qry, (self.__procedure_id))
                con.commit()
        finally:

            con.close()
    def to_json(self):
        fields_data = {
            "procedure_id" : self.__procedure_id,
            "name" : self.__name,
            "price" : self.__price
        }
        return json.dumps(fields_data)
    
class Testing(unittest.TestCase):
#Implemenent unit tests for the methods that:
#Select a doctor entry from the database and update appropriate instance variables
    def test_select(self):
        temp = Doctor("firsttest", "lasttest", 1)
        testDoc = Doctor(doctor_id = temp.get_doctor_id())
        testDoc.update_age(2)
        testDoc.update_fname("updated")
        testDoc.update_lname("updated")
        self.assertEqual(testDoc.get_age(),2)
        self.assertEqual(testDoc.get_fname(), "updated")
        self.assertEqual(testDoc.get_lname(), "updated")

#Create a new doctor entry
    def test_create(self):
        testDoc = Doctor("firsttest", "lasttest", 1)
        self.assertEqual(testDoc.get_fname, "firsttest")
        self.assertEqual(testDoc.get_lname, "lasttest")
        self.assertEqual(testDoc.get_age(),1)
#Edit/update an existing doctor entry
    def test_update(self):
        testDoc = Doctor("firsttest", "lasttest", 1)
        testDoc.update_age(18)
        testDoc.update_fname("jim")
        testDoc.update_lname("bob")
        self.assertEqual(testDoc.get_age,18)
        self.assertEqual(testDoc.get_fname(),"jim")
        self.assertEqual(testDoc.get_lname(),"bob")
#Delete an existing doctor entry
    #def testDelete(self):
        #ask dimitri idk how to test 
#Make sure that your unit tests are executable → make sure to call unittest.main()

#if __name__ == '__main__':
#    unittest.main()

from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    patient = Patient("Julia", "Garthwaite", 21)
    doctor = Doctor("Mx", "Doctor", 54)
    visit1 = Visit(patient.get_patient_id(),doctor.get_doctor_id(),False,"Ms Refferal")
    visit2 = Visit(patient.get_patient_id(),doctor.get_doctor_id(),True, "None")
    value = "" + patient.to_json() + doctor.to_json(), visit1.to_json(), visit2.to_json()
    return value