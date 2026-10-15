import logging

format = "%(asctime)s %(levelname)s %(message)s"


def get_logger(name, level = logging.INFO):

    """
    Return a logger that prints one line per message

    name: where the message comes from
    level: the lowest level we want to see (default will be INFO)
    """

    logger = logging.getLogger(name)    # creates a logger with the name ds2b_cosmosdb
    logger.setLevel(level)              # Sets the minimum severity level for this logger to INFO

    if not logger.handlers:             # Checks whether this logger already has a handler attached 
                                        # handler decides where log messages go, such as: console,terminal,file
                                        # Without this check, one log message could appear multiple times:
        handler = logging.StreamHandler() # Creates a stream handler. This handler will print to the console
        handler.setFormatter(logging.Formatter(format)) # Sets the format for the handler
        logger.addHandler(handler)        # Adds the handler to the logger
    
    return logger