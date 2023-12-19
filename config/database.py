""" Database Settings """

import os

from masonite.environment import LoadEnvironment, env
from masoniteorm.query import QueryBuilder
from masoniteorm.connections import ConnectionResolver

"""
|--------------------------------------------------------------------------
| Load Environment Variables
|--------------------------------------------------------------------------
|
| Loads in the environment variables when this page is imported.
|
"""

LoadEnvironment()

"""
The connections here don't determine the database but determine the "connection".
They can be named whatever you want.
"""

DATABASES = {
    'default': 'postgres',
    'postgres': {
        'driver': 'postgres',
        'host': env('DB_HOST', 'localhost'),
        'user': env('DB_USERNAME', 'root'),
        'password': env('DB_PASSWORD', ''),
        'database': env('DB_DATABASE', 'masonite'),
        'port': env('DB_PORT', '5432'),
        'prefix': '',
        'log_queries': env('DB_LOG', False),
        'url': env('DATABASE_URL'),
    }
}

DB = ConnectionResolver().set_connection_details(DATABASES)
