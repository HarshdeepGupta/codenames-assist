from flask import Flask

class Logger():
    def __init__(self, app: Flask) -> None:
       self.app = app
    

    def log(self, message):
        self.app.logger.info(msg = message)