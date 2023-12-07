from controlTower.adapters.repository import FileRepository
from controlTower.domain.model import Account, Design, Receipt, Job
from controlTower.entrypoints import studio
from controlTower.utils.io import IO
from controlTower import config

import json

def test_execute_job_fake_account():
    job = studio.job(config.TEST_FILE, 'core-dev')
    doc = FileRepository(job)

    tempObject = {"date": doc.date, "time": doc.time, "job": job, "path": doc.path}

    write_it = doc.add()
    read_it  = FileRepository().get(doc.path)

    assert write_it  ==  True
    assert read_it   ==  json.dumps(IO().pretty_print(tempObject, (Account, Design, Job, Receipt)))
