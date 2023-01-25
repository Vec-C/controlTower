from src.controlTower.domain.account import account
from src.controlTower.domain.design import design
from src.controlTower.services.architect import architect
from src.controlTower.utils.io import io
from src.controlTower import config
import click
import re

environment = True

@click.command()
@click.option('--id',      '-i', required=False, multiple=False, default="", prompt="Account ID", help="New Account Access_Id")
@click.option('--job',     '-j', required=True, multiple=False, default="", prompt="New Job", help="New Infrastructure Design Path")
@click.option('--secret',  '-s', required=False, multiple=False, default="", prompt="Account Secret", help="New Account Access_secret")
def job(job, id="", secret=""):
    global environment
    name      = job.split("/")[-2]
    version   = job.split("/")[-1]
    account   = createAccount(id, secret, name)
    newDesign = design(name, version, f'{job}/{config.RECEIPT}')
    project   = architect(account, newDesign)
    if(environment):
        project.execute()

def createAccount(access_id, access_secret, name, region=config.REGION):
    global environment
    configuration = io.read_data(config.AWS_CONFIG)
    newAccount    = account(access_id, access_secret, name, region)
    isset         = re.search('(' + config.AWS_PROFILE_PREFIX + ' ' + newAccount.name + ')', configuration).group(1)
    if isset is None:
        environment = newAccount.configure()

if __name__ == '__main__':
    job()