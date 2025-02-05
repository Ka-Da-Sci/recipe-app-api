"""Django command to wait for the database to be available."""

import time
from django.core.management.base import BaseCommand
from psycopg import errors
from django.db.utils import OperationalError

PscopgOperationalError = errors.OperationalError


class Command(BaseCommand):
    """Django command to wait for the database to be available"""

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
            except (OperationalError, PscopgOperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
            else:
                db_up = True
        self.stdout.write(self.style.SUCCESS('Database available!'))
