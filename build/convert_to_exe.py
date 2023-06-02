
import shutil
import common

from common import SEP



def copy_over_libs():
    dll_path = common.get_lib_path()
    shutil.copytree(dll_path, common.BUILD_OUTPUT_FOLDER, dirs_exist_ok=True)



def fuse_exe_windows():
    love_binary = None
    zip_binary = None
    love_path = common.get_love_path() + SEP + "love.exe"

    with open(love_path, "r") as f:
        love_binary = f.read()

    with open("build/zipped.zip", "r") as zp:
        zip_binary = zp.read()

    with open("umg.exe", "w+") as out:
        out.write(love_binary + zip_binary)



def copy_over_love():
    love_path = common.get_love_path()
    shutil.copytree(love_path, common.BUILD_OUTPUT_FOLDER, dirs_exist_ok=True)


def run():
    copy_over_libs()
    copy_over_love()

    shutil.make_archive("zipped", "zip", common.FILES_BUILD_OUTPUT_FOLDER)

    if common.is_windows():
        fuse_exe_windows()
    else:
        raise RuntimeError("platform not supported yet")

