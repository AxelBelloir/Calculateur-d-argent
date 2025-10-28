import sqlite3
def main():
  commande = 0
  while commande != "3":
    print()
    print("1 - Modifier la base de donnee")
    print("2 - Voir l'argent total")
    print()
    commande = input("Entrez une commande : ")
    if commande == "1":
      print()
      print("1 - Ajouter une piece ou un billet")
      print("2 - Supprimer une piece ou un billet")
      print()
      commande = input("Entrez une commande : ")
      conn = sqlite3.connect("data.db")
      c = conn.cursor()
      c.execute("""CREATE TABLE IF NOT EXISTS data (
        id TEXT,
        uncent INTEGER,
        deuxcent INTEGER,
        cinqcent INTEGER,
        dixcent INTEGER,
        vingtcent INTEGER,
        cinquantecent INTEGER,
        uneuro INTEGER,
        deuxeuro INTEGER,
        cinqeuro INTEGER,
        dixeuro INTEGER,
        vingteuro INTEGER,
        cinquanteeuro INTEGER,
        centeuro INTEGER,
        cinqcenteuro INTEGER
      )""")
      conn.commit()
      c.execute("INSERT INTO data (id,uncent,deuxcent,cinqcent,dixcent,vingtcent,cinquantecent,uneuro,deuxeuro,cinqeuro,dixeuro,vingteuro,cinquanteeuro,centeuro,cinqcenteuro) VALUES (?,0,0,0,0,0,0,0,0,0,0,0,0,0,0)",("Axel",))
      conn.commit()
      if commande =="1":
        print()
        print("1 - 1 cent")
        print("2 - 2 cent")
        print("3 - 5 cent")
        print("4 - 10 cent")
        print("5 - 20 cent")
        print("6 - 50 cent")
        print("7 - 1 euro")
        print("8 - 2 euro")
        print("9 - 5 euro")
        print("10 - 10 euro")
        print("11 - 20 euro")
        print("12 - 50 euro")
        print("13 - 100 euro")
        print("14 - 500 euro")
        print()
        Type = input("Entrez la piece ou le billet : ")
        print()
        Num = int(input("Entrez le nombre de piece ou de billet : "))
        c.execute("SELECT * FROM data")
        data = c.fetchall()
        id = "Axel"
        if Type == "1":
          data = data[0][1]
          data = data + Num
          c.execute("UPDATE data SET uncent = ? WHERE id = ?", (data,id,))
          conn.commit()
        elif Type == "2":
          data = data[0][2]
          data = data + Num
          c.execute("UPDATE data SET deuxcent = ? WHERE id = ?", (data,id,))
          conn.commit()
        elif Type == "3":
          data = data[0][3]
          data = data + Num
          c.execute("UPDATE data SET cinqcent = ? WHERE id = ?", (data,id,))
          conn.commit()
        elif Type == "4":
          data = data[0][4]
          data = data + Num
          c.execute("UPDATE data SET dixcent = ? WHERE id = ?", (data,id,))
          conn.commit()
        elif Type == "5":
          data = data[0][5]
          data = data + Num
          c.execute("UPDATE data SET vingtcent = ? WHERE id = ?", (data,id,))
          conn.commit()
        elif Type == "6":
          data = data[0][6]
          data = data + Num
          c.execute("UPDATE data SET cinquantecent = ? WHERE id = ?", (data,id))
          conn.commit()
        elif Type == "7":
          data = data[0][7]
          data = data + Num
          c.execute("UPDATE data SET uneuro = ? WHERE id = ?", (data,id,))
          conn.commit()
        elif Type == "8":
          data = data[0][8]
          data = data + Num
          c.execute("UPDATE data SET deuxeuro = ? WHERE id = ?", (data,id,))
          conn.commit()
        elif Type == "9":
          data = data[0][9]
          data = data + Num
          c.execute("UPDATE data SET cinqeuro = ? WHERE id = ?", (data,id,))
          conn.commit()
        elif Type == "10":
          data = data[0][10]
          data = data + Num
          c.execute("UPDATE data SET dixeuro = ? WHERE id = ?", (data,id,))
          conn.commit()
        elif Type == "11":
          data = data[0][11]
          data = data + Num
          c.execute("UPDATE data SET vingteuro = ? WHERE id = ?", (data,id,))
          conn.commit()
        elif Type == "12":
          data = data[0][12]
          data = data + Num
          c.execute("UPDATE data SET cinquanteeuro = ? WHERE id = ?", (data,id,))
          conn.commit()
        elif Type == "13":
          data = data[0][13]
          data = data + Num
          c.execute("UPDATE data SET centeuro = ? WHERE id = ?", (data,id,))
          conn.commit()
        elif Type == "14":
          data = data[0][14]
          data = data + Num
          c.execute("UPDATE data SET cinqcenteuro = ? WHERE id = ?", (data,id,))
          conn.commit()
        else:
          print("Erreur : Commande Inconnue")
        conn.close()
      elif commande == "2":
        print()
        print("1 - 1 cent")
        print("2 - 2 cent")
        print("3 - 5 cent")
        print("4 - 10 cent")
        print("5 - 20 cent")
        print("6 - 50 cent")
        print("7 - 1 euro")
        print("8 - 2 euro")
        print("9 - 5 euro")
        print("10 - 10 euro")
        print("11 - 20 euro")
        print("12 - 50 euro")
        print("13 - 100 euro")
        print("14 - 500 euro")
        print()
        Type = input("Entrez la piece ou le billet : ")
        print()
        Num = int(input("Entrez le nombre de piece ou de billet : "))
        c.execute("SELECT * FROM data")
        data = c.fetchall()
        id = "Axel"
        if Type == "1":
          data = data[0][1]
          data = data - Num
          c.execute("UPDATE data SET uncent = ? WHERE id = ?", (data,id))
          conn.commit()
        elif Type == "2":
          data = data[0][2]
          data = data - Num
          c.execute("UPDATE data SET deuxcent = ? WHERE id = ?", (data,id))
          conn.commit()
        elif Type == "3":
          data = data[0][3]
          data = data - Num
          c.execute("UPDATE data SET cinqcent = ? WHERE id = ?", (data,id))
          conn.commit()
        elif Type == "4":
          data = data[0][4]
          data = data - Num
          c.execute("UPDATE data SET dixcent = ? WHERE id = ?", (data,id))
          conn.commit()
        elif Type == "5":
          data = data[0][5]
          data = data - Num
          c.execute("UPDATE data SET vingtcent = ? WHERE id = ?", (data,id))
          conn.commit()
        elif Type == "6":
          data = data[0][6]
          data = data - Num
          c.execute("UPDATE data SET cinquantecent = ? WHERE id = ?", (data,id))
          conn.commit()
        elif Type == "7":
          data = data[0][7]
          data = data - Num
          c.execute("UPDATE data SET uneuro = ? WHERE id = ?", (data,id))
          conn.commit()
        elif Type == "8":
          data = data[0][8]
          data = data - Num
          c.execute("UPDATE data SET deuxeuro = ? WHERE id = ?", (data,id))
          conn.commit()
        elif Type == "9":
          data = data[0][9]
          data = data - Num
          c.execute("UPDATE data SET cinqeuro = ? WHERE id = ?", (data,id))
          conn.commit()
        elif Type == "10":
          data = data[0][10]
          data = data + Num
          c.execute("UPDATE data SET dixeuro = ? WHERE id = ?", (data,id))
          conn.commit()
        elif Type == "11":
          data = data[0][11]
          data = data - Num
          c.execute("UPDATE data SET vingteuro = ? WHERE id = ?", (data,id))
          conn.commit()
        elif Type == "12":
          data = data[0][12]
          data = data - Num
          c.execute("UPDATE data SET cinquanteeuro = ? WHERE id = ?", (data,id))
          conn.commit()
        elif Type == "13":
          data = data[0][13]
          data = data - Num
          c.execute("UPDATE data SET centeuro = ? WHERE id = ?", (data,id))
          conn.commit()
        elif Type == "14":
          data = data[0][14]
          data = data - Num
          c.execute("UPDATE data SET cinqcenteuro = ? WHERE id = ?", (data,id))
          conn.commit()
        else:
          print("Erreur : Commande Inconnue")
    elif commande == "2":
      conn = sqlite3.connect("data.db")
      c = conn.cursor()
      c.execute("SELECT * FROM data")
      data = c.fetchall()
      valeurList = [0,0.01,0.02,0.05,0.1,0.2,0.5,1,2,5,10,20,50,100,500]
      valeurTotal = 0
      index = 1
      while index < 15:
        valeur = data[0][index] * valeurList[index]
        valeurTotal += valeur
        index += 1
      print(valeurTotal)
main()
