/*
  A table containing the students enrolled in a course has
  incorrect data in records with ids between 40 and 100 (inclusive).

  This is the definition of the table:

    TABLE course_enrollments
      id INTEGER NOT NULL PRIMARY KEY
      year INTEGER NOT NULL
      studentId INTEGER NOT NULL

  Write a query that updates the field 'year' of every faulty record to 2019.
*/

UPDATE course_enrollments
SET year = 2019
WHERE id BETWEEN 40 AND 100
