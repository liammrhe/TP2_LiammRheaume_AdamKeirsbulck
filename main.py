# lecture du fichier
def charger_pokémons_csv(fichier):
    with open("pokemon.csv", "r") as f:
        lignes = f.readlines()

        # stockage des pokemons
        pokemons = {}

        # separation des pokemons
        for element in lignes:
            save = (element.strip().split(","))

            # stats str to int
            stats = [int(element) for element in save[1:]]


            # stockage des pokemons
            pokemons[save[0]] = stats

        return pokemons


# tests
pkmn = charger_pokémons_csv("pokemon.csv")
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")

pkmn = charger_pokémons_csv("pokemon.csv")
print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))



