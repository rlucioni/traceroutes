# traceroutes

Tools for generating and working with `traceroute` output. After activating a virtualenv, install requirements with:

```sh
make requirements
```

Installing `pygraphviz` requires following [special instructions](https://github.com/pygraphviz/pygraphviz/issues/398#issuecomment-1038476921). Run the `loop.sh` script to run traceroutes for the hosts in `hosts.txt` and log output to `data.txt`:

```sh
make loop
```

Use the `parse.py` script to manipulate the logged output. It's bound to a Jupyter notebook with [Jupytext](https://github.com/mwouts/jupytext). To open it, start Jupyter Notebook with:

```sh
make notebook
```
