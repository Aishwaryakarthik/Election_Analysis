counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])   
for county in counties_dict:
    print(counties_dict.get(county)) 
for county,voters in counties_dict.items():
    print(county,voters)
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Jefferson","registered_voters": 432438})
voting_data
for county,voters in counties_dict.items():
    print(county,voters)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for counties_dict in voting_data:
    print(counties_dict)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county,voters in counties_dict.items():
    print(county + " county has" + str( voters) + " registered voters")
for county,voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")






                       











