import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random

# --- Network Simulator Class ---
class NetworkSimulator:
    def __init__(self):
        self.graph = nx.Graph()

    def create_topology(self, topology_type, num_nodes):
        self.graph.clear()
        if topology_type == 'bus':
            self.graph = nx.path_graph(num_nodes)
        elif topology_type == 'ring':
            self.graph = nx.cycle_graph(num_nodes)
        elif topology_type == 'star':
            self.graph = nx.star_graph(num_nodes - 1)
        elif topology_type == 'mesh':
            self.graph = nx.complete_graph(num_nodes)

        for (u, v) in self.graph.edges():
            self.graph[u][v]['weight'] = random.randint(1, 10)

    def hot_potato_routing(self, source, target):
        path = [source]
        current = source
        while current != target:
            neighbors = list(self.graph.neighbors(current))
            if target in neighbors:
                current = target
            else:
                current = random.choice(neighbors)
            path.append(current)
        return path

    def flooding(self, source, target):
        visited = set()
        queue = [(source, [source])]
        while queue:
            (node, path) = queue.pop(0)
            if node not in visited:
                visited.add(node)
                if node == target:
                    return path
                for neighbor in self.graph.neighbors(node):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        return None

    def source_routing(self, source, target):
        return nx.shortest_path(self.graph, source, target, weight='weight')

    def distance_vector_routing(self, source, target):
        return nx.shortest_path(self.graph, source, target, weight='weight')

    def link_state_routing(self, source, target):
        return nx.shortest_path(self.graph, source, target, weight='weight')

    def simulate_routing(self, algorithm, source, target):
        if algorithm == 'hot-potato':
            return self.hot_potato_routing(source, target)
        elif algorithm == 'flooding':
            return self.flooding(source, target)
        elif algorithm == 'source':
            return self.source_routing(source, target)
        elif algorithm in ['distance-vector', 'rip', 'link-state']:
            return self.distance_vector_routing(source, target)
        else:
            raise ValueError("Unknown routing algorithm")

    def draw_path(self, path):
        pos = nx.spring_layout(self.graph)
        plt.figure(figsize=(8, 6))
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=600)
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        if path:
            nx.draw_networkx_edges(self.graph, pos, edgelist=list(zip(path[:-1], path[1:])), edge_color='red', width=2)
            nx.draw_networkx_nodes(self.graph, pos, nodelist=path, node_color='orange', node_size=700)
        st.pyplot(plt)

# --- Streamlit UI ---
st.title("Network Routing Simulator")

topology = st.selectbox("Select Topology", ['bus', 'ring', 'star', 'mesh'])
num_nodes = st.slider("Number of Nodes", min_value=3, max_value=10, value=5)
source = st.number_input("Source Node", min_value=0, max_value=num_nodes - 1, value=0)
target = st.number_input("Target Node", min_value=0, max_value=num_nodes - 1, value=1)
algorithm = st.selectbox("Routing Algorithm", ['hot-potato', 'flooding', 'source', 'distance-vector', 'rip', 'link-state'])

if st.button("Simulate Routing"):
    simulator = NetworkSimulator()
    simulator.create_topology(topology, num_nodes)

    if source == target:
        st.warning("Source and target cannot be the same.")
    else:
        try:
            path = simulator.simulate_routing(algorithm, source, target)
            if path:
                st.success(f"Path from {source} to {target} using {algorithm} routing: {path}")
                simulator.draw_path(path)
            else:
                st.error("No path found.")
        except Exception as e:
            st.error(f"Error: {e}")
