import sqlite3

dbs = [
	"""
	CREATE TABLE IF NOT EXISTS pet (
		id INTEGER PRIMARY KEY,
		name TEXT,
		breed TEXT,
		age INTEGER,
		dead INTEGER
	);

	""",
	"""
	CREATE TABLE IF NOT EXISTS person_pet (
		person_id INTEGER,
		pet_id INTEGER
	);
	""",
	"""
	CREATE TABLE IF NOT EXISTS person (
		id INTEGER PRIMARY KEY,
		first_name TEXT,
		last_name TEXT,
		age INTEGER
	);
	"""
]


person_tups = [
		(1, 'James', 'Smith', 41),
		(2, 'Diana', 'Greene', 23),
		(3, 'Sara', 'White', 27),
		(4, 'William', 'Gibson', 23)

]

pet_tups = [
		(1, 'Rusty', 'Dalmation', 4, 1),
		(2, 'Bella', 'Alaskan Malamute', 3, 0),
		(3, 'Max', 'Cocker Spaniel', 1, 0),
		(4, 'Rocky', 'Beagle', 7, 0),
		(5, 'Rufus', 'Cocker Spaniel', 1, 0),
		(6, 'Spot', 'Bloodhound', 2, 1)
	]

person_pet_tups = [
		(1, 1),
		(1, 2),
		(2, 3),
		(2, 4),
		(3, 5),
		(4, 6)
	]


insert_queries = [
	"""
		INSERT OR IGNORE INTO pet VALUES (?, ?, ?, ?, ?)
	""",
	"""
		INSERT OR IGNORE INTO person_pet VALUES (?, ?)
	""",
	"""
		INSERT OR IGNORE INTO person VALUES (?, ?, ?, ?)
	"""
]


def make_dbs():
	conn = sqlite3.connect('pets.db')
	c = conn.cursor()
	for query in dbs:
		c.execute(query)
	conn.commit()

def insert_data():
	conn = sqlite3.connect('pets.db')
	c = conn.cursor()
	c.executemany(insert_queries[0], pet_tups)
	c.executemany(insert_queries[1], person_pet_tups)
	c.executemany(insert_queries[2], person_tups)
	conn.commit()


if __name__ == '__main__':
	make_dbs()
	insert_data()