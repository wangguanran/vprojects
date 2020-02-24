'''
@Author: WangGuanran
@Email: wangguanran@vanzotec.com
@Date: 2020-02-23 15:29:44
@LastEditTime: 2020-02-23 16:02:27
@LastEditors: WangGuanran
@Description: Platform manager operate py file
@FilePath: \vprojects\scripts\pm.py
'''

import os
import sys

if __name__ == "__main__":
    if os.path.basename(os.getcwd()) == "vprojects":
        sys.path.append(os.getcwd())
    elif os.path.basename(os.getcwd()) in ["vprjcore","scripts"]:
        sys.path.append(os.path.dirname(os.getcwd()))
    else:
        sys.path.append(os.path.join(os.getcwd(),"vprojects"))

    from vprjcore.platform_manager import parse_cmd,PlatformManager
    args_dict = parse_cmd()
    project = PlatformManager(args_dict)