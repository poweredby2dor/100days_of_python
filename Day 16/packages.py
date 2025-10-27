"""
This module contains an exercise for 100 Days of Python
"""

# Tables in ASCII
from prettytable import PrettyTable
# Documentation for PrettyTables: https://pypi.org/project/prettytable/

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"


print(f"\n{table}")
