from process import *
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

