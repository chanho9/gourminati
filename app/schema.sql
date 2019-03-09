-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS restaurant;

CREATE TABLE restaurant (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    address TEXT UNIQUE NOT NULL
);
