SELECT P.full_name, C.startTime FROM classes C JOIN professors P ON C.professor_id = P.id WHERE C.courseCode = "INF"
DELETE from professors where full_name="Testprofessor"