# %%
from collections import defaultdict
from statistics import mean

from matplotlib import pyplot as plt


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
                'host': '',
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
