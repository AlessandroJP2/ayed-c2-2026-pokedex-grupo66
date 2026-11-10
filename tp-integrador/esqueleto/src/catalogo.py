import src

#Se crea un diccionario con los datos de cada pokemon

Bulbasaur = {
    "id": 1,
    "tipo1": "Planta",
    "tipo2": "Veneno",
    "hp": 45,
    "ataque": 49,
    "defensa": 49,
    "velocidad": 45,
    "generacion": 1
}

Ivysaur = {
    "id": 2,
    "tipo1": "Planta",
    "tipo2": "Veneno",
    "hp": 60,
    "ataque": 62,
    "defensa": 63,
    "velocidad": 60,
    "generacion": 1  
}

Venusaur = {
    "id": 3,
    "tipo1": "Planta",
    "tipo2": "Veneno",
    "hp": 80,
    "ataque": 82,
    "defensa": 83,
    "velocidad": 80,
    "generacion": 1
}


Charmander = {
    "id": 4,
    "tipo1": "Fuego",
    "tipo2": "Ninguno",
    "hp": 39,
    "ataque": 52,
    "defensa": 49,
    "velocidad": 45,
    "generacion": 1
}

Charmeleon = {
    "id": 5,
    "tipo1": "Fuego",
    "tipo2": "Ninguno",
    "hp": 58,
    "ataque": 64,
    "defensa": 58,
    "velocidad": 65,
    "generacion": 1
}

Charizard = {
    "id": 6,
    "tipo1": "Fuego",
    "tipo2": "Volador",
    "hp": 78,
    "ataque": 84,
    "defensa": 78,
    "velocidad": 100,
    "generacion": 1
}

Squirtle = {
    "id": 7,
    "tipo1": "Agua",
    "tipo2": "Ninguno",
    "hp": 44,
    "ataque": 48,
    "defensa": 65,
    "velocidad": 43,
    "generacion": 1
}

Wartortle = {
    "id": 8,
    "tipo1": "Agua",
    "tipo2": "Ninguno",
    "hp": 59,
    "ataque": 63,
    "defensa": 80,
    "velocidad": 58,
    "generacion": 1
}

Blastoise = {
    "id": 9,
    "tipo1": "Agua",
    "tipo2": "Ninguno",
    "hp": 79,
    "ataque": 83,
    "defensa": 100,
    "velocidad": 78,
    "generacion": 1
}

Larvitar = {
    "id": 212,
    "tipo1": "Tierra",
    "tipo2": "Roca",
    "hp": 50,
    "ataque": 64,
    "defensa": 50,
    "velocidad": 41,
    "generacion": 2
}
Pupitar = {
    "id": 213,
    "tipo1": "Tierra",
    "tipo2": "Roca",
    "hp": 70,
    "ataque": 84,
    "defensa": 70,
    "velocidad": 51,
    "generacion": 2  
}

Tyranitar = {
    "id": 214,
    "tipo1": "Tierra",
    "tipo2": "Roca",
    "hp": 100,
    "ataque": 134,
    "defensa": 110,
    "velocidad": 61,
    "generacion": 2
}

Dratini = {
    "id": 147,
    "tipo1": "Dragón",
    "tipo2": "Ninguno",
    "hp": 41,
    "ataque": 64,
    "defensa": 45,
    "velocidad": 50,
    "generacion": 1
}

Dragonair = {
    "id": 148,
    "tipo1": "Dragón",
    "tipo2": "Ninguno",
    "hp": 61,
    "ataque": 84,
    "defensa": 65,
    "velocidad": 70,
    "generacion": 1
}

Dragonite = {
    "id": 149,
    "tipo1": "Dragón",
    "tipo2": "Volador",
    "hp": 91,
    "ataque": 134,
    "defensa": 95,
    "velocidad": 80,
    "generacion": 1
}


Mewtwo = {
    "id": 150,
    "tipo1": "Psíquico",
    "tipo2": "Ninguno",
    "hp": 106,
    "ataque": 110,
    "defensa": 90,
    "velocidad": 130,
    "generacion": 1
}

Mew = {
    "id": 151,
    "tipo1": "Psíquico",
    "tipo2": "Ninguno",
    "hp": 100,
    "ataque": 100,
    "defensa": 100,
    "velocidad": 100,
    "generacion": 1
}

#El siguiente diccionario contiene diccionarios con los datos de cada pokemon
Pokedex = {"Bulbasaur": Bulbasaur, "Ivysaur": Ivysaur, "Venusaur": Venusaur, "Charmander": Charmander, "Charmeleon": Charmeleon, "Charizard": Charizard, "Squirtle": Squirtle, "Wartortle": Wartortle, "Blastoise": Blastoise, "Dratini": Dratini, "Dragonair": Dragonair, "Dragonite": Dragonite, "Mewtwo": Mewtwo, "Mew": Mew, "Larvitar": Larvitar, "Pupitar": Pupitar, "Tyranitar": Tyranitar}

print(Pokedex)
