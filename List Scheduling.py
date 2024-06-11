# Author: Llobrera, John Aaron B.
    # Affiliation: BS Statistics, Institute of Statistics, University of the Philippines Los Baños
    # E-Mail: jbllobrera@up.edu.ph

# Code Description:
    # This program performs list scheduling of identical machines based on user input.

# Print Header
print("List scheduling of identical machines")

# User input for the No. of Jobs to Schedule
Jobs = int(input("\nNo. of Jobs to schedule: "))

# Joblist
joblist = []

for j in range(0, Jobs):
    ProcessingTime = int(input('Input processing time of Job ' + str(j + 1) + ': '))
    joblist.append(ProcessingTime)

# Input for the number of machines
Machines = int(input("No. of Machines: "))

# Output for the joblist
print("Job List:", joblist)
joblist.sort(reverse=True)  # Sort in reverse order

# Initialize the machines
machines = [[] for _ in range(Machines)]

# Function to find the next available machine
def machineavailability(machines):
    # Find the machine with the minimum load time using the min function
    min_load_time = min(sum(machine) for machine in machines)
    for machine in machines:
        if sum(machine) == min_load_time:
            return machine

# Schedule the jobs
for job in joblist:
    # Find the next available machine
    machine = machineavailability(machines)
    # Schedule the job on the found machine
    machine.append(job)

# Calculate load times and makespan
load_times = [sum(machine) for machine in machines]
makespan = max(load_times)

# Output the schedule, load times, and makespan
print("Schedule: ", machines)
print("Load times: ", load_times)
print("Makespan: ", makespan)
