from controlTower import config
from controlTower.entrypoints import studio
from controlTower.utils.io import IO
from controlTower.domain.model import Account, Design
from controlTower.services.architect import Architect
from datetime import date, timedelta
import re

# today = date.today()
# tomorrow = today + timedelta(days=1)

def test_read_Account():
    newAccount   = Account("access_id_111", "access_secret_111", "core-dev", "us-east-1")
    a = studio.createAccount(newAccount.access_id, newAccount.access_secret, newAccount.name, newAccount.region)
    configuration = IO().read_data(config.AWS_CONFIG)

    assert a == newAccount
    assert re.findall('(' + config.AWS_PROFILE_PREFIX + ' ' + newAccount.name + ')', configuration)[0] == "profile core-dev"
    #TODO: ADD ACCESS ID/SECRET VERIFICATION, DISTINCT FROM DUMMY, EQUALS TO THE ONE ALREADY IN THE FILE

def test_set_Account():
    newAccount   = Account("access_id_111", "access_secret_111", "test_111", "us-east-1")
    a = studio.createAccount(newAccount.access_id, newAccount.access_secret, newAccount.name, newAccount.region)
    configuration = IO().read_data(config.AWS_CONFIG)

    assert a == newAccount
    assert re.findall('(' + config.AWS_PROFILE_PREFIX + ' ' + newAccount.name + ')', configuration)[0] == "profile test_111"

def test_execute():
    newAccount = Account("access_id_111", "access_secret_111", "test_111", "us-east-1")
    newDesign  = Design("test_273", "0.1", f'tests/Makefile')
    job        = Architect(newAccount, newDesign)
    job.execute()

    assert job.design.status          == config.PROCESSING
    assert job.design.steps[0].status == config.SUCCESS
    assert job.design.current.status  == config.INIT

def test_steps_sequence():
    newAccount = Account("access_id_111", "access_secret_111", "test_111", "us-east-1")
    newDesign = Design("test_273", "0.1", f'tests/Makefile')
    job = Architect(newAccount, newDesign)
    job.execute()
    job.execute()

    assert job.design.steps[0].status    == config.SUCCESS
    assert job.design.steps[1].status    == config.SUCCESS
    assert job.design.steps[2].status    == config.INIT

    #TODO ERROR RESPONSES TESTS