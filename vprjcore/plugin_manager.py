'''
@Author: WangGuanran
@Email: wangguanran@vanzotec.com
@Date: 2020-02-19 23:10:49
@LastEditTime: 2020-02-21 17:55:55
@LastEditors: WangGuanran
@Description: Plugin manager py file
@FilePath: \vprojects\vprjcore\plugin_manager.py
'''
import os
import sys
from functools import partial

from vprjcore.log import log

get_full_path = partial(os.path.join, os.getcwd(), "vprjcore", "plugins")
PROJECT_PLUGIN_PATH = get_full_path()


class PluginManager(object):

    '''
    Singleton mode
    '''
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.name = __name__
        self._plugin_info = {}
        self.plugin_list = {}
        self._loadPlugins()

    def _loadPlugins(self):
        for filename in os.listdir(PROJECT_PLUGIN_PATH):
            if not filename.endswith(".py") or filename.startswith("_"):
                continue
            pluginName = os.path.splitext(filename)[0]
            log.debug("pluginName = %s" % (pluginName))
            packageName = __package__ + ".plugins."+pluginName
            log.debug("packageName = %s" % (packageName))
            plugin_module = __import__(packageName, fromlist=[pluginName])

            if hasattr(plugin_module, "get_plugin_object"):
                plugin = plugin_module.get_plugin_object()
                plugin.filename = plugin_module.__file__
                plugin.pluginName = pluginName
                plugin.packageName = packageName
                self.register_plugin(plugin)
            else:
                log.warning("file '%s' does not have attr:'get_plugin_object',fail to register plugin" %
                            (plugin_module.__file__))

    def register_plugin(self, plugin):
        attrlist = dir(plugin)
        log.debug(attrlist)

        plugin.operate_list = {}
        for attr in attrlist:
            if not attr.startswith("_"):
                funcaddr = getattr(plugin, attr)
                if callable(funcaddr):
                    if "_" in attr:
                        index, operate = attr.split(sep="_",maxsplit=1)
                        if not operate in plugin.operate_list.keys():
                            plugin.operate_list[operate] = {}
                        plugin.operate_list[operate][index] = funcaddr
        log.debug(plugin.operate_list)
        if plugin.operate_list:
            log.debug("register '%s' successfully!" % (plugin.pluginName))
            self._plugin_info[plugin.pluginName] = plugin
        else:
            log.warning("No matching function in '%s'" % (plugin.pluginName))

    def get_plugin_info(self):
        return self._plugin_info


def get_module():
    return PluginManager()

if __name__ == "__main__":
    plugin = PluginManager()

'''
from vprjcore.log import log

class Plugin(object):
    def __init__(self):
        # If support_list and unsupported_list are not specified in the plug-in,
        #   all platforms are supported by default
        # self.support_list=[
        #     ""
        # ]
        # self.unsupported_list=[
        #     ""
        # ]
        pass

    def before_new_project(self, project):
        log.debug("In!")

    def before_compile(self, project):
        log.debug("In!")

    def after_compile(self, project):
        log.debug("In!")

def get_plugin_object():
    # All plugin must contain this interface
    return Plugin()
'''
