from serum import dependency

@dependency
class Switchable:
    def turn_on(self):
        raise NotImplementedError()
    
    def turn_off(self):
        raise NotImplementedError()