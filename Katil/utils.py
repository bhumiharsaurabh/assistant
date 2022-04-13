# Powered By: © heartbrokenperson1
# Copyright (C) 2022 @KatilXUpdates

import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"Katil/plugins/{plugin_name}.py")
    name = "Katil.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Katil.plugins." + plugin_name] = load
    print("Bot has Started Successfully " + plugin_name)
