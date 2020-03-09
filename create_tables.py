from models import *
from config import *

DB.connect()

DB.drop_tables([Book])
DB.create_tables([Book])

DB.close()
