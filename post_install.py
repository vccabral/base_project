from django.core import management
from base_project.settings import INSTALLED_APPS

management.call_command('syncdb', noinput = True)

for app in INSTALLED_APPS:
    management.call_command('schemamigration', initial = True)

for app in INSTALLED_APPS:
    management.call_command('migrate')
