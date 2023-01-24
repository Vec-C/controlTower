from src.controlTower.domain.account import account
from src.controlTower.domain.design import design
from src.controlTower.services.architect import architect
from src.controlTower.utils.io import reader
import click
import re

@click.command()
@click.option('--id',      '-i', required=False, multiple=False, default="", prompt="Account ID", help="New Account Access_Id")
@click.option('--job',     '-j', required=True, multiple=False, default="", prompt="New Job", help="New Infrastructure Design Path")
@click.option('--secret',  '-s', required=False, multiple=False, default="", prompt="Account Secret", help="New Account Access_secret")
def job(job, id="", secret=""):
    name    = job.split("/")[-1]
    account = createAccount(id, secret, name)
    design  = createDesign(job, name)
    project = architect(account, design)
    project.execute()

def createAccount(access_id, access_secret, name, region="us-east-1"):
    configuration = reader.read_data("~/.aws/config")
    newAccount    = account(access_id, access_secret, name, region)
    isset         = re.search('(profile' + newAccount.name + ')', configuration).group(1)
    if isset is None:
        newAccount.configure()

def createDesign(path, name):
    newDesign = design(name, path)


if __name__ == '__main__':
    job()