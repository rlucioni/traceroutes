# traceroutes

Tools for parsing and interpreting lots of `traceroute` output. After activating a virtualenv, install requirements with:

```sh
make requirements
```

Run the `traceroute-loop.sh` script to log `traceroute` output to text files:

```sh
./traceroute-loop.sh
```

Use the `parse_traceroute.py` script to parse and work with the logged output. It's bound to a Jupyter notebook with [Jupytext](https://github.com/mwouts/jupytext). To open it, start Jupyter Notebook with:

```sh
make notebook
```
