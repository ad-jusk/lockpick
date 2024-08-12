import logging

def _configure_logger() -> logging.Logger:

    handler: logging.Handler = logging.StreamHandler()
    format: logging.Formatter = logging.Formatter(f'[ %(levelname)s ] [ %(asctime)s ] %(msg)s')
    handler.setFormatter(format)

    logger: logging.Logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger

class LOGGER:

    _LOGGER: logging.Logger = _configure_logger()
    _DEBUG: bool = True

    @classmethod
    def info(cls, message: str) -> None:
        if cls._DEBUG:
            cls._LOGGER.info(message)
    
    @classmethod
    def warn(cls, message: str) -> None:
        if cls._DEBUG:
            cls._LOGGER.warning(message)

    @classmethod
    def error(cls, message: str) -> None:
        if cls._DEBUG:
            cls._LOGGER.error(message)
        


