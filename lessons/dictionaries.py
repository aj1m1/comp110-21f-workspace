"""Demonstrations of dictionary capabilities."""

# #Declare the type of dictionary
# schools: dict[str, int]
# #intitialize to an empty dictionary
# schools = dict()
# #set a key -value pairing in the dictionary
# schools["UNC"] = 19_400
# schools["Duke"] = 6717
# schools["NCSU"] = 26150

# #print a dictionary literal
# #print(schools)


# #Access a value 
# print(f'UNC has {schools["UNC"]} students')
# #remove a key-value by its key pair from a dictionary
# schools.pop("Duke")

# #Test for the existence of the key
# is_Duke_present: bool = "Duke" in schools
# print(is_Duke_present)
# #update or reassign a key-value pair from
# schools["UNC"] = 20000
# schools["NCSU"] += 200


# print(schools)



#Empty dictionary
schools = {} #same as dict()
# alternatively initialize key-value pairs
schools = {
    "UNC": 19400, 
    "Dukie": 6717,
    "NCSU": 26150
    }
print(schools)
for school in schools:
    print(schools[school])


