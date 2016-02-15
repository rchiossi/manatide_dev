import sys
import time
import os


class log:
    log_name = None
    log_level = 4

    @staticmethod
    def _log(entry, log_level):
        if log.log_level > log_level:
            print(entry)

        if log.log_name is not None:
            with open(log.log_name, 'a') as f:
                f.write("%s\n" % entry)

    @staticmethod
    def e(msg):
        entry = "[%s][!!!] %s" % (time.strftime("%I:%M.%S"), msg)
        log._log(entry, 0)
        raise(Exception(msg))

    @staticmethod
    def w(msg):
        entry = "[%s][!] %s" % (time.strftime("%I:%M.%S"), msg)
        log._log(entry, 1)

    @staticmethod
    def i(msg):
        entry = "[%s] %s" % (time.strftime("%I:%M.%S"), msg)
        log._log(entry, 2)

    @staticmethod
    def d(msg):
        entry = "[%s][*] %s" % (time.strftime("%I:%M.%S"), msg)
        log._log(entry, 3)

    @staticmethod
    def init_logfile(dirname=None):
        name = "%s.log" % time.strftime("%Y.%m.%d-%I.%M.%S")

        if dirname is not None:
            if not os.path.exists(dirname):
                os.makedirs(dirname)

            name = "%s/%s" % (dirname, name)

        log.log_name = name

    @staticmethod
    def set_loglevel(level):
        log.log_level = level
