# %%
from collections import defaultdict
from statistics import mean

from matplotlib import pyplot as plt
import networkx as nx


# %%
def strip_parens(val):
    return val.replace('(', '').replace(')', '')


# %%
# log_file = 'data/cloudflare.txt'
log_file = 'data/google.txt'

traceroutes = defaultdict(list)
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
traceroutes['2023-03-06T17:45:18-05:00']

# %%
# https://networkx.org/documentation/stable/reference/classes/multidigraph.html
G = nx.MultiDiGraph()

for traceroute in traceroutes.values():
    for ix, hop in enumerate(traceroute):
        if ix + 1 < len(traceroute):
            this_host = hop['host']
            next_host = traceroute[ix + 1]['host']

            G.add_edge(this_host, next_host)

# %%
# https://networkx.org/documentation/latest/auto_examples/drawing/plot_unix_email.html
# https://networkx.org/documentation/latest/auto_examples/graphviz_layout/plot_lanl_routes.html

# https://graphviz.org/docs/layouts/dot/
pos = nx.nx_agraph.pygraphviz_layout(G, prog='dot')

nx.draw_networkx_nodes(G, pos, node_size=200)
nx.draw_networkx_edges(G, pos, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=8)

plt.box(False)
plt.show()

# %%
