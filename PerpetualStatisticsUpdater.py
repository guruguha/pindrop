from Stats import Stats
import time

stats = Stats()
flush_stat_rate = 100


def start_stats_update(cur_itr):
    print("Updating stats..." + str(flush_stat_rate - cur_itr) + " iterations remaining to flush!")
    if cur_itr == flush_stat_rate:
        print("Flushing old statistics...")
        stats.flush_old_stats()
    stats.populate_current_stats()


def get_stats_object():
    return stats


def begin_statistics_updater():
    start_time = time.time()
    cur_stat_itr = 0
    while True:
        # update the system stats every 1 second
        start_stats_update(cur_stat_itr)
        cur_stat_itr += 1
        time.sleep(1.0 - ((time.time() - start_time) % 1.0))
