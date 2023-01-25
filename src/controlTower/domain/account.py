from invoke import run, Failure

class account:

    def __init__(self, access_id: str, access_secret: str, name: str, region: str):
        self.access_id     = access_id
        self.access_secret = access_secret
        self.name          = name
        self.region        = region

    def configure(self):
        try:
            set = run(f'aws --profile {self.account.name} configure set aws_access_key_id "{self.account.access_id}"', pty=True)
            set = run(f'aws --profile {self.account.name} configure set aws_secret_access_key "{self.account.access_secret}"', pty=True)
            set = run(f'aws --profile {self.account.name} configure set region "{self.account.region}"', pty=True)
        except Failure:
            print(set.result)
            return False
        else:
            return True
