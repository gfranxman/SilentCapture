import aifc  
# aifc will be removed from standard python in 3.13.  
# See https://peps.python.org/pep-0594/#aifc for details.
from pprint import pprint
import os

import subprocess

subprocess.run( ["cp", "/System/Library//Components/CoreAudio.component/Contents/SharedSupport/SystemSounds/system/Grab.aifi", "."])
params = None

with  aifc.open("Grab.aif_original", "rb") as orig:
    print(str(orig))
    pprint(dir(orig))
    f=orig.readframes( 1)
    params = orig.getparams()
    print(f"{params=}")


with  aifc.open("empty.aif", "wb") as empty:
	empty.setparams(params)

subprocess.run(["cp", "empty.aif", "/System/Library//Components/CoreAudio.component/Contents/SharedSupport/SystemSounds/system/Grab.aif"])
