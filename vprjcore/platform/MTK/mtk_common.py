'''
@Author: WangGuanran
@Email: wangguanran@vanzotec.com
@Date: 2020-02-16 22:36:07
@LastEditTime: 2020-02-21 00:30:16
@LastEditors: WangGuanran
@Description: Mtk Common Operate py file
@FilePath: \vprojects\vprjcore\platform\MTK\mtk_common.py
'''

import os
import shutil
from functools import partial

from vprjcore.log import log


get_full_path = partial(os.path.join, os.getcwd(), "new_project_base")
NEW_PROJECT_DIR = get_full_path()
DEFAULT_BASE_NAME = "demo"


class MTKCommon(object):

    def __init__(self):
        self.support_list = [
            "MT6735",
            "MT6739",
        ]

    def new_project(self, *args, **kwargs):
        log.debug("In!")
        project_name = args[0].prj_info["name"].lower()
        is_board = args[0].arg_list["is_board"]
        platform = args[0].arg_list["platform"].lower()
        log.debug("project_name = %s,is_board = %s,platform = %s" %
                  (project_name, is_board, platform))
        basedir = get_full_path(platform)
        destdir = os.path.join(os.getcwd(), project_name)
        log.debug("basedir = %s destdir = %s" % (basedir, destdir))
        if os.path.exists(basedir):
            if os.path.exists(destdir):
                log.error(
                    "The project has been created and cannot be created repeatedly")
            else:
                shutil.copytree(basedir, destdir,symlinks="True")
                self.modify_filename(destdir, project_name)
                self.modify_filecontent(destdir, project_name)
                log.debug("new project '%s' down!" % (project_name))
                return True
        else:
            log.error("No platform file, unable to create new project")

        return False

    def modify_filename(self, path, project_name):
        for p in os.listdir(path):
            p = os.path.join(path, p)
            if os.path.isdir(p):
                self.modify_filename(p, project_name)
            if DEFAULT_BASE_NAME in os.path.basename(p):
                p_dest = os.path.join(os.path.dirname(
                    p), os.path.basename(p).replace(DEFAULT_BASE_NAME, project_name))
                os.rename(p, p_dest)

    def modify_filecontent(self, path, project_name):
        ini_filepath = os.path.join(path, "env_"+project_name+".ini")
        log.debug("ini_filepath = %s" % (ini_filepath))
        with open(ini_filepath, "r+") as f_rw:
            content = f_rw.readlines()
            f_rw.seek(0)
            f_rw.truncate()
            for line in content:
                line = line.replace(DEFAULT_BASE_NAME, project_name)
                f_rw.write(line)
            f_rw.close()

    def del_project(self, *args, **kwargs):
        log.debug("In!")

    def compile_project(self, *args, **kwargs):
        log.debug("In!")


# All platform scripts must contain this interface
def get_platform():
    return MTKCommon()
