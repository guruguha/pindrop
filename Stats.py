from Util import CPUUsage, DiskUsage, NetworkUsage, MemoryUsage
import time
import MetricsProvider

# This class is used to save all statistics periodically (every one second)
# and also flush the stats after a 100 iterations
class Stats:
    stats_per_point_time = {}

    def __init__(self):
        self.cpu_usage = None
        self.disk_usage = None
        self.memory_usage = None
        self.network_usage = None

    def populate_current_stats(self):
        curr_time = int(time.time())
        current_bucket = curr_time - (curr_time % 60)
        self.update_stats()
        self.stats_per_point_time[current_bucket] = {"cpu": self.cpu_usage, "disk":self.disk_usage,
                                                     "network":self.memory_usage, "memory": self.memory_usage}

    def update_stats(self):
        self.update_cpu_usage()
        self.update_disk_usage()
        self.update_memory_usage()
        self.update_network_usage()

    def update_cpu_usage(self):
        cpu_usage_details = MetricsProvider.cpu_usage()
        cpu_usage_percent = MetricsProvider.cpu_usage_percent(False)
        cpu_count = MetricsProvider.cpu_count()
        self.cpu_usage = CPUUsage(cpu_usage_details.user, cpu_usage_details.system, cpu_usage_details.idle,
                                  cpu_usage_percent, cpu_count)

    def update_disk_usage(self):
        disk_usage_details = MetricsProvider.disk_usage("basic", "/")
        self.disk_usage = DiskUsage(disk_usage_details.total, disk_usage_details.used, disk_usage_details.free)

    def update_memory_usage(self):
        memory_usage_details = MetricsProvider.memory_usage()
        self.memory_usage = MemoryUsage(memory_usage_details.total, memory_usage_details.available,
                                        memory_usage_details.used, memory_usage_details.free, memory_usage_details.percent)

    def update_network_usage(self):
        network_usage_details = MetricsProvider.network_usage()
        self.network_usage = NetworkUsage(network_usage_details.bytes_recv, network_usage_details.bytes_sent,
                                          network_usage_details.packets_recv, network_usage_details.packets_sent)

    def get_stat_at_time(self, time):
        bucket = time - time % 60
        return 	self.stats_per_point_time[bucket]

    # def average_of_time(self, start_time, end_time, stat_name):
    #     result = []
    #     for bucket in range(start_time, end_time, 60):
    #         stat = self.get_stat_at_time(bucket)
    #         result.append(get the stat)
    #     return avg(result)

    def flush_old_stats(self):
        self.stats_per_point_time.clear()