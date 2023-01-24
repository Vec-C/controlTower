from src.controlTower.utils.io import reader
import datetime
import os
import re

class receipt:

    def __init__(self, command: str, dependencies: list, files: str, name: str):
        self.command        = command
        self.creation_date  = datetime.date.today().isoformat()
        self.dependencies   = dependencies
        self.error          = None
        self.execution_date = None
        self.files          = files
        self.id             = 0
        self.name           = name
        self.status         = "init"

class design:

    def __init__(self, name: str, path: str):
        self.current       = None
        self.creation_date = datetime.date.today().isoformat()
        self.data          = reader.read_data(path)
        self.name          = name
        self.path          = path
        self.set_steps()
        self.status        = "init"
        self.steps         = []

    def set_steps(self):
        commands     = re.search('^[^\n|^#](.*?):(.*?)\n(\t(.*?))?$', self.data).group(3)
        dependencies = re.search('^[^\n|^#](.*?):(.*?)\n(\t(.*?))?$', self.data).group(2)
        steps        = re.search('^[^\n|^#](.*?):(.*?)\n(\t(.*?))?$', self.data).group(1)
        for step in range(0, steps.len() - 1):
            files = re.search('.*?\s([A-z0-9_-]+\.[A-z0-9]+).*?', commands[step]).group(1)
            self.addStep(self, commands[step], dependencies[step], files, step, steps[step])
        self.setCurrent(steps[0])

    def setCurrent(self, receipt):
        self.current = receipt

    def setStatus(self, status, msg=""):
        self.current.execution_date = datetime.date.today().isoformat()
        self.current.status         = status
        self.status                 = "processing"
        if status == "error":
            self.current.error      = msg
        else:
            next = self.current.id + 1
            if next > len(self.steps):
                self.status         = "finished"
            else:
                self.current        = self.steps[next]

    def addStep(self, command, dependencies, files, id, name):
        newStep = receipt(command, dependencies, files, id, name)
        self.steps.append(newStep)







