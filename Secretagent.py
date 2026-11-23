name = input("Enter your real name Agent")
gadget = input("Enter your favorite gadget:")
agent_number = 7
speed_rating = 5.5
mission_count = 12
is_active = True
print("Name:", name,"--- type =",type(name))
print("agent_number:", agent_number,"--- type =",type(agent_number))
print("speed rating:", speed_rating,"--- type =",type(speed_rating))
print("is active:", is_active,"--- type =",type(is_active))
agent_number_text = str(agent_number)
speed_rating_text = str(speed_rating)
mission_count_text = str(mission_count)
status_text = str(is_active)
print("agent_number text:", agent_number_text,"--- type =",type(agent_number_text))
print("mission count text:", mission_count_text,"--- type =",type(mission_count_text))
print("speed rating text:", speed_rating_text,"--- type =",type(speed_rating_text))
print("status as text:", status_text,"--- type =",type(status_text))
first_three = name[0:3]
last_letter = name[-1:]
code = first_three + last_letter
print("first letter", first_three)
print("last letter",last_letter)
print("Secret code name",code)
reversed_gadget = gadget[::-1]
print("reversed gadget Name",reversed_gadget)
code_upper = code.upper()
print("code upper ", code_upper)