import unittest
from deploy.database.database import DataBase


class TestDataBase(unittest.TestCase):
    def setUp(self):
        self.db = DataBase()

    def test_insertModel(self):
        result = self.db.insertInModel(name="test_model", type="test_type")
        self.assertNotEqual(result, -1, "Insert in Models Table:Error happened")

    def test_insertObject(self):
        result = self.db.insertInObjectTable(category="test_cat", type="test_type", color="test_color")
        self.assertNotEqual(result, -1, "Insert in Objects Table:Error happened")

    def test_insertDetectedObject(self):
        result = self.db.insertInDetectedObject(object_id=1, model_id=1, accuracy=96.3, timestamp=123456)
        self.assertGreaterEqual(result, 0, msg="Insert in DetectedObjects Table:Error happened")

    def test_insertAnomalyObject(self):
        result = self.db.insertInAnomalyObjects(model_id=0, timestamp=25645, accuracy=20)
        self.assertGreaterEqual(result, 0, msg="Insert in DetectedObjects Table:Error happened")


if __name__ == "__main__":
    unittest.main()
