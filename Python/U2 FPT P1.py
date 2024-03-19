#This program creates a table based on the user's input of different cities and the amount of households within that city
#The code will then output the amount of pet owning households based on the information given

#Ask for the user's input on different cities and households 

cityName0 = str(input("Please enter the first city:"))
houseHold0 = int(input("Please enter the total households in %s:" % (cityName0)))
cityName1 = str(input("Please enter the second city:"))
houseHold1 = int(input("Please enter the total households in %s:" % (cityName1)))
cityName2 = str(input("Please enter the third city:"))
houseHold2 = int(input("Please enter the total households in %s:" % (cityName2)))

#Calculate the amount of households with at least one pet in a given city, based on the statistics this number is 42%

petHouse0 = float(houseHold0 * 0.42)
petHouse1 = float(houseHold1 * 0.42)
petHouse2 = float(houseHold2 * 0.42)

#Display the table with the information calculated and provided 

print("City \t \t Total Households \t Pet-Owning Households")
print("%s \t \t %8i \t %21.1f" % (cityName0, houseHold0, petHouse0))
print("%s \t \t %8i \t %21.1f" % (cityName1, houseHold1, petHouse1))
print("%s \t \t %8i \t %21.1f" % (cityName2, houseHold2, petHouse2))
