# Import the random variable which we will use for this simulation
import random
import math

# Create a Computer class which we will use to create Computer objects with an infected attribute
# This attribute will let us know whether a Computer is infected or not
class Computer:
    def __init__(self):
        self.infected = False

days = []
nsim = 1000

for i in range(nsim):
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
    not_infected.remove(virus_computer)

    # This happens on day 0
    day = 0

    # Continue while infected computers exists in the system
    while infected:
        # Increment the day by 1 each time and have a set of the newly infected computers
        day += 1
        curr_infected = set()

        # For each infected computer, infect each clean computer with a probability of 0.1
        for infected_comp in infected:
            for clean_comp in not_infected:
                prob = random.random()
                if prob <= 0.1:
                    clean_comp.infected = True
                    curr_infected.add(clean_comp)
        for comp in curr_infected:
            infected.append(comp)
            not_infected.remove(comp)
        # Choose all the infected computers if they are less than 5 or choose 5 randomly infected computers
        if len(infected) <= 5:
            tech_choice = infected.copy()
        else:
            tech_choice = random.sample(infected, 5)

        # Remove the cleaned computers from the infected ones
        infected = [computer for computer in infected if computer not in tech_choice]
        not_infected.extend(tech_choice)
    days.append(day)

print(f"Solution after {nsim} simulations: ")
print(f'Expected number of days to clean the system: {sum(days) / len(days)}')