import functools
import time

from django.db import transaction

from apps.delivery.services import periodically_add_patches
from celery import Task, shared_task
from celery.schedules import crontab
from celery.task import periodic_task


class BaseTaskWithRetry(Task):
    autoretry_for = (Exception, KeyError)
    retry_kwargs = {"max_retries": 5}
    retry_backoff = 5
    retry_jitter = True


class transaction_celery_task:
    """
    This is a decorator we can use to add custom logic to our Celery task
    such as retry or database transaction
    """

    def __init__(self, *args, **kwargs):
        self.task_args = args
        self.task_kwargs = kwargs

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            try:
                with transaction.atomic():
                    return func(*args, **kwargs)
            except Exception as e:
                # task_func.request.retries
                raise task_func.retry(exc=e, countdown=5)

        task_func = shared_task(*self.task_args, **self.task_kwargs)(wrapper_func)
        return task_func


@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True


@shared_task
def sample_task():
    print("The sample task just ran.")


@transaction_celery_task(base=BaseTaskWithRetry)
def task_process_periodically_add_patches(self):
    periodically_add_patches()


@periodic_task(run_every=(crontab(minute="*/1")), name="some_task", ignore_result=True)
def some_task():
    print("run_every minute='*/1'.")
