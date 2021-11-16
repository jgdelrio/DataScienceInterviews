/*
  Write a query that selects the userId and the average
  session duration for each user who has more than one session.

  Sessions are kept in the following table:

  TABLE sessions
    id INTEGER PRIMARY KEY,
    userId INTEGER NOT NULL,
    duration DECIMAL NOT NULL
*/

SELECT userId, avg(duration) as avg_duration
FROM sessions
GROUP BY userid
HAVING COUNT(*) > 1
