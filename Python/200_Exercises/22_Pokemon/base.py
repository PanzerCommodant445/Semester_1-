import requests
name = input("please choose a pokimon: ")

pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/" + name).json()

# Use this JSON formatter to better visualize the JSON from the Pokemon website
# https://jsonformatter.org/json-viewer
print(pokemon["name"])
print(pokemon["weight"])
print(pokemon["height"])
print(pokemon["Abilities"])


