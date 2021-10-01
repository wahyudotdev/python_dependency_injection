from serum import inject
from di import context
from electronic.switchable import Switchable

@inject
class App:
    lamp:Switchable

    def turn_on(self):
        self.lamp.turn_on()
    
    def turn_off(self):
        self.lamp.turn_off()

@context
def start_app():
    app = App()
    app.turn_on()
    app.turn_off()

if __name__ == '__main__':
    start_app()