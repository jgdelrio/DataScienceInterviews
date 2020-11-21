/*
  We have information about companies in two separate tables:

  TABLE uk_companies
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL

  TABLE usa_companies
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL


  Write a query that select all distinct company names.
*/

SELECT DISTINCT name
FROM (
  SELECT name
  FROM uk_companies
  UNION ALL
  SELECT name from usa_companies
)