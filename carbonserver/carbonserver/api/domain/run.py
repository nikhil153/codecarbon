import abc
from typing import List

from carbonserver.database import schemas, models


class RunInterface(abc.ABC):
    @abc.abstractmethod
    def add_save_run(self, run: schemas.RunCreate):
        raise NotImplementedError
