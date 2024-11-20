# Import the random variable which we will use for this simulation
import random

# Create a Computer class which we will use to create Computer objects with an infected attribute
# This attribute will let us know whether a Computer is infected or not
class Computer:
    def __init__(self):
        self.infected = False

# Create two lists to store the non-infected and infected variables
not_infected = []
infected = []

# Create 20 Computer objects
for i in range(20):
    not_infected.append(Computer())

# Choose a random computer and infect it with the virus to start the simulation
virus_computer = random.choice(not_infected)
virus_computer.infected = True
infected.append(virus_computer)

# This happens on day 0
day = 0

# Continue while infected computers exists in the system
while infected:
    # Increment the day by 1 each time
    day += 1

    # For each infected computer, infect each clean computer with a probability of 0.1
    for infected_comp in infected:
        for clean_comp in not_infected:
            prob = random.random()
            if prob <= 0.1:
                clean_comp.infected = True
                not_infected.remove(clean_comp)
                infected.append(clean_comp)

    # Choose all the infected computers if they are less than 5 or choose 5 randomly infected computers
    if len(infected) <= 5:
        tech_choice = infected
    else:
        tech_choice = random.sample(infected, 5)

    # Remove the cleaned computers from the infected ones
    infected = [computer for computer in infected if computer not in tech_choice]
print(day)