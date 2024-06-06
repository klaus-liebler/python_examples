BEGIN TRANSACTION;
DROP TABLE IF EXISTS "classes";
CREATE TABLE IF NOT EXISTS "classes" (
	"id"	INTEGER,
	"courseCode"	TEXT NOT NULL,
	"dayOfWeek"	INTEGER NOT NULL,
	"startTime"	timestamp NOT NULL,
	"endTime"	timestamp NOT NULL,
	"professor_id"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("professor_id") REFERENCES "professors"("id")
);
DROP TABLE IF EXISTS "professors";
CREATE TABLE IF NOT EXISTS "professors" (
	"id"	INTEGER,
	"full_name"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	PRIMARY KEY("id")
);
INSERT INTO "classes" VALUES (1,'INF',2,'11:45','13:15',1);
INSERT INTO "classes" VALUES (2,'MechSys',1,'19:00','21:00',2);
INSERT INTO "classes" VALUES (3,'RT1',4,'14:00','17:15',1);
INSERT INTO "classes" VALUES (4,'RT2',3,'0:00','24:00',2);
INSERT INTO "professors" VALUES (1,'Liebler, Klaus','k.liebler@hs-osnabrueck.de');
INSERT INTO "professors" VALUES (2,'Niemeyer, Philip','p.niemeyer@hs-osnabrueck.de');
INSERT INTO "professors" VALUES (3,'Testprofessor 1','test1@hs-osnabrueck.de');
INSERT INTO "professors" VALUES (4,'Testprofessorin 1','test2@hs-osnabrueck.de');
COMMIT;
