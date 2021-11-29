def get_fuel_value(number):
	try:
		value = already_computed[number]
	except KeyError:
		value = (int(number/3)) - 2
		already_computed[number] = value

	return value
	print("Something has gone wrong...") 

file = open("C:\\Users\\Five\\Desktop\\Day1.txt")
already_computed = {}

current = file.readline().strip()
fuel = 0

while(current != ''):
	try:
		number = int(current)
		current_fuel = get_fuel_value(number)
		fuel += current_fuel

		while(not(current_fuel <= 0)):
			print(current_fuel)
			current_fuel = get_fuel_value(current_fuel)
			if current_fuel >= 0:
				fuel += current_fuel

		current = file.readline().strip()

	except ValueError:
		print("Something went wrong...")
		print("Error line: " + str(current))

file.close()
print("The total fuel cost is: " + str(fuel))