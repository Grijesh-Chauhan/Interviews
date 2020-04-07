drop table if exists slots;


create table slots (
  id integer primary key autoincrement,
  day date default (date('now', 'localtime')),
  start time not null,
  end time not null,
  booked text default "available",
    -- available
    -- booked
    -- cancelled -- canceling should mark available back
    -- blocked
  doctor_locations_id integer not null,
  foreign key (doctor_locations_id) references doctor_locations (id)
);

insert into
    slots(id, day, 
              start, 
              end, 
              doctor_locations_id
         )
values
    (1, date('now', 'localtime'), 
        time('now', 'localtime'), 
        time('now', 'localtime', '+30 minutes'),
        0
    ),
    
    (2, date('now', 'localtime'), 
        time('now', 'localtime', '+30 minutes'),
        time('now', 'localtime', '+60 minutes'),
        1
    ),
    
    (3, date('now', 'localtime'), 
        time('now', 'localtime', '+60 minutes'),
        time('now', 'localtime', '+120 minutes'),
        2
    )
;


insert into
    slots(id, day, start, end, booked, doctor_locations_id)
values
    (4, date('now', 'localtime'), time('now', 'localtime', '+120 minutes'),
                                  time('now', 'localtime', '+150 minutes'),
                                  'blocked',
                                  3
    )
;







