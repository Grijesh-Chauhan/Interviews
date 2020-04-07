import datetime

from flask import Blueprint, request
from flask_restful import Resource, Api, abort, reqparse

from in_database.db import get_db
from . import utils

bp = Blueprint('slots', __name__, url_prefix='/slots')
api = Api(bp)
api.representations['application/json'] = utils.output_json

parser = reqparse.RequestParser()
parser.add_argument('booked')

class SlotsAPIView(Resource):
    
    Sql_GetById = "SELECT * FROM slots WHERE id = ?"

    def get_slot(self, id):
        db = get_db()
        cursor = db.execute(SlotsAPIView.Sql_GetById, (id, ))
        slot = cursor.fetchone()
        if slot is None:
            abort(404, message=f"slot is with {id} does not exists")
        if cursor.fetchone() is not None:
            # http-500 justified ?!!
            abort(500, message=f"slot is with {id} does not exists")
        return slot

    def get(self, id):
        """
        curl http://localhost:5000/slots/<id>
        """
        slot = self.get_slot(id)
        return dict(zip(slot.keys(), slot))

class SlotBookAPI(SlotsAPIView):

    Sql_BookByID = """UPDATE slots 
                      SET booked = ?
                      WHERE id = ?
                   """
    def parse_boolean(self, booked):
        try:
            if booked == 1 or booked.lower() == "true":
                return True
            if booked == 0 or booked.lower() == "false":
                return False
        except AttributeError:
            pass
        abort(422, message="Booked should be True or False")

    def get(self, id):
        slot = self.get_slot(id)
        return dict(booked=slot['booked'])
        
    def update(self, id, booked):
        db = get_db()
        db.execute(SlotBookAPI.Sql_BookByID, (booked, id))
        db.commit()
    
    def put(self, id):
        # FIXME handel race issue!!
        """
        curl http://localhost:5000/slots/1/book   -d "booked=True" -X PUT -v 
        """
        slot = self.get_slot(id)
        if slot['booked'] == 'blocked':
            abort(422, message="slot can not be booked!")
                        
        booked = self.parse_boolean(parser.parse_args()["booked"])
        booked = 'booked' if booked else 'cancel'
        if booked == 'booked':
            if slot['booked'] == 'booked':
                abort(422, message="slot is already booked!")
            if slot['booked'] == 'available':
                self.update(id, booked)
        if booked == 'cancel':
            if slot['booked'] == 'available':
                abort(422, message="bad request!")
            if slot['booked'] == 'booked':
                self.update(id, 'available')
                
        return {'detail': f"slot {booked} successfully"}


class SlotsListAPIView(Resource):
    # FIXME pagination
    # FIXME Join With Doctor and Location tables to display names
    Sql_SelectAll = """SELECT * FROM slots WHERE day = ?"""
    Sql_SelectByDoctorID = """
SELECT slots.*
FROM slots
JOIN doctor_locations
    ON slots.doctor_locations_id = doctor_locations.id
WHERE slots.day = ? and doctor_locations.doctor_id = ?
"""

    def get_slots(self, doctor_id=None):
        today = datetime.datetime.utcnow().date()        
        db = get_db()
        if doctor_id is None:
            slots = db.execute(SlotsListAPIView.Sql_SelectAll, [today]).fetchall()
        else:
            slots = db.execute(SlotsListAPIView.Sql_SelectByDoctorID, 
                               [today, doctor_id]
                              ).fetchall()
        return slots
        
    def string_to_datetime(self, time):
        hours, minutes, *seconds = time.split(":")
        now = datetime.datetime.utcnow()
        return datetime.datetime(now.year, now.month, now.day, int(hours), int(minutes))
            
    def get(self):
        """
        curl http://localhost:5000/slots
        curl http://localhost:5000/slots?doctor_id=1
        """
        doctor_id = request.args.get('doctor_id')
        slots = self.get_slots(doctor_id)
        return [dict(zip(slot.keys(), slot)) for slot in slots]        
        
    def post(self):
        """ 
        curl http://localhost:5000/slots -d  '{"start": "03:00:00", "end": "03:30:00", "doctor_locations_id": 1 }' -H "Content-Type:application/json" -X POST        
        """
        args = request.json
        args['start'] = self.string_to_datetime(args['start'])
        args['end'] = self.string_to_datetime(args['end'])
        db = get_db()
        doctor_location = db.execute("""
            select *
            from doctor_locations
            where id = ?
        """, [int(args['doctor_locations_id'])]).fetchone()        
        if doctor_location is None:
            abort(422, message="Invalid (doctor, location) pair!")

        doctor_id = doctor_location['doctor_id']

        slots = self.get_slots(doctor_id)
        for slot in slots:
            start = self.string_to_datetime(slot['start'])
            end = self.string_to_datetime(slot['end'])
            overlaps = (start <= args['start'] <= end or
                        args['start'] <= start <= args['end']
                       )
            if overlaps:
                abort(400, message="New Slot overlaps existing slot")
                
        db.execute("""
            INSERT INTO 
                slots (start, end, doctor_locations_id)
            VALUES
                (?, ?, ?)
        """, (args['start'].strftime("%H:%M:%S"), 
              args['end'].strftime("%H:%M:%S"), 
              args['doctor_locations_id']
             )
        )
        db.commit()
        return {'detail': "slot successfully created"}
        
                                        
api.add_resource(SlotsAPIView, '/<int:id>')
api.add_resource(SlotBookAPI, '/<int:id>/book')
api.add_resource(SlotsListAPIView, '')


