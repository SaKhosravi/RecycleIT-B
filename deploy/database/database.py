import os
import sqlite3


class DataBase:
    def __init__(self):
        print("database")

        self.connection()

    def connection(self):
        self.conn = sqlite3.connect(self.__getPath())
        self.cursor = self.conn.cursor()
        self.createTabels()

    def __getPath(self, ):
        path = os.getcwd().split("gui")[0]
        path = path + os.sep + "files" + os.sep + "recycleB.db"
        if os.sep == "\\":
            path.replace("/", "\\")
        return path

    def createTabels(self):
        try:
            q1 = " create table if not exists anomaly_objects ( anomaly_id  INTEGER UNIQUE,  timestamp  INTEGER,  accuracy NUMERIC,  model_id  INTEGER,PRIMARY KEY( anomaly_id  AUTOINCREMENT), FOREIGN KEY( model_id ) REFERENCES  models ( model_id));"
            q2 = "create table if not exists  detected_objects  (detected_object_id	INTEGER UNIQUE, accuracy 	NUMERIC, timestamp 	INTEGER, model_id 	INTEGER,  object_id 	TEXT, 	FOREIGN KEY( object_id) REFERENCES objects( object_id), FOREIGN KEY( model_id) REFERENCES models(model_id), PRIMARY KEY(detected_object_id AUTOINCREMENT));"
            q3 = "create table if not exists models (model_id	INTEGER UNIQUE, model_name 	TEXT, type 	INTEGER, 	PRIMARY KEY( model_id AUTOINCREMENT));"
            q4 = " create table if not exists objects (object_id	INTEGER UNIQUE,category	TEXT, type  TEXT, color	TEXT, PRIMARY KEY(object_id  AUTOINCREMENT)); "
            self.cursor.execute(q1)
            self.cursor.execute(q2)
            self.cursor.execute(q3)
            self.cursor.execute(q4)
        except:
            print("error in create tabel")

    def insertInObjectTable(self, category, type, color):
        pass

    def insertInDetectedObject(self, object_id, model_id, accuracy, timestamp):
        pass

    def insertInModel(self, name, type):
        pass

    def insertInAnomalyObject(self, model_id, timestamp, accuracy):
        pass

    def getObjects(self):
        pass

    def getModels(self, ):
        pass
