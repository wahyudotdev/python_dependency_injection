from serum import inject
from hello import hello
from hello.hello import Hello
from di import context

@inject
class App:
    hello:Hello

    def messages(self, msg):
        self.hello.messages(msg)

@context
def hello():
    app = App()
    app.messages('Tes Dependency Injection')

if __name__ == '__main__':
    hello()