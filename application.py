import threading

__author__ = 'Guruguha'

import MetricsProvider
import multiprocessing
from flask import Flask, jsonify, request, render_template, make_response
import PerpetualStatisticsUpdater

application = Flask(__name__)
stats = PerpetualStatisticsUpdater.get_stats_object()


@application.route('/')
def interface_page():
    return jsonify({'Message':"Provide correct URL"})


@application.errorhandler(400)
def not_found(error, code):
    return make_response(jsonify({'error': error}), code)


@application.route('/api/stats/cpu/now', methods=['GET'])
def get_cpu_stats():
    try:
        arg = request.args.get("stat_type")
        if arg == "user":
            cpu_usage = MetricsProvider.cpu_usage().user
        elif arg == "system":
            cpu_usage = MetricsProvider.cpu_usage().system
        elif arg == "idle":
            cpu_usage = MetricsProvider.cpu_usage().idle
        else:
            cpu_usage = "Stats not found!!"

        return jsonify({'result': cpu_usage})
    except Exception:
        error_msg = "Invalid URL, please try again!"
        return not_found(error_msg, 400)


def get_cpu_usage():
    usage = MetricsProvider.cpu_usage()
    return jsonify({'user': usage.user, 'system': usage.system, 'idle': usage.idle})


@application.route('/api/stats/cpu', methods=['GET'])
def get_all_cpu_stats():
    try:
        cpu_usage = get_cpu_usage()
        return jsonify({"CPU Usage" : cpu_usage})
    except Exception:
        error_msg = "An error occured!"
        return not_found(error_msg)


def get_disk_usage(stat_type, detail_type=None):
    disk_usage = {}
    detailed_info = {}
    if detail_type:
        details = MetricsProvider.disk_usage(detail_type)
        detailed_info = {"read_count": details.read_count, "write_count": details.write_count}

    if stat_type == "total":
        disk_usage["total"] = MetricsProvider.disk_usage().total
    elif stat_type == "used":
        disk_usage["used"] = MetricsProvider.disk_usage().used
    elif stat_type == "free":
        disk_usage["free"] = MetricsProvider.disk_usage().free
    else:
        disk_usage["error_msg"] = "Stats not found!!"

    if len(detailed_info) == 0:
        return jsonify({"disk_usage":disk_usage})
    else:
        return jsonify({'disk_usage':disk_usage, 'details':detailed_info})


@application.route('/api/stats/disks/now', methods=['GET'])
def get_disk_stats():
    try:
        stat_type = request.args.get("stat_type")
        detail_type = request.args.get("detail_type")

        if detail_type == "detailed_io":
            details = get_disk_usage(stat_type, detail_type)
            return jsonify({"disk_stats": details})
        else:
            details = get_disk_usage(stat_type)
            return jsonify({"disk_stats": details})
    except Exception:
        error_msg = "An error occured!"
        return not_found(error_msg)


def get_memory_usage(stat_type):
    memory_usage = {}
    if stat_type == "total":
        memory_usage["total"] = MetricsProvider.memory_usage().total
    elif stat_type == "used":
        memory_usage["used"] = MetricsProvider.memory_usage().used
    elif stat_type == "free":
        memory_usage["free"] = MetricsProvider.memory_usage().free
    else:
        memory_usage["error_msg"] = "Stats not found!!"
    return jsonify({"memory_usage": memory_usage})


@application.route('/api/stats/memory/now', methods=['GET'])
def get_memory_stats():
    try:        
        stat_type = request.args.get("stat_type")
        details = get_memory_usage(stat_type)
        return details
    except Exception:
        error_msg = "An error occured!"
        return not_found(error_msg)


@application.route('/api/stats/memory', methods=['GET'])
def get_all_memory_stats():
    try:
        details = {}
        memory_usage = MetricsProvider.memory_usage()
        details['total'] = memory_usage.total
        details['available'] = memory_usage.available
        details['used'] = memory_usage.used
        details['free'] = memory_usage.free
        details['percent'] = memory_usage.percent
        return jsonify({"Memory_Stats":details})
    except Exception:
        error_msg = "An error occured!"
        return not_found(error_msg)


def start_server():
    application.run(debug=True, use_reloader=False)


if __name__ == '__main__':

    application.run(debug=True, use_reloader=False)

    p2 = multiprocessing.Process(target=PerpetualStatisticsUpdater.begin_statistics_updater)
    p2.start()



