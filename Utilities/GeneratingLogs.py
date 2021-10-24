import logging
def log():
    logging.basicConfig(filename="..\\logsfolder\\logfile.log",
                        format='%(asctime)s:%(levelname)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filemode='w',level=logging.INFO)
    logger=logging.getLogger()
    return logger


