import json


def test_get_all_doctors(client):
    # Test that getting all doctors truly gets them all
    rv = client.get('/doctors')
    assert rv.status_code == 200

    # Can't guarantee order, so test that we get the expected count and fields seem to make sense
    data = json.loads(rv.data)
    assert len(data) == 2
    for field in ['id', 'first_name', 'last_name']:
        assert field in data[0]


def test_get_valid_doctor(client):
    # Test getting a single doctor, successfully
    rv = client.get('/doctors/0')
    assert rv.status_code == 200

    data = json.loads(rv.data)
    assert data['id'] == 0
    assert data['first_name'] == 'Testy'
    assert data['last_name'] == 'McTestFace'


def test_get_invalid_doctor(client):
    # Test getting a single doctor that doesn't exist
    rv = client.get('/doctors/2')
    assert rv.status_code == 404


def test_create_doctor(client):
    # Test creating a real doctor, successfully

    # Note: Flask chokes if you pass in an inline dict; must use json.dumps()
    rv = client.post('/doctors',
                     data=json.dumps(dict(first_name='Elmer', last_name='Hartman')),
                     content_type='application/json')

    assert rv.status_code == 200

    data = json.loads(rv.data)
    assert data['id'] == 2


def test_create_invalid_doctor(client):
    # Test various ways a doctor creation may fail
    rv = client.post('/doctors',
                     data=json.dumps(dict(first_name='Elmer')),
                     content_type='application/json')

    assert rv.status_code == 400

    data = json.loads(rv.data)
    assert data['error_detail'] == 'Missing required field'

    rv = client.post('/doctors',
                     data=json.dumps(dict(last_name='Hartman')),
                     content_type='application/json')

    assert rv.status_code == 400

    data = json.loads(rv.data)
    assert data['error_detail'] == 'Missing required field'
