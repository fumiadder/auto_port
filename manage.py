#!/usr/bin/env python
import os
import sys
import threading
from utils.CrontabHand import run

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auto_port.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    # 起一个线程执行定时任务
    # threading.Thread(target=run).start()

    execute_from_command_line(sys.argv)
