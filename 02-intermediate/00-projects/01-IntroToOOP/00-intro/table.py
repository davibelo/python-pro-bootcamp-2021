# importing PrettyTable class from prettytable package
from prettytable import PrettyTable

table = PrettyTable()

# using add_column method
table.add_column("pokemon name", ["pikachu", "psiduck", "chamander"])
table.add_column("pokemon type", ["electric", "psi", "fire"])

# accessing and changing attributes
print(table.align)
table.align = "l"
print(table.align)

# printing table
print(table)