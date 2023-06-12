travel_log = [
{
  "pais": "Francia",
  "visitas": 12,
  "ciudades": ["Paris", "Lille", "Dijon"]
},
{
  "pais": "Alemania",
  "visitas": 5,
  "ciudades": ["Berlin", "Hamburgo", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_nuevo_pais(pais_visitado, veces_visitado, ciudades_visitadas):
    nuevo_pais = {}
    nuevo_pais["country"] = pais_visitado
    nuevo_pais["visits"] = veces_visitado
    nuevo_pais["cities"] = ciudades_visitadas
    travel_log.append(nuevo_pais)

#🚨 Do not change the code below
add_nuevo_pais("Russia", 2, ["Moscow", "San Petersburgo"])
print(travel_log)