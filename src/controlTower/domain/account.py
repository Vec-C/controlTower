from invoke import run

class account:
    access_id     : str
    access_secret : str
    name          : str
    region        : str

    def __init__(self, access_id, access_secret, name, region):
        self.access_id     = access_id
        self.access_secret = access_secret
        self.name          = name
        self.region        = region

    def configure(self):
        run(f'aws --profile {self.account.name} configure set aws_access_key_id "{self.account.access_id}"', pty=True)
        run(f'aws --profile {self.account.name} configure set aws_secret_access_key "{self.account.access_secret}"', pty=True)
        run(f'aws --profile {self.account.name} configure set region "{self.account.region}"', pty=True)
