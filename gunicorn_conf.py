from multiprocessing import cpu_count

# Socket Path
bind = "unix:/home/admin/todoapi/gunicorn.sock"

# Worker Options
workers = cpu_count()
worker_class = "uvicorn.workers.UvicornWorker"

# Logging Options
loglevel = "debug"
accesslog = "/home/admin/todoapi/access_log"
errorlog = "/home/admin/todoapi/error_log"
