import abc
import checksumdir
import datetime
import json
from src.controlTower import config
from src.controlTower.domain import job
from src.controlTower.utils.io import io

class AbstractRepository(abc.ABC):
    @abc.absctractmethod
    def add(self, job: job):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference ) -> job:
        raise NotImplementedError

class FileRepository(AbstractRepository):
    def __init__(self, job: job):
        self.date    = datetime.date.today().isoformat()
        self.job     = job
        if self.job is not None:
            self.path    = checksumdir.dirhash(job.design.name)
            self.version = job.design.version

    def add(self):
        data = io.to_json(self.job)
        return io.write_file(f'{self.path}/{self.version}/{self.date}.{config.FILE_EXTENSION}', data)

    def get(self, reference):
        return json.loads(io.read_data(reference))

    #TOOD
        #LIST
        # def list(self):
        #     return self.session.query(job).all()