# This class is a place holder for current stats of CPU
class CPUUsage:

    def __init__(self, user_time, system_time, idle_time, cpu_percent, cpu_count):
        self.user_time = user_time
        self.system_time = system_time
        self.idle_time = idle_time
        self.cpu_percent = cpu_percent
        self.cpu_count = cpu_count

    def get_user_time(self):
        return self.user_time

    def get_system_time(self):
        return self.system_time

    def get_cpu_percent(self):
        return self.cpu_percent

    def get_cpu_count(self):
        return self.cpu_count


# This class is a place holder for current stats of Disk
class DiskUsage:

    def __init__(self, total_space, used_space, free_space):
        self.total_space = total_space
        self.free_space = free_space
        self.used_space = used_space

    def get_total_space(self):
        return self.total_space

    def get_free_space(self):
        return self.free_space

    def get_used_space(self):
        return self.used_space


# This class is a place holder for current stats of Network
class NetworkUsage:

    def __init__(self, bytes_rcvd, bytes_sent, pkts_rcvd, pkts_sent):
        self.bytes_received = bytes_rcvd
        self.bytes_sent = bytes_sent
        self.packets_received = pkts_rcvd
        self.packets_sent = pkts_sent

    def get_bytes_sent(self):
        return self.bytes_sent

    def get_bytes_received(self):
        return self.bytes_received

    def get_packets_sent(self):
        return self.packets_sent

    def get_packets_received(self):
        return self.packets_received


# This class is a place holder for current stats of Memory
class MemoryUsage:
    def __init__(self, total, available, used, free, percent):
        self.total_mem = total
        self.available_mem = available
        self.used_mem = used
        self.free_mem = free
        self.percent = percent

    def get_total_memory(self):
        return self.total_mem

    def get_available_memory(self):
        return self.available_mem

    def get_used_memory(self):
        return self.used_mem

    def get_free_memory(self):
        return self.free_mem

    def get_percent(self):
        return self.percent
