import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List


@dataclass
class Process:
    id: int
    arrival: int
    burst: int
    priority: int
    remaining: int = 0

    def __post_init__(self):
        self.remaining = self.burst


class Scheduler:
    def __init__(self, processes: List[Process]):
        self.processes = processes
        self.current_time = 0

    def fifo(self):
        # Sort first by arrival time, then by priority
        sorted_processes = sorted(self.processes, 
                                key=lambda p: (p.arrival, p.priority))
        self.current_time = 0
        schedule = []
        for p in sorted_processes:
            if self.current_time < p.arrival:
                self.current_time = p.arrival
                # Check if there are higher priority processes that arrived while waiting
                available = [proc for proc in sorted_processes 
                            if proc.arrival <= self.current_time and 
                            proc.priority < p.priority]
                if available:
                    p = min(available, key=lambda x: x.priority)
            schedule.append((p.id, self.current_time, 
                            self.current_time + p.burst))
            self.current_time += p.burst
        return schedule

    def sjf(self):
        remaining = self.processes.copy()
        self.current_time = 0
        schedule = []
        while remaining:
            available = [p for p in remaining if p.arrival <= self.current_time]
            if not available:
                self.current_time = min(p.arrival for p in remaining)
                continue
            # Consider both burst time and priority
            next_process = min(available, 
                             key=lambda p: (p.burst * 0.7 + p.priority * 0.3))
            schedule.append((next_process.id, self.current_time, 
                            self.current_time + next_process.burst))
            self.current_time += next_process.burst
            remaining.remove(next_process)
        return schedule

    def round_robin(self, quantum: int):
        # Sort processes by priority (lower number = higher priority)
        remaining = sorted(self.processes.copy(), key=lambda p: p.priority)
        self.current_time = 0
        schedule = []

        while remaining:
            # Get processes that have arrived and sort by priority
            available = [p for p in remaining if p.arrival <= self.current_time]
            if not available:
                self.current_time = min(p.arrival for p in remaining)
                continue

            # Get highest priority process
            current = min(available, key=lambda p: p.priority)
            remaining.remove(current)

            exec_time = min(quantum, current.remaining)
            schedule.append((current.id, self.current_time,
                            self.current_time + exec_time))

            current.remaining -= exec_time
            self.current_time += exec_time

            if current.remaining > 0:
                # Add back to queue, maintaining priority order
                index = 0
                for i, p in enumerate(remaining):
                    if p.priority > current.priority:
                        index = i
                        break
                remaining.insert(index, current)

        return schedule


def plot_gantt(schedule, processes, title):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_title(title)

    for pid, start, end in schedule:
        ax.barh(y=pid, width=end-start, left=start,
                color=f'C{pid % 10}', alpha=0.5)
        ax.text((start+end)/2, pid, f'P{pid}',
                ha='center', va='center')

    ax.set_xlabel('Time')
    ax.set_ylabel('Process ID')
    ax.grid(True)

    details = []
    for p in processes:
        details.append(f'P{p.id}: Arrival={p.arrival}, Burst={p.burst}, '
                       f'Priority={p.priority}')
    fig.text(0.05, -0.1, '\n'.join(details), ha='left', va='center')

    plt.tight_layout()
    plt.show()


def main():
    # Get number of processes
    n = int(input("Number Of Processes: "))
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
    print("2. Plus court d'abord")
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
