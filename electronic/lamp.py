from .switchable import Switchable
from serum import dependency, inject

@dependency
class Messages:
    def construct(self, msg: str, state: str)-> str:
        return f'{msg} => {state}'

class Lamp(Switchable):

    @inject
    def __init__(self, messages:Messages) -> None:
        self.messages = messages

    def turn_on(self):
        msg = self.messages.construct(msg='lamp', state='ON')
        print(msg)

    def turn_off(self):
        msg = self.messages.construct(msg='lamp', state='OFF')
        print(msg)