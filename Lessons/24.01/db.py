db = {9103976271:("Reina Meinhard", "Memphis, Tennessee"),
4199392609:("Stephanie Bruce", "Greensboro, North Carolina"),
9099459979:("Ermes Angela", "Dallas, Texas"),
6123479367:("Lorenza Takuya", "Indianapolis, Indiana"),
7548993768:("Margarete Quintin", "Raleigh, North Carolina")}

x = 7548993768
if x in db:
    print(f"{db[x][0]} from {db[x][1]}")
else:
    print("not found")

val = db.get(x, "")
if val:
    print(f"{val[0]} from {val[1]}")
else:
    print("not found")

res = f"{db.get(x)[0]} from {db.get(x)[1]}" if db.get(x) else "not found"
print(res)