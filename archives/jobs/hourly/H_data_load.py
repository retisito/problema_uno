from django_extensions.management.jobs import BaseJob
from scripts.data_load import run


class Job(BaseJob):
    def execute(self): 
        #run()
        pass
