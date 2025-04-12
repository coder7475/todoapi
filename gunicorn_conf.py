from multiprocessing import cpu_count

# Socket Path
bind = "unix:/home/todoapi/gunicorn.sock"

# Worker Options
workers = cpu_count()
worker_class = "uvicorn.workers.UvicornWorker"

# Logging Options
loglevel = "debug"
accesslog = "/home/todoapi/access_log"
errorlog = "/home/todoapi/error_log"
