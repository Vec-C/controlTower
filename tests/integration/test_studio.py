from controlTower import config
from controlTower.entrypoints import studio

def test_execute_job_fake_account():
    job = studio.job(config.TEST_FILE, 'core-dev')

    assert job.account.name           == "core-dev"
    assert job.design.name            == "core-dev"
    assert job.design.version         == "terra_ecsV4"
    assert job.design.current.id      == 1
    assert job.design.steps[0].status == config.SUCCESS

