from scheduler import *


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
