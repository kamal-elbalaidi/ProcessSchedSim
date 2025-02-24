# ProcessSchedSim

## Description
A Python-based simulator for process scheduling algorithms (FIFO, SJF, Round Robin) with Gantt chart visualization.

![Process Scheduling Example](https://media.licdn.com/dms/image/v2/D4E22AQGm4o6q_z8TWg/feedshare-shrink_800/B4EZU1g0CVH0Ag-/0/1740359551155?e=1743033600&v=beta&t=iAgVP-bJh7WmsB07Y8vvxC2SPjNqDFoqbbBhSL8s7Ew)  
*An example of a Gantt chart generated by the simulator.*

---

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- Simulates three scheduling algorithms: **FIFO**, **SJF**, and **Round Robin**.
- Customizable process attributes (ID, arrival time, burst time, priority).
- Visualizes execution schedules using **Gantt charts**.
- Evaluates performance based on metrics like waiting time, turnaround time, and fairness.

---

## Requirements
- Python 3.6 or higher
- Required libraries:
  - `matplotlib`
  - `dataclasses`
  - `typing`

You can install the required libraries using pip:
```bash
pip install matplotlib
```

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kamal-elbalaidi/ProcessSchedSim.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ProcessSchedSim
   ```
3. Install the dependencies:
   ```bash
   pip install matplotlib
   ```

---

## Usage
1. Run the main script:
   ```bash
   python main.py
   ```
2. Enter the number of processes and their attributes (arrival time, burst time, priority).
3. Choose the scheduling algorithm you want to simulate (FIFO, SJF, Round Robin).
4. View the results in the form of a Gantt chart.

---

## Examples
### Input Example:
- Number of processes: 3
- Process details:
  - P1: Arrival = 0, Burst = 8
  - P2: Arrival = 1, Burst = 4
  - P3: Arrival = 2, Burst = 9

### Output Example:
A Gantt chart showing the execution schedule of the selected algorithm.

---

## Contributing
 Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
