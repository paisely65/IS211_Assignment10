CREATE TABLE IF NOT EXISTS artist (
	name TEXT
);

CREATE TABLE IF NOT EXISTS albums (
	name TEXT,
	artist TEXT
);

CREATE TABLE IF NOT EXISTS songs (
	name TEXT,
	album TEXT,
	artist TEXT,
	length INTEGER
);