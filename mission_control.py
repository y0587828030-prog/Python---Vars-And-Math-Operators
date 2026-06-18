#stap 2
agent_name = "yehoshua"
task_code = 127
distance = 376.5
mission_status = True
#stap 3
print (agent_name, task_code, distance, mission_status)
#stap 4
print(type(agent_name))
print(type(task_code))
print(type(distance))
print(type(mission_status))
#stap 5
travel_distance = distance * 2
print (travel_distance)
#stap 6
fuel = 1
fuel_usage = 1 # liter/km
fuel_needed = fuel_usage * travel_distance

print(f"fuel needed for the trip {fuel_needed}")
#stap 7
total_fuel = 1000
print(total_fuel)
remaining_fuel = total_fuel - fuel_needed
print (f"remaining_fuel: {remaining_fuel}")
#stap 8
countdown_conversion =input("How long until your mission starts in seconds? ")
countdown_conversion = int(countdown_conversion)
countdown_in_minuts = countdown_conversion / 60
countdown_in_hours = countdown_in_minuts / 60
print(f"your mission start at {countdown_in_hours} hours. in minut at {countdown_in_minuts} .at seconds {countdown_conversion} ")
 
#stap 9
distance_formatting =input("How much distance in a kilometer? ")
distance_formatting =int(distance_formatting)
distance_at_mails = distance_formatting * 0.6
print(distance_at_mails)