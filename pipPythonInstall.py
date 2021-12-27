import sys
import os


pipdir=os.path.dirname(sys.executable)+"\\Scripts"
INSTALLSIGNAL=0
if INSTALLSIGNAL:
	os.system(rf'setx PATH "%PATH%;{pipdir}"')