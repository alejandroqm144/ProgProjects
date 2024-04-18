

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

estados = ["Yucatán", "Campeche", "Quintana Roo", "Tabasco", "Veracruz", "Oaxaca", "Chiapas"]
for estado in estados:
    G.add_node(estado)

G.add_edge("Yucatán", "Campeche", weight=250)
G.add_edge("Yucatán", "Quintana Roo", weight=200)
G.add_edge("Campeche", "Quintana Roo", weight=150)
G.add_edge("Campeche", "Tabasco", weight=300)
G.add_edge("Quintana Roo", "Tabasco", weight=400)
G.add_edge("Tabasco", "Veracruz", weight=350)
G.add_edge("Veracruz", "Oaxaca", weight=200)
G.add_edge("Oaxaca", "Chiapas", weight=250)
G.add_edge("Veracruz", "Chiapas", weight=400)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Grafo de Estados de México")
plt.show()

print("\nRelaciones entre estados:")
for edge in G.edges(data=True):
    estado1, estado2, peso = edge
    print(f"{estado1} - {estado2}: Costo de traslado ${peso['weight']}")