import os
import sqlite3


class DataBase:
    def __init__(self):

        self.connection()

    def connection(self):
        self.conn = sqlite3.connect(self.__getPath())
        self.cursor = self.conn.cursor()
        self.__objectTabelName = "objects"
        self.__detectedObjectTabelName = "detected_objects"
        self.__modelsTabelName = "models"
        self.__anomalyObjectsDetected = "anomaly_objects"
        self.createTabels()

    def __getPath(self, ):
        path = os.getcwd().split("deploy")[0]
        path = path + "deploy" + os.sep + "files" + os.sep + "recycleB.db"
        if os.sep == "\\":
            path.replace("/", "\\")
        return path

    def createTabels(self):
        try:
            q1 = " create table if not exists {} ( anomaly_id  INTEGER UNIQUE,  timestamp  INTEGER,  accuracy NUMERIC,  model_id  INTEGER,PRIMARY KEY( anomaly_id  AUTOINCREMENT), FOREIGN KEY( model_id ) REFERENCES  models ( model_id));".format(
                "anomaly_objects").format(self.__anomalyObjectsDetected)
            q2 = "create table if not exists  {}  (detected_object_id	INTEGER UNIQUE, accuracy 	NUMERIC, timestamp 	INTEGER, model_id 	INTEGER,  object_id 	TEXT, 	FOREIGN KEY( object_id) REFERENCES objects( object_id), FOREIGN KEY( model_id) REFERENCES models(model_id), PRIMARY KEY(detected_object_id AUTOINCREMENT));".format(
                self.__detectedObjectTabelName)
            q3 = "create table if not exists {} (model_id	INTEGER UNIQUE, model_name 	TEXT, type 	INTEGER, 	PRIMARY KEY( model_id AUTOINCREMENT));".format(
                self.__modelsTabelName)
            q4 = " create table if not exists {} (object_id	INTEGER UNIQUE, category	TEXT, type  TEXT, color	TEXT, PRIMARY KEY(object_id  AUTOINCREMENT)); ".format(
                self.__objectTabelName)
            self.cursor.execute(q1)
            self.cursor.execute(q2)
            self.cursor.execute(q3)
            self.cursor.execute(q4)
        except:
            print("error in create tabel")

    def insertInObjectTable(self, category, type, color):
        try:
            q = "insert into {} ( category ,type,color) values (?,?,?) ".format(self.__objectTabelName)
            res = self.cursor.execute(q, (category, type, color))
            self.conn.commit()
            return res.lastrowid
        except:
            print("error in insertInObjectTable ")
            return -1

    def insertInDetectedObject(self, object_id, model_id, accuracy, timestamp):
        # try:
        q = "insert into {} ( accuracy ,timestamp,model_id,object_id) values (?,?,?,?) ".format(
            self.__detectedObjectTabelName)
        res = self.cursor.execute(q, (accuracy, timestamp, model_id, object_id))
        self.conn.commit()
        return res.lastrowid

    # except:
    #     print("")
    #     return -1

    def insertInModel(self, name, type):
        try:
            q = "insert into {} (model_name ,type) values (?,?) ".format(self.__modelsTabelName)
            res = self.cursor.execute(q, (name, type))
            self.conn.commit()
            return res.lastrowid
        except:
            print("error in insert model")
            return -1

    def insertInAnomalyObjects(self, model_id, timestamp, accuracy):
        try:
            q = "insert into {} ( model_id ,timestamp,accuracy) values (?,?,?) ".format(self.__anomalyObjectsDetected)
            res = self.cursor.execute(q, (model_id, timestamp, accuracy))
            self.conn.commit()
            return res.lastrowid
        except:
            print("")
            return -1

    def getObjects(self):
        pass

    def getModelsId(self, model_name):
        q = "select models.model_id from models where model_name =? "
        self.cursor.execute(q, (model_name,))
        rows = self.cursor.fetchall()
        return rows
