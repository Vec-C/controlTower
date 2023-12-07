from abc import ABCMeta, abstractmethod
from controlTower import config
from controlTower.domain.model import Account, Design, Job, Receipt
from controlTower.utils.io import IO
import hashlib
import json


class AbstractRepository(metaclass=ABCMeta):
    @abstractmethod
    def add(self, job: Job):
        raise NotImplementedError

    @abstractmethod
    def get(self, reference) -> Job:
        raise NotImplementedError

class FileRepository(AbstractRepository):
    def __init__(self, job: Job=None):
        self.date    = config.NOW_FILE
        self.time    = config.NOW_UTC
        self.job     = job
        if self.job is not None:
            h = hashlib.new(config.HASH_LGRTHM)
            h.update((self.job.design.name + self.job.design.version).encode(config.ENCODING))
            self.path    = f"{config.ROOTREPOSITORY}/{h.hexdigest()[-config.HASH_DIR_LENGTH:]}/{self.date}_{id(self)}.{config.FILE_EXTENSION}"

    def add(self):
        data = json.dumps(IO().pretty_print(self, (Job, Account, Design, Receipt)))
        return IO().write_data(f'{self.path}', data)

    def get(self, path):
        return IO().read_data(path)

    #TOOD
        #LIST
        # def list(self):
        #     return self.session.query(job).all()

#TODO: S3 BUCKET REPOSITORY
class BucketRepository(AbstractRepository):
    def __init__(self, job: Job=None):
        self.date    = config.NOW_UTC
        self.job     = job
        if self.job is not None:
            self.path    = f"{config.ROOTREPOSITORY}/{hashlib.md5().update((job.design.name + job.design.version).encode(config.ENCODING))}/{self.date}_{id(self)}.{config.FILE_EXTENSION}"


    def add(self):
        data = json.dumps(IO().pretty_print(self, (Job, Account, Design, Receipt)))
        return IO().write_data(f'{self.path}', data)

    def get(self, path):
        return json.loads(IO().read_data(path))

    #TOOD
        #LIST
        # def list(self):
        #     return self.session.query(job).all()

#TODO: FAKE REPOSITORY