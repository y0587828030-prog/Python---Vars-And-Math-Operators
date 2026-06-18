agent_name = "yehoshua"
task_code = 127
distance = 376.5
mission_status = True
print (agent_name, task_code, distance, mission_status)
print(type(agent_name))
print(type(task_code))
print(type(distance))
print(type(mission_status))
travel_distance = distance * 2
print (travel_distance)
fuel = 1
fuel_usage = 1 # liter/km
fuel_needed = fuel_usage * travel_distance

print(f"fuel needed for the trip {fuel_needed}")
total_fuel = 1000
print(total_fuel)
remaining_fuel = total_fuel - fuel_needed
print (remaining_fuel)
