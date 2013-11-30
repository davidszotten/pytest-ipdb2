import sys

import py


def pytest_configure(config):
    original_trace = py.std.ipdb.set_trace

    def cleanup():
        py.std.ipdb.set_trace = original_trace

    def set_trace():
        # we don't want to drop in here, but at the point of the oriainal
        # set_trace statement
        frame = sys._getframe().f_back

        capman = config.pluginmanager.getplugin("capturemanager")
        out, err = capman.suspendcapture()
        original_trace(frame)

    py.std.ipdb.set_trace = set_trace
    config._cleanup.append(cleanup)


