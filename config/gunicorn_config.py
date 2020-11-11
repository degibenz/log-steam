import os

API_SERVER_PORT = os.getenv("SERVER_PORT", 9000)

bind = ":%s" % API_SERVER_PORT
access_log_format = '%a %l %u %t "%r" %s %b %Tf "%{Referrer}i" "%{User-Agent}i" "%{X-Request-ID}i"'
workers = os.getenv("GUNICORN_WORKERS_COUNT", 10)
worker_class = "aiohttp.GunicornWebWorker"
timeout = os.getenv("GUNICORN_WORKERS_TIMEOUT", 36)
capture_output = os.getenv("GUNICORN_CAPTURE_OUTPUT", True)
max_requests = os.getenv("GUNICORN_MAX_REQUEST", 25000)
pythonpath = '/app/src/'
