from app.config.mysqlconnection import connectToMySQL
from datetime import datetime

class Svc:
    db_name = "proyecto_personal"
    def __init__(self,svc_data):
        self.id = svc_data['id']
        self.matricule = svc_data['matricule']
        self.model = svc_data['model']
        self.engine = svc_data['engine']
        self.init_date = svc_data['init_date']
        self.end_date = svc_data['end_date']
        self.tat = svc_data['tat']
        self.movement_time = svc_data['movement_time']
        self.description = svc_data['description']
        self.location = svc_data['location']
        self.user_id = svc_data['user_id']
        self.created_at = svc_data['created_at']
        self.updated_at = svc_data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM aircrafts;"
        results = connectToMySQL(cls.db_name).query_db(query)
        aircraft = []
        for row in results:
            aircraft.append( cls(row))
        return aircraft    

    @classmethod
    def save(cls,data):
        query = "INSERT INTO aircrafts (matricule,model,engine,init_date,end_date,tat,movement_time,description,location,user_id) VALUES (%(matricule)s,%(model)s,%(engine)s,%(init_date)s,%(end_date)s,%(tat)s,%(movement_time)s,%(description)s,%(location)s,%(user_id)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)    
    
    @classmethod
    def check_time(cls, movement_time):
        if isinstance(movement_time, datetime):
            local_now = datetime.now()
            return movement_time < local_now
        else:
            return False

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM aircrafts WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)    