from pymongo import MongoClient
import random
import string


class MongoConnect(BaseException):
    def __init__(self):
        self.my_client = MongoClient("mongodb://localhost:27017/")
        self.mydb = self.my_client["store"]
        self.product = self.mydb["products"]

    def insert_one(self):
        try:
            self.product.insert_one({'name': 'pen', 'price': '0.6'})
        except Exception:
            raise
        finally:
            self.my_client.close()

    def insert_many(self):
        try:
            self.product.insert_many([{'name': 'pencil', 'price': '0.2'},
                                      {'name': 'album', 'price': '1.1'},
                                      {'name': 'felt-tip pen', 'price': '1.2'},
                                      {'name': 'book', 'price': '3.6'}])
        except Exception:
            raise
        finally:
            self.my_client.close()

    def find_one(self):
        try:
            product = self.product.find_one({})
            print(product)
        except Exception:
            raise
        finally:
            self.my_client.close()

    def find_many(self):
        try:
            products = self.product.find({})
            for product in products:
                print(product)
        except Exception:
            raise
        finally:
            self.my_client.close()

    def find_one_and_delete(self):
        try:
            self.product.find_one_and_delete({'name': 'pencil'})
        except Exception:
            raise
        finally:
            self.my_client.close()

    def find_one_and_update(self):
        try:
            self.product.find_one_and_update({'name': 'book'}, {'$set': {'name': 'book_update'}})
        except Exception:
            raise
        finally:
            self.my_client.close()

    def delete_one(self):
        try:
            self.product.delete_one({"name": "pencil"})
        except Exception:
            raise
        finally:
            self.my_client.close()

    def delete_many(self):
        try:
            self.product.delete_many({"name": "pencil"})
        except Exception:
            raise
        finally:
            self.my_client.close()

    def drop(self):
        try:
            self.product.drop()
        except Exception:
            raise
        finally:
            self.my_client.close()

    def update_many(self):
        try:
            self.product.update_many({'name': 'book'}, {'$set': {'name': ''.join(random.choice(string.ascii_letters)
                                                                                 for _ in range(10))}})
        except Exception:
            raise
        finally:
            self.my_client.close()
