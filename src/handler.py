from mangum import Mangum
from src.modules.api import app

handler = Mangum(app)
