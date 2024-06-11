List Scheduling of Identical Machines

Description:
This Python program performs list scheduling of identical machines based on user input. It schedules jobs on a set of machines in a way that minimizes the makespan, which is the total time required to complete all jobs.

Features:
- Allows the user to input the number of jobs to schedule and their processing times.
- User can specify the number of machines available.
- Implements list scheduling algorithm to assign jobs to machines.
- Calculates and displays the schedule, load times for each machine, and the makespan.

Usage:
1. Run the program.
2. Enter the number of jobs to schedule.
3. Input the processing time for each job.
4. Enter the number of machines available.
5. The program will output the schedule, load times for each machine, and the makespan.

Example:
```
List scheduling of identical machines

No. of Jobs to schedule: 4
Input processing time of Job 1: 3
Input processing time of Job 2: 5
Input processing time of Job 3: 2
Input processing time of Job 4: 4
No. of Machines: 2

Job List: [5, 4, 3, 2]
Schedule:  [[5, 3], [4, 2]]
Load times:  [8, 6]
Makespan:  8
```

Notes:
- Jobs are scheduled in descending order of processing time to minimize makespan.
- The program assumes identical machines with no setup times between jobs.
- This is a basic implementation and may not be suitable for complex scheduling problems.

Author:
- Name: Llobrera, John Aaron B.
- Affiliation: BS Statistics, Institute of Statistics, University of the Philippines Los Baños
- Email: jbllobrera@up.edu.ph

Feel free to reach out for any questions or suggestions!