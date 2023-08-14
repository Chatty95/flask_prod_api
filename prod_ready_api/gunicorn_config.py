import multiprocessing

bind = "0.0.0.0:8100"
workers = 2
# multiprocessing.cpu_count()*2 +1
threads = 2
worker_class = "gthread"
timeout = 30
keepalive = 2
