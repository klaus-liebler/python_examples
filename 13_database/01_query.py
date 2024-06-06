import sqlite3
conn = sqlite3.connect('profs.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM professors'):
    print(row)
    print(row[2])

courseCode = input("Welchen Kurs suchen Sie?") 
c.execute('SELECT P.full_name, C.startTime FROM classes C JOIN professors P ON C.professor_id = P.id WHERE C.courseCode = ?', (courseCode,))
#c.execute('SELECT P.full_name, C.startTime FROM classes C JOIN professors P ON C.professor_id = P.id WHERE C.courseCode = "' + courseCode+'"')
print(c.fetchone())

#t = ("Testprofessor", "t@hsos.de")
#c.execute("INSERT INTO professors VALUES (NULL,?,?)", t)

conn.commit()
conn.close()