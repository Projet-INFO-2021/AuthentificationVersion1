import sqlite3

conn = sqlite3.connect('identification')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS identification(
    id INTEGER AUTO INCREMENT UNIQUE,
    idPersonne_Ext INTEGER ,
    Mdp TEXT,
    PRIMARY KEY (id)
)
""")
conn.commit() 
cursor.execute("""
INSERT INTO identification(idPersonne_Ext, Mdp) VALUES(?, ?)""", (34041, "Chocolat"))
cursor.execute("""SELECT idPersonne_Ext, Mdp FROM identification""")
user1 = cursor.fetchone()
print(user1)

print("Entrer votre identifiant")
id=input()

print("Entrer votre mot de passe")
motdepasse=input()
def comparaison(id, motdepasse):
    cursor.execute("SELECT * FROM identification WHERE idPersonne_Ext = " + str(id))
    resultat = list(cursor)
    if len(resultat) == 0 :
        return "identifiant ou mot de passe incorrect"
    elif resultat[0][1]==str(motdepasse) :
        return "mot de passe correct"
    return "identifiant ou mot de passe incorrect"

print(comparaison(id,motdepasse))