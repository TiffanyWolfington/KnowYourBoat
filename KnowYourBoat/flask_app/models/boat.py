from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Boat:

    db = "solo"

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.serial_number = data['serial_number']
        self.content = data['content']
        self.purchase_date = data['purchase_date']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod

    def save(cls,data):
        query = "INSERT INTO boats (name, serial_number, content, purchase_date, user_id) VALUES (%(name)s,%(serial_number)s,%(content)s,%(purchase_date)s,%(user_id)s);"
        
        return connectToMySQL(cls.db).query_db(query, data)



    @classmethod
    
    def get_all(cls):
        query = "SELECT * FROM boats;"
        results =  connectToMySQL(cls.db).query_db(query)
        all_boats = []
        
        for row in results:

            all_boats.append( cls(row) )
        
        return all_boats
    



    @classmethod

    def get_one(cls,data):

        query = "SELECT * FROM boats WHERE id = %(id)s;"

        results = connectToMySQL(cls.db).query_db(query,data)

        return cls( results[0] )



    @classmethod

    def update(cls, data):
        query = "UPDATE boats SET name=%(name)s, serial_number=%(serial_number)s, content=%(content)s, purchase_date=%(purchase_date)s,updated_at=NOW() WHERE id = %(id)s;"
        
        return connectToMySQL(cls.db).query_db(query,data)
    



    @classmethod
    
    def destroy(cls,data):
        
        query = "DELETE FROM boats WHERE id = %(id)s;"
        
        return connectToMySQL(cls.db).query_db(query,data)




    @staticmethod
    
    def validate_boat(boat):
        
        is_valid = True
        
        if len(boat['name']) < 5:
            is_valid = False
            flash("Product name must be at least 5 characters long.","boat")
        
        if len(boat['serial_number']) < 4:
            is_valid = False
            flash("Serial # must be at least 3 characters long.","boat")
        
        if len(boat['content']) < 3:
            is_valid = False
            flash("IF applicable: Content ID is case sensitive and must be at least 5 characters long.","boat")
        
        if boat['purchase_date'] == "":
            is_valid = False
            flash("Please enter a purchase date.","boat")
        
        return is_valid
