from django_extensions.management.jobs import BaseJob
from scripts.create_csv import run


class Job(BaseJob):
    def execute(self): 
        run()
