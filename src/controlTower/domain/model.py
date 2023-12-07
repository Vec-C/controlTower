from   controlTower import config
from   controlTower.utils.io import IO
from   invoke import run, Failure
import re

class Account:

    def __init__(self, access_id: str, access_secret: str, name: str, region: str):
        self.access_id     = access_id
        self.access_secret = access_secret
        self.name          = name
        self.region        = region

    def __eq__(self, other):
        if isinstance(other, Account):
            if(self.access_id == other.access_id and self.access_secret == other.access_secret and self.name == other.name and self.region == other.region):
                return True
            else:
                return False
        else:
            return False

    def configure(self):
        '''Executes "aws configure" command which sets access info in ~/.aws/credentials & ~/.aws/config files'''
        try:
            set = run(f'aws --profile {self.name} configure set aws_access_key_id "{self.access_id}"', pty=True)
            set = run(f'aws --profile {self.name} configure set aws_secret_access_key "{self.access_secret}"', pty=True)
            set = run(f'aws --profile {self.name} configure set region "{self.region}"', pty=True)
        except Failure:
            print(set.result)
            return False
        else:
            return self

class Receipt:

    def __init__(self, command: str, dependencies: list, files: str, id: int, name: str):
        self.command        = command
        self.creation_date  = config.NOW_UTC
        self.dependencies   = dependencies
        self.error          = None
        self.execution_date = None
        self.files          = files
        self.id             = id
        self.name           = name
        self.status         = config.INIT

#TODO: ADD GIT HASH SEQUENCE MANAGMENT
class Design:

    def __init__(self, name: str, version: str, path: str):
        self.creation_date = config.NOW_UTC
        self.current       = None
        self.data          = IO().read_data(path)
        self.name          = name
        self.path          = path
        self.progress      = 0
        self.status        = config.INIT
        self.steps         = []
        self.version       = version
        self.set_steps()

    def set_steps(self):
        '''
        Reads Makefile(self.data) and creates a list with each receipt
        regex[x][0]: step name
        regex[x][1]: dependencies
        regex[x][3]: files involved
        :return: list()
        '''
        regex        = re.findall(config.REGEX_STEPS, self.data)
        for step in range(0, len(regex)):
            files = re.findall(config.REGEX_IN_FILES, regex[step][3])
            if len(files) > 0:
                files = files[0]
            else:
                files = None
            self.addStep(regex[step][3], regex[step][1], files, step, regex[step][0])
        self.setCurrent(self.steps[0])

    def setCurrent(self, receipt):
        '''Adds "Current" modifications to the steps registry and sets next step as "Current"'''
        if self.current is not None:
            self.steps[self.current.id] = self.current
        self.current = receipt

    def setCurrentStatus(self, status, msg=""):
        '''Sets current step status and if it is Success sets the next step as Current
           If there are no more steps it sets the entire Design status from processing to success'''
        self.current.execution_date = config.NOW_UTC
        self.current.status         = status
        self.status                 = config.PROCESSING
        if status == config.ERROR:
            self.current.error      = msg
        else:
            next = self.current.id + 1
            if next > len(self.steps) - 1:
                self.progress = 100
                self.status   = config.SUCCESS
            else:
                self.progress = (next*100)/len(self.steps)
                self.setCurrent(self.steps[next])

    def addStep(self, command, dependencies, files, id, name):
        newStep = Receipt(command, dependencies, files, id, name)
        self.steps.append(newStep)

class Job:
    def __init__(self, account: Account, design: Design):
        self.account   = account
        self.design    = design