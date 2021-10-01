from .hello import Hello
from serum import dependency, inject

@dependency
class ShowMessages:
    def show_msg(self, msg: str):
        print(msg)

class HelloImpl(Hello):
    @inject
    def __init__(self, show_messages:ShowMessages) -> None:
        self.show_messages = show_messages

    def messages(self, msg: str):
        self.show_messages.show_msg(msg)