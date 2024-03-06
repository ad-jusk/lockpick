from logger import LOGGER
from model.model import Model

class Controller:

    def __init__(self):
        self.model = Model()
    
    def test(self):
        LOGGER.info('Hello from controller!')
        self.model.test()
        