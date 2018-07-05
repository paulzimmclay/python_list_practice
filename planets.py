planet_list = ["Mercury", "Mars"]
print(planet_list)

# Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")
print(planet_list)

# Use the extend() method to add another list of the last two planets in our solar system to the end of the list
planet_list.extend(["Uranus", "Neptune"])
print(planet_list)

# Use insert() to add Earth and Venus in the correct order
planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")
print(planet_list)

# Use append again to add Pluto to the end of the list
planet_list.append("Pluto")
print(planet_list)

# Slice the list in order to get the rocky planets into a new list called rocky_planets
rocky_planets = planet_list[0:4]
print(rocky_planets)

# Use del to remove pluto from the end of the list
del(planet_list[8])
# Using Remove, which deletes the first matching value:
# planet_list.remove("Pluto")
print(planet_list)