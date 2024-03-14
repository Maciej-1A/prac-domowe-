liczba = 10
liczba2 = 15
idk = {"buczysalw": "chomik", "liczba":liczba +liczba2,"sex":"analny"}
print(idk["liczba"])
idk["chomik"] = "buczy"
print(idk)
print(idk.get("sex", "kys"))


print("\n----------------")
for el in idk.keys():
    print(el)



print("\n-----------")
print(idk.pop("sex"))
print(idk)