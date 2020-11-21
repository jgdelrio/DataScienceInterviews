/*
  We own a company with the following employee hierarchy.
  We consider that an employee is a manager if other employee
  includes in his/her managerId the first employees id.
  And any manager may or may not also have a manager.

  TABLE employees
    id INTEGER NOT NULL PRIMARY KEY
    managerId INTEGER REFERENCES employees(id)
    name VARCHAR(50) NOT NULL

  Write a query that selects the names of employees
  who are not managers.
*/

SELECT name
FROM employees
WHERE id NOT IN (
  SELECT emp1.Id
  FROM employees emp1
  INNER JOIN employees emp2 ON emp1.id = emp2.managerid
)