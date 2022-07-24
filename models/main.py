from mongo.models.product import MongoConnect

if __name__ == '__main__':
    prod = MongoConnect()
    # prod.insert_one()
    # prod.insert_many()
    # prod.find_one()
    prod.find_many()
    # prod.find_one_and_delete()
    # prod.find_one_and_update()
    # prod.delete_one()
    # prod.delete_many()
    # prod.drop()
    # prod.update_many()
