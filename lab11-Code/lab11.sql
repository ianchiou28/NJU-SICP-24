.read lab11_data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = 'blue' AND pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = 'blue' AND pet = 'dog';

CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(*) = 1;


CREATE TABLE matchmaker AS
  SELECT p1.pet, p1.song, p1.color,p2.color FROM students AS p1, students AS p2 WHERE p1.time < p2.time AND p1.song = p2.song AND p1.pet = p2.pet;


CREATE TABLE sevens AS
  SELECT seven FROM students, numbers WHERE number = 7 AND numbers."7" = "True" AND students.time = numbers.time;


CREATE TABLE avg_difference AS
  SELECT ROUND(AVG(ABS(number-smallest))) FROM students;

