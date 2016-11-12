import sqlite3

def ask_query():
	conn = sqlite3.connect('pets.db')
	c = conn.cursor()
	user_input = raw_input('Please input an ID number: ')
	query = """
		SELECT DISTINCT pet.name, pet.age, pet.breed, pet.dead, person.first_name, person.last_name, person.age
		FROM person
		INNER JOIN person_pet 
		ON person.id = person_pet.person_id
		INNER JOIN pet
		ON pet.id == person_pet.pet_id
		WHERE person.id == ?
	"""
	c.execute(query, (user_input, ))
	rows = c.fetchall()
	if len(rows) > 0:
		results = '{} {}, {} years old'
		print results.format(
			rows[0][4],
			rows[0][5],
			rows[0][6])
		results = '{} {} owned {}, which was a {} year old {}. {} is {}.'
		for row in rows:
			print results.format(
				row[4],
				row[5],
				row[0],
				row[1],
				row[2],
				row[0],
				'alive' if row[3] else 'dead')




if __name__ == '__main__':
	ask_query()
