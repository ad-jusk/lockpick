from logger import LOGGER

class Model:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Model, cls).__new__(cls)
        return cls.instance
    
    def test(self):
        LOGGER.info('Hello from model!')