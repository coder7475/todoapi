from multiprocessing import cpu_count

# Socket Path
bind = "0.0.0.0:8000"
# Worker Options
workers = cpu_count()
worker_class = "uvicorn.workers.UvicornWorker"

# Logging Options
loglevel = "debug"
accesslog = "/home/admin/todoapi/access_log"
errorlog = "/home/admin/todoapi/error_log"
