import sqlite3

def create_db(db):
	conn = sqlite3.connect(db)
	cur = conn.cursor()

	cur.execute("""CREATE TABLE IF NOT EXISTS areas (
		id INTEGER PRIMARY KEY NOT NULL,
		name TEXT NOT NULL)""")

	cur.execute("""CREATE TABLE IF NOT EXISTS types (
		id TEXT PRIMARY KEY NOT NULL,
		name TEXT NOT NULL)""")

	cur.execute("""CREATE TABLE IF NOT EXISTS addresses (
		id INTEGER PRIMARY KEY NOT NULL,
		raw TEXT NOT NULL)""")

	cur.execute("""CREATE TABLE IF NOT EXISTS employers (
		id INTEGER PRIMARY KEY NOT NULL,
		name TEXT NOT NULL)""")

	cur.execute("""CREATE TABLE IF NOT EXISTS schedules (
		id TEXT PRIMARY KEY NOT NULL,
		name TEXT NOT NULL)""")

	cur.execute("""CREATE TABLE IF NOT EXISTS vacancies (
		id INTEGER PRIMARY KEY NOT NULL,
		name TEXT NOT NULL,
		description TEXT NOT NULL,
		area_id INTEGER NOT NULL,
		type_id TEXT NOT NULL,
		address_id INTEGER,
		salary_from INTEGER,
		salary_to INTEGER,
		currency TEXT,
		gross TEXT,
		published_at TEXT,
		archived TEXT,
		employer_id INTEGER NOT NULL,
		schedule_id TEXT NOT NULL,
		FOREIGN KEY (area_id) REFERENCES areas (id) ON DELETE CASCADE,
		FOREIGN KEY (type_id) REFERENCES types (id) ON DELETE CASCADE,
		FOREIGN KEY (address_id) REFERENCES addresses (id) ON DELETE CASCADE,
		FOREIGN KEY (employer_id) REFERENCES employers (id) ON DELETE CASCADE,
		FOREIGN KEY (schedule_id) REFERENCES schedules (id) ON DELETE CASCADE)""")

	conn.commit()
	cur.close()
	conn.close()
	

def add_vacancy(db, vacancy):
	conn = sqlite3.connect(db)
	cur = conn.cursor()

	cur.execute("""INSERT OR IGNORE INTO areas VALUES (?, ?)""",
		(vacancy['area']['id'], 
			vacancy['area']['name']))

	cur.execute("""INSERT OR IGNORE INTO types VALUES (?, ?)""",
		(vacancy['type']['id'], 
			vacancy['type']['name']))
	
	cur.execute("""INSERT OR IGNORE INTO addresses VALUES (?, ?)""",
		(vacancy['address']['id'], 
			vacancy['address']['raw']))

	cur.execute("""INSERT OR IGNORE INTO employers VALUES (?, ?)""",
		(vacancy['employer']['id'], 
			vacancy['employer']['name']))

	cur.execute("""INSERT OR IGNORE INTO schedules VALUES (?, ?)""",
		(vacancy['schedule']['id'], 
			vacancy['schedule']['name']))

	cur.execute("""INSERT OR IGNORE INTO vacancies VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
		(vacancy['id'], 
			vacancy['name'], 
			vacancy['description'], 
			vacancy['area']['id'], 
			vacancy['type']['id'], 
			vacancy['address']['id'], 
			vacancy['salary']['from'], 
			vacancy['salary']['to'], 
			vacancy['salary']['currency'], 
			vacancy['salary']['gross'], 
			vacancy['published_at'], 
			vacancy['archived'], 
			vacancy['employer']['id'], 
			vacancy['schedule']['id']))

	conn.commit()
	cur.close()
	conn.close()
