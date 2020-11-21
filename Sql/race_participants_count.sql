/*
  Write a query that returns the number of race participants
  whose first name is Jackson.

  String comparisons should be case sensitive.

  You are given to following data definition:

  TABLE participants
    id INTEGER PRIMARY KEY,
    firstName VARCHAR(30) NOT NULL,
    lastName VARCHAR(30) NOT NULL
*/

SELECT COUNT(*)
FROM participants
WHERE firstname = 'Jackson'
