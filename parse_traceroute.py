# %%
from matplotlib import pyplot as plt


# %%
def is_timestamp(line):
    return line.startswith('2023-03')


def is_usg(line):
    return '192.168.1.1' in line

# Cable modem termination system (CMTS) is equipment located
# at a cable company's headend. Used to provide high speed data
# services like cable Internet to cable subscribers.
def is_cmts(line):
    return ' 2  10.' in line


def is_rcn(line):
    return 'rcn.net' in line


def is_cloudflare(line):
    return 'one.one.one.one (1.1.1.1)' in line


def is_google(line):
    return '1e100.net' in line


# %%
log_file = 'cloudflare.txt'
# log_file = 'google.txt'

# is_target_hop = is_usg
# is_target_hop = is_cmts
# is_target_hop = is_rcn
is_target_hop = is_cloudflare
# is_target_hop = is_google

xs = []
ys = []

with open(log_file) as f:
    probes = []

    for line in f:
        if is_timestamp(line):
            if len(probes):
                # record average latency observed for previous timestamp
                avg_latency = sum(probes) / len(probes)
                ys.append(avg_latency)

            probes = []

            # record this new timestamp
            xs.append(line.strip())
        elif is_target_hop(line):
            parts = line.split()

            for ix, part in enumerate(parts):
                if part == 'ms':
                    # collect probes for current timestamp
                    probes.append(float(parts[ix - 1]))
    
    if len(probes):
        # record average latency observed for final timestamp
        avg_latency = sum(probes) / len(probes)
        ys.append(avg_latency)

width = len(xs) / 3
plt.figure(figsize=(width, 4.8))

plt.plot(xs, ys)

plt.xticks(rotation=-90)
plt.xlim(-1, len(xs))
plt.ylim(0, 175)
plt.grid()

# double-click to zoom
plt.show()

# %% [markdown]
# # Notes
#
# Based on the traceroute output parsed above, consistently low average latency (and packet loss) to USG (external gateway) and CMTS. However, examples of intermittent high average latency (and packet loss) to:
#
# - RCN
#   - `2023-03-04T22:20:53-05:00` to `2023-03-04T22:25:18-05:00` (enroute to Cloudflare)
#   - `2023-03-04T22:45:33-05:00` to `2023-03-04T22:51:43-05:00` (enroute to Cloudflare) <- good example
#   - `2023-03-04T21:51:39-05:00` to `2023-03-04T21:56:05-05:00` (enroute to Google)
#   - `2023-03-04T22:45:12-05:00` to `2023-03-04T22:52:51-05:00` (enroute to Google)
#   - ...
# - Cloudflare
#   - `2023-03-04T21:51:55-05:00` to `2023-03-04T21:54:58-05:00`
#   - `2023-03-04T22:45:33-05:00` to `2023-03-04T22:51:43-05:00` <- good example
#   - ...
# - Google
#   - `2023-03-04T21:48:48-05:00` to `2023-03-04T21:57:30-05:00`
#   - `2023-03-04T22:45:12-05:00` to `2023-03-04T22:51:22-05:00` <- good example
#   - ...
#

# %%
