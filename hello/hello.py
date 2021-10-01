from serum import dependency

@dependency
class Hello:
    def messages(self, msg:str):
        raise NotImplementedError()