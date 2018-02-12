import sqlite

def najboljsi:
	povezava = sqlite3.connect('podatki.sqlite')
	povezava.execute("""SELECT Users.username, Scores.napake, Scores.beseda
	FROM Scores 
	JOIN Users ON Scores.user_id=Users.id
	ORDER BY Sores.napake
	""")

	return rezultat.fetchmany(10)


def vstavi_novo_igro (user_id, napake, beseda):
	#INSERT INTO Scores
	pass