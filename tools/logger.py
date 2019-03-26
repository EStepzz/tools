import logging

class Log:
    # def __init__(self,msg):
    #     self.msg = msg

    def debug(self):
        FORMAT = "%(asctime)-15s%(message)s"
        logging.basicConfig(filemode="w+", filename="file.log", format=FORMAT, level=logging.DEBUG)
        logging.debug(self.msg)