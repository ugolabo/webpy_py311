import sys

path = 'home/ugoproto/webpy_project/'
if path not in sys.path:
    sys.path.append(path)

from bin.app import app
application = app.wsgifunc()
