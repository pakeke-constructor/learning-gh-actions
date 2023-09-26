
import shutil
import common
import os

from common import *



def copy_over_libs():
    dll_path = common.get_lib_path()
    shutil.copytree(dll_path, common.BUILD_OUTPUT_FOLDER, dirs_exist_ok=True)



def fuse_exe_windows():
    love_binary = None
    zip_binary = None
    love_path = common.get_love_path() + SEP + "love.exe"

    with open(love_path, "rb") as f:
        love_binary = f.read()

    zip_path = BUILD_OUTPUT_FOLDER + SEP + FILES_BUILD_OUTPUT_ZIPNAME + FILES_BUILD_OUTPUT_ZIP_EXTEN
    with open(zip_path, "rb") as zp:
        zip_binary = zp.read()
    os.remove(zip_path)

    exe_path = BUILD_OUTPUT_FOLDER + SEP + "umg.exe"
    with open(exe_path, "wb+") as out:
        out.write(love_binary + zip_binary)


def copy_over_love():
    love_path = common.get_love_path()
    shutil.copytree(love_path, common.BUILD_OUTPUT_FOLDER, dirs_exist_ok=True)


def run():
    # copy shared object libs over
    copy_over_libs()

    # copy over love dlls, and love exe
    copy_over_love()

    if common.is_windows():
        fuse_exe_windows()
    else:
        raise RuntimeError("platform not supported yet")

