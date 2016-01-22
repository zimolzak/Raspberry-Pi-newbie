CREATE TABLE roomdetails (id INTEGER PRIMARY KEY AUTOINCREMENT, room VARCHAR(25));

CREATE TABLE temperature (id INTEGER PRIMARY KEY AUTOINCREMENT, roomid INTEGER, FOREIGN KEY(roomid) REFERENCES roomdetails(id));

ALTER TABLE temperature ADD COLUMN temperaturec FLOAT(8);

ALTER TABLE temperature ADD COLUMN datetime DATETIME;

INSERT INTO roomdetails (room) VALUES ('Living room');
