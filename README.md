# Network-Routing-Simulator
It simulates a network simulation with all types of topologies and specific algortithms
```markdown
# Network Routing Simulator in Python (Google Colab)

This project is an interactive network routing simulator built using Python libraries: NetworkX, Matplotlib, and ipywidgets. It enables dynamic visualization of packet routing over various network topologies using different routing algorithms.

## Features

- Supports multiple network topologies:
  - Bus
  - Ring
  - Star
  - Mesh
- Implements several routing algorithms:
  - Hot Potato Routing
  - Flooding
  - Source Routing
  - Distance Vector Routing
  - Link-State Routing
- Animated visualization of packet movement
- Interactive controls using ipywidgets in Google Colab or Jupyter Notebooks

## Libraries Used

| Library           | Purpose                                           |
|------------------|---------------------------------------------------|
| `networkx`        | Graph creation, manipulation, and routing        |
| `matplotlib`      | Plotting and animations                          |
| `ipywidgets`      | Interactive widgets for user input               |
| `random`          | Random selection for hot-potato routing, weights |
| `IPython.display` | Displaying HTML animations in the notebook       |

## Getting Started

1. Open the notebook in Google Colab or a Jupyter Notebook environment.

2. Install dependencies if not already installed:

```python
!pip install networkx matplotlib ipywidgets
from google.colab import output
output.enable_custom_widget_manager()
```

3. Run the code to load the `NetworkSimulator` class and associated logic.

4. Use the provided interactive UI to:
   - Select the desired topology
   - Set the number of nodes
   - Choose a routing algorithm
   - Define the source and target nodes

## Routing Algorithms Overview

| Algorithm       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| Hot Potato      | Randomly forwards the packet to one of the neighbors until it reaches the target. |
| Flooding        | Broadcasts the packet to all unvisited neighbors until the destination is found. |
| Source Routing  | The source node computes the entire path using Dijkstra’s shortest path algorithm. |
| Distance Vector | Each node makes routing decisions based on distance metrics (weights). Simulated with NetworkX's shortest path. |
| Link-State      | Each node has a global view and calculates the shortest path using link-state information. Also simulated via shortest path. |

## Example Usage

Once all functions and classes are defined, use the following interactive widget to start the simulation:

```python
interact(run_simulation,
         topology=widgets.Dropdown(options=['bus', 'ring', 'star', 'mesh'], description='Topology:'),
         num_nodes=widgets.IntSlider(min=3, max=10, step=1, value=5, description='Nodes:'),
         algorithm=widgets.Dropdown(options=['hot-potato', 'flooding', 'source', 'distance-vector', 'rip', 'link-state'], description='Algorithm:'),
         source=widgets.IntText(value=0, description='Source:'),
         target=widgets.IntText(value=4, description='Target:'))
```

## Directory Structure

```
network-routing-simulator/
│
├── notebook.ipynb       # Main notebook with simulation code
├── README.md            # Project documentation
```

## Potential Improvements

- Add simulation of packet loss or network delays
- Implement advanced routing protocols like OSPF or BGP
- Export routing paths or performance metrics
- Enable manual graph editing with node placement

## Author

Shreyash Sule

## License

This project is licensed under the MIT License.
```
