import psutil


def cpu_usage():
    return psutil.cpu_times()


def cpu_usage_percent(per_cpu):
    return psutil.cpu_percent(percpu=per_cpu)


def cpu_count():
    return psutil.cpu_count()


def memory_usage():
    return psutil.virtual_memory()


def disk_usage(param=None, directory=None):
    if param == "basic":
        return psutil.disk_usage(directory)
    else:
        return psutil.disk_io_counters()


def network_usage():
    return psutil.net_io_counters()
