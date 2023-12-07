from   controlTower.domain.model import Account, Design

def test_create_account_design():
    newAccount   = Account("access_id_273", "access_secret_273", "test_273", "us-east-1")
    newDesign    = Design("test_273", "0.1", f'tests/Makefile')
    newSteps     = []
    for step in newDesign.steps:
        newSteps.append(step.name)

    assert newAccount.name      == "test_273"
    assert newSteps == ["set", "feedPipelines", "auroraAcces", "apiInfo", "verifyAPI", "capacities", "policy", "listIPS", "envVariables", "black"]

