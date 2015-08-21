## Broker settings.
BROKER_URL = 'amqp://'

# List of modules to import when celery starts.
CELERY_IMPORTS = ('crawlclima.tasks', )

## Using the database to store task state and results.
CELERY_RESULT_BACKEND = 'mongodb'
CELERY_TASK_RESULT_EXPIRES = 18000  # 5 hours.

CELERY_ROUTES = {
    'tasks.pega_dados_cemaden': 'high-priority',
}

CELERY_ANNOTATIONS = {'tasks.pega_dados_cemaden': {'rate_limit': '10/s'}}


