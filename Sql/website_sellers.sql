/*
  Imagine that you manage a website like ebay
  where we well multiple items bolonging to multiple sellers.
  Each item belongs to a seller and we want to track the quality of the seller.
  To that purpose each seller has a rating and we have the two following tables:

    TABLE sellers
	  id INTEGER PRIMARY KEY,
	  name VARCHAR(50) NOT NULL,
	  rating INTEGER NOT NULL

	TABLE items
	  id INTEGER PRIMARY KEY,
	  name VARCHAR(50) NOT NULL,
	  sellerId INTEGER REFERENCES sellers(id)

  Write a query that selects for all sellers with rating equal or greater than 8 (ratings are from 0 to 10)
  all the names of the items and their seller.
  The query must return in the 1st column the name of the item and in the 2nd column the name of the seller.
*/

SELECT it.name AS item, se.name AS seller
FROM items it INNER JOIN sellers se
ON it.sellerid = se.id
WHERE se.rating >= 8
