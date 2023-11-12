from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"])
table.add_column("Type",["Elecrtric", "Fire", "Water", "Grass"])

table.align = "c"

print(table)

