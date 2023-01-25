from src.controlTower.domain.account import account
from src.controlTower.domain.design import design
from src.controlTower import config
from invoke import run, Failure

class architect:

    def __init__(self, accoun: account, design: design):
        self.account = account
        self.design  = design

    def execute(self):
        if(self.design.status != config.SUCCESS):
            try:
                process = run(f'export AWS_PROFILE={self.account.name} && make {self.design.current.name}', asynchronous=True, pty=True)
            except Failure:
                self.design.setStatus(config.ERROR, process.result)
                print(process.result)
            else:
                self.design.setStatus(config.SUCCESS)
            finally:
                print(process)
        else:
            print("Nothing to do")
            return False

