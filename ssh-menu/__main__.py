from .config import init_config
from .config import get_servers_config
from .config import get_default_servers_config_path
from . import widget
from argparse import ArgumentParser

parser = ArgumentParser()

args = parser.parse_args()

init_config()

path = get_default_servers_config_path()
config = get_servers_config(path)

for s in config.servers:
    print("got server: %s" % s.name)

#widget.start()
