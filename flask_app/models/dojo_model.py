from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model #could do from .ninja import Ninja

class Dojo:
    my_db= "dojos_and_ninjas"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod #gets all dojos from database
    def get_all(cls):
        query='''
            SELECT * FROM dojos;
        '''
        results = connectToMySQL(cls.my_db).query_db(query)

        print(results)

        dojo_objects=[]
        for record in results:
            one_dojo= cls(record) # 2 lines culd be done without making one_dojo variable, in one line like: dojo_objects.append(cls(record))
            dojo_objects.append(one_dojo) 

        print("dojo_objects")
            
        return dojo_objects

    @classmethod #add dojo
    def save(cls, data):
        query='''
            INSERT INTO dojos (name) VALUES (%(name)s)
        '''
        result = connectToMySQL(cls.my_db).query_db(query,data)
        return result
    
    @classmethod
    def get_one_and_ninjas(cls,data):
        query ="""
            SELECT * From dojos
            LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
            WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL("dojos_and_ninjas").query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            one_ninja = {
                        "id": row['ninjas.id'],
                        "first_name": row['first_name'],
                        "last_name": row['last_name'],
                        "age": row['age'],
                        "created_at": row['ninjas.created_at'],
                        "updated_at": row['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja_model.Ninja(one_ninja))
        return dojo