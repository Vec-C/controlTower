from controlTower.domain.model import Account, Design
from controlTower import config
from invoke import run, Failure, UnexpectedExit


class Architect:

    def __init__(self, account: Account, design: Design):
        self.account = account
        self.design  = design

    def execute(self):
        if(self.design.status != config.SUCCESS):
            try:
                process = run(f'export AWS_PROFILE={self.account.name} && make {self.design.current.name}', asynchronous=True)
            except Failure:
                self.design.setCurrentStatus(config.ERROR, str(Failure))
                print(str(Failure))
            else:
                self.design.setCurrentStatus(config.SUCCESS)

            # TODO: CATCH AND PRETTY PRINT STDOUT WHEN COMMAND FAILS
            # https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result
            # try:
            #     wait = process.join()
            #     self.design.setCurrentStatus(config.SUCCESS)
            # except UnexpectedExit:
            #     print("Error")
            #     self.design.setCurrentStatus(config.ERROR)

        else:
            print("Nothing to do")
        return self

