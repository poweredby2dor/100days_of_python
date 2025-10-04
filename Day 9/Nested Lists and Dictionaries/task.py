"""
This module contains an exercise for 100 Days of Python
"""
"""
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Print Lille
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

# =Print "D"
print(nested_list[2][1])
"""

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Stuttgart", "Berlin"],
        "total_visits": 5
    },
}

# Print Stuttgart
print(travel_log["Germany"]["cities_visited"][1])
