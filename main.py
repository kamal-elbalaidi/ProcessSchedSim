from gantt import *


def main():
    # Get number of processes
    n = int(input("Number of processes: "))
    processes = []

    # Get process details
    print("\nEnter processes: ")
    for i in range(n):
        print(f"\nProcess {i+1}:")
        arrival = int(input("Date: "))
        burst = int(input("Duree: "))
        priority = int(input("Priority: "))
        processes.append(Process(i+1, arrival, burst, priority))

    # Get scheduling algorithm
    print("\n Algorithem")
    print("1. FIFO")
    print("2. SJF")
    print("3. Round Robin")
    choice = int(input("Chose (1-3): "))

    scheduler = Scheduler(processes)

    if choice == 1:
        schedule = scheduler.fifo()
        # Scheduling
        plot_gantt(schedule, processes, 'FIFO')
    elif choice == 2:
        schedule = scheduler.sjf()
        plot_gantt(schedule, processes, "Plus court d'abord")
    elif choice == 3:
        quantum = int(input("Quantum: "))
        schedule = scheduler.round_robin(quantum)
        plot_gantt(schedule, processes, f'Quantum (Q={quantum})')


if __name__ == "__main__":
    main()
