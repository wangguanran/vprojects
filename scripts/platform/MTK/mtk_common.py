'''
@Author: WangGuanran
@Email: wangguanran@vanzotec.com
@Date: 2020-02-16 22:36:07
@LastEditTime: 2020-02-16 22:36:08
@LastEditors: WangGuanran
@Description: Mtk Common Operate py file
@FilePath: \vprojects\scripts\platform\MTK\mtk_common.py
'''

from scripts.log import log


class MTKCommon(object):

    def __init__(self):
        self.support_list = [
            "MT6735",
            "MT6739",
        ]

    def new_project(self, prj_info, args_info):
        log.debug("In!")
        # TODO 本地创建项目所需要的文件
        # * 根据新建项目所在平台（MTK/SPRD/RK）动态加载相关模块（mtk/sprd/rk_manager.py）(传入参数：项目名、项目平台)（返回操作句柄）
        # * Kernel部分 新建dts/dws/defconfig(MTK)
        # * Lk, Pl部分 拷贝相关文件，替换相关目录名
        # * Device目录下 拷贝.mk等配置信息，替换目录名
        pass

    def del_project(self, prj_info, args_info):
        log.debug("In!")
        pass

    def compile_project(self, prj_info, args_info):
        log.debug("In!")
        pass


# All platform scripts must contain this interface
def get_platform():
    return MTKCommon()
