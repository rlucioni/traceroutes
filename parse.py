# %%
from collections import defaultdict
from statistics import mean

from matplotlib import pyplot as plt
import networkx as nx


# %%
def strip_parens(val):
    return val.replace('(', '').replace(')', '')


# %%
traceroutes = defaultdict(list)

# %%
log_file = 'data/cloudflare.txt'
# log_file = 'data/google.txt'

timestamp = None

with open(log_file) as f:
    for line in f:
        parts = line.split()

        if parts[0].startswith('2023-'):
            timestamp = parts[0]
        elif parts[1] == '*':
            traceroutes[timestamp].append({
                # TODO: set the host to <hop number>-*?
                'host': '*',
                'ip': '',
                'rtt': None,
            })
        elif parts[3] == '*':
            traceroutes[timestamp].append({
                'host': parts[1],
                'ip': strip_parens(parts[2]),
                'rtt': None,
            })
        else:
            traceroutes[timestamp].append({
                'host': parts[1],
                'ip': strip_parens(parts[2]),
                'rtt': float(parts[3]),
            })

# %%
xs = traceroutes.keys()
ys = []

for traceroute in traceroutes.values():
    # USG (external gateway)
    # ys.append(traceroute[0]['rtt'])
    
    # # CMTS?
    # ys.append(traceroute[1]['rtt'])

    # RCN
    # ys.append(mean([t['rtt'] for t in traceroute if 'rcn.net' in t['host']]))

    # destination host
    ys.append(traceroute[-1]['rtt'])

# %%
width = len(xs) / 3
fig = plt.figure(figsize=(width, 4.8))
fig.subplots_adjust(bottom=0.5)

plt.plot(xs, ys)

plt.ylabel('ms')
plt.xticks(rotation=-90)
plt.xlim(-1, len(xs))
plt.ylim(0, 175)
plt.grid()

plt.show()

# %%
G = nx.MultiDiGraph()

for traceroute in traceroutes.values():
    for ix, hop in enumerate(traceroute):
        if ix + 1 < len(traceroute):
            this_host = hop['host']
            next_host = traceroute[ix + 1]['host']

            G.add_edge(this_host, next_host)

# %%
fig = plt.figure(figsize=(10, 10))

pos = nx.nx_agraph.pygraphviz_layout(G, prog='dot')

nx.draw_networkx_nodes(G, pos, node_size=100)
nx.draw_networkx_edges(G, pos, node_size=100, alpha=0.2)
nx.draw_networkx_labels(G, pos, font_size=6)

# expand margins to keep labels in frame
x_values, y_values = zip(*pos.values())
x_max = max(x_values)
x_min = min(x_values)
x_margin = (x_max - x_min) * 0.25
plt.xlim(x_min - x_margin, x_max + x_margin)

plt.box(False)
plt.show()

# %%
