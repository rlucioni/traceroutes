# traceroutes

Tools for generating and navigating lots of `traceroute` output. After activating a virtualenv, install requirements with:

```sh
make requirements
```

Run the `loop.sh` script to log `traceroute` output to text files under `data/`:

```sh
./loop.sh
```

Use the `parse.py` script to manipulate the logged output, to help hone in on interesting periods to look at in the logs. It's bound to a Jupyter notebook with [Jupytext](https://github.com/mwouts/jupytext). To open it, start Jupyter Notebook with:

```sh
make notebook
```
