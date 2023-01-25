from src.controlTower.domain import account
from src.controlTower.domain import design

class job:
    def __init__(self, account: account, design: design):
        self.account = account
        self.design  = design