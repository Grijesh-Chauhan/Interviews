-- Everything here will get rolled back at the end of a test run
-- Populate everything with known data

DELETE FROM doctors;
INSERT INTO doctors(id, first_name, last_name) VALUES (0, 'Testy', 'McTestFace');
INSERT INTO doctors(id, first_name, last_name) VALUES (1, 'Julius', 'Hibbert');

DELETE FROM locations;
INSERT INTO locations(id, address) VALUES (0, '1 Park St');
INSERT INTO locations(id, address) VALUES (1, '2 University Ave');

DELETE FROM doctor_locations;
INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (0, 0, 0);
INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (1, 0, 1);
INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (2, 1, 1);
