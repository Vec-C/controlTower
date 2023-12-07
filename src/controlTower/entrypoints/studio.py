from controlTower.domain.model import Account, Design, Job
from controlTower.services.architect import Architect
from controlTower.utils.io import IO
from controlTower import config
import click
import re

# @click.command()
# @click.option('--account', '-s', required=False, multiple=False, default="", prompt="Account Name", help="Account name")
# @click.option('--id',      '-i', required=False, multiple=False, default="", prompt="Account ID", help="New Account Access_Id")
# @click.option('--job',     '-j', required=True, multiple=False, default="", prompt="New Job", help="New Infrastructure Design Path")
# @click.option('--secret',  '-s', required=False, multiple=False, default="", prompt="Account Secret", help="New Account Access_secret")
def job(job, profile, id="", secret=""):
    name      = job.split("/")[-2]
    version   = job.split("/")[-1]
    account   = createAccount(id, secret, profile)
    newDesign = Design(name, version, f'{job}/{config.RECEIPT}' )
    job       = Architect(account, newDesign)
    if account is not False:
        job.execute()
    return Job(job.account, job.design)

def createAccount(access_id, access_secret, name, region=config.REGION):
    configuration = IO().read_data(config.AWS_CONFIG)
    newAccount    = Account(access_id, access_secret, name, region)
    isset         = re.findall('(' + config.AWS_PROFILE_PREFIX + ' ' + newAccount.name + ')', configuration)
    if isset == []:
        return newAccount.configure()
    else:
        return newAccount

#TODO: SAVE WITH FILEREPOSITORY
def save():
    pass

if __name__ == '__main__':
    job()