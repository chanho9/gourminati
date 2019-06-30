-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS restaurant;

CREATE TABLE restaurant (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    address TEXT UNIQUE NOT NULL,
    parking TEXT NOT NULL, 
    cost TEXT NOT NULL,
    room TEXT NOT NULL

);
