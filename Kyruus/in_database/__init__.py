import os

from flask import Flask, jsonify, request
from in_database import db


# Program & structure influenced heavily by the Flask tutorial
# http://flask.pocoo.org/docs/1.0/tutorial/database/
def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev',
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, 'doctors.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register the database commands
    db.init_app(app)

    from .appointment import apis as appointment_apis
    app.register_blueprint(appointment_apis.bp)

    @app.route('/doctors', methods=['GET'])
    def list_doctors():
        """
        Get all doctors

        :return: List of full doctor rows
        """
        cursor = db.get_db().cursor()

        result = cursor.execute(
            'SELECT id, first_name, last_name '
            'FROM doctors'
        ).fetchall()

        # See https://medium.com/@PyGuyCharles/python-sql-to-json-and-beyond-3e3a36d32853
        doctors = [dict(zip([key[0] for key in cursor.description], row)) for row in result]

        cursor.close()

        return jsonify(doctors), 200

    @app.route('/doctors/<int:doctor_id>', methods=['GET'])
    def list_doctor(doctor_id):
        """
        Get one doctor

        :param doctor_id: The id of the doctor
        :return: Full doctor row
        """
        cursor = db.get_db().cursor()

        result = cursor.execute(
            'SELECT id, first_name, last_name '
            'FROM doctors '
            'WHERE id = ?',
            (doctor_id, )
        ).fetchone()

        if result is None:
            return jsonify({'error_detail': 'Doctor not found'}), 404

        # See https://medium.com/@PyGuyCharles/python-sql-to-json-and-beyond-3e3a36d32853
        doctor = dict(zip([key[0] for key in cursor.description], result))

        cursor.close()

        return jsonify(doctor), 200

    # Note: Must set the content type to JSON. Use something like:
    # curl -X POST -H "Content-Type: application/json" --data '{"first_name": "Joe", "last_name": "Smith"}' http://localhost:5000/doctors
    @app.route('/doctors', methods=['POST'])
    def add_doctor():
        """
        Create a doctor

        :param first_name: The doctor's first name
        "param last_name: The doctor's last name

        :return: The id of the newly created doctor
        """
        req_data = request.get_json()

        try:
            first_name = req_data['first_name']
            last_name = req_data['last_name']
        except KeyError:
            return jsonify({'error_detail': 'Missing required field'}), 400

        try:
            cursor = db.get_db().cursor()

            cursor.execute(
                'INSERT INTO doctors (first_name, last_name) '
                'VALUES (?, ?)',
                (first_name, last_name)
            )

            doctor_id = cursor.lastrowid

            cursor.close()
            db.get_db().commit()
        except Exception as e:
            return jsonify({'error_detail': e.message}), 400

        return jsonify({'id': doctor_id}), 200

    @app.route('/doctors/<int:doctor_id>/locations', methods=['GET'])
    def list_doctor_locations(doctor_id):
        """
        Get the locations for a single doctor

        :param doctor_id: The id of the doctor
        :return: List of full location rows
        """

        cursor = db.get_db().cursor()

        result = cursor.execute(
            'SELECT l.id, l.address '
            'FROM doctor_locations dl '
            'INNER JOIN locations l ON dl.location_id = l.id '
            'WHERE dl.doctor_id = ?',
            (doctor_id,)
        ).fetchall()

        # See https://medium.com/@PyGuyCharles/python-sql-to-json-and-beyond-3e3a36d32853
        locations = [dict(zip([key[0] for key in cursor.description], row)) for row in result]

        cursor.close()

        return jsonify(locations), 200

    return app
