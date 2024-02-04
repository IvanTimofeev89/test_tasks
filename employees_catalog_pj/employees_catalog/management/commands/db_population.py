from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from random import randint

from employees_catalog.models import Employees

fake = Faker()


class Command(BaseCommand):
    help = 'DB population with test data'

    def add_arguments(self, parser):
        parser.add_argument('--levels', type=int, help='Number of hierarchy levels')
        parser.add_argument('--emp_amount', type=int, help='Number of employees per level')

    @transaction.atomic
    def handle(self, *args, **kwargs):
        hierarchy_levels = kwargs.get('levels', 5)
        emp_amount = kwargs.get('emp_amount', 20)

        for level in range(hierarchy_levels):
            for _ in range(emp_amount):
                supervisor = None
                if level != 0:
                    supervisor = Employees.objects.filter(hierarchy_level=level - 1).order_by('?').first()

                employee = Employees.objects.create(
                    name=fake.name(),
                    position=fake.job(),
                    hire_date=fake.date_this_decade(),
                    salary=randint(30000, 100000),
                    hierarchy_level=level,
                    supervisor=supervisor
                )
                if supervisor:
                    supervisor.subordinates.add(employee)
