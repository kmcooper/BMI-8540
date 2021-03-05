-- Create the table for courses, which contains
-- the course identification number (cid),
-- the instructor identification number (iid),
-- the class mode (In-Person, Remote, Hybrid, or In-Person)
-- the semester it is offered, and
-- the year it is offered.
-- cid, semester, and iid uniquely identify a course
-- so that combination is used as primary key
CREATE TABLE course_list(
 cid VARCHAR(20),
 iid INT,
 mode VARCHAR(20),
 semester VARCHAR(8),
 year INT,
 PRIMARY KEY(cid,semester,iid)
);

-- This is the course_list data for all taught BIOI classes in 2021
INSERT INTO course_list VALUES("BIOI 1000",114,"In-person","SPR",2021);
INSERT INTO course_list VALUES("BIOI 1000",113,"In-person","FALL",2021);
INSERT INTO course_list VALUES("BIOI 3500",112,"Online","SPR",2021);
INSERT INTO course_list VALUES("BIOI 1000",113,"Online","SUM",2021);
INSERT INTO course_list VALUES("BIOI 1000",115,"Online","FALL ",2021);
INSERT INTO course_list VALUES("BIOI 2000",111,"Remote","SPR",2021);
INSERT INTO course_list VALUES("BIOI 4890",111,"In-person","SPR",2021);

-- Create the table for instructors, which contains
-- the instructor identification number (iid),
-- their first and last names,
-- the department with which they are formally affiliated,
-- their current academic rank,
-- iid uniquely identifies an instructor
-- so that is used as primary key
CREATE TABLE instructor_list(
 iid INT,
 firstname VARCHAR(20),
 lastname VARCHAR(20),
 dept VARCHAR(8),
 rank VARCHAR(30),
 PRIMARY KEY(iid)
);

INSERT INTO instructor_list VALUES(111,"Kir","Bast","Si2","Professor");
INSERT INTO instructor_list VALUES(115,"Mar","Clar","Si2","Assistant Professor");
INSERT INTO instructor_list VALUES(113,"Kat","Coop","Si2","Assistant Professor");
INSERT INTO instructor_list VALUES(110,"Ann","Fruh","Si2","Professor");
INSERT INTO instructor_list VALUES(112,"Dar","Gher","Si2","Associate Professor");
INSERT INTO instructor_list VALUES(114,"Tyl","Smit","External","Instructor");
INSERT INTO instructor_list VALUES(109,"Hes","Al","CS","Dean");
