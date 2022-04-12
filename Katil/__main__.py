# Powered By: © heartbrokenperson1
# Copyright (C) 2022 @KatilXUpdates

import glob
from pathlib import Path
from Katil.utils.util import load_plugins
import logging
from Katil import Saurabh

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "Katil/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("Successfully Started Your Bot!")

if __name__ == "__main__":
    Saurabh.run_until_disconnected()
