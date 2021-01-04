import sys, logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"C:/Apache24/htdocs/proyecto/")

from ejecutar import app as application
application.secret_key = '234lfkj345;lg46;[78]'

