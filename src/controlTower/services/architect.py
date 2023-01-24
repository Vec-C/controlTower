from src.controlTower.domain.account import account
from src.controlTower.domain.design import design
from invoke import run, Failure

class architect:

    def __init__(self, accoun: account, design: design):
        self.account = account
        self.design  = design

    def execute(self):
        if(self.design.status != "finished"):
            try:
                process = run(f'export AWS_PROFILE={self.account.name} && make {self.design.current.name}', asynchronous=True, pty=True)
            except Failure:
                self.design.setStatus("error", process.result)
                print(process.result)
            else:
                self.design.setStatus("success")
            finally:
                print(process)
        else:
            print("Nothing to do")
            return False

