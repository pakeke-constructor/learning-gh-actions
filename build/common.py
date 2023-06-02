
import os


BUILD_FOLDER = "build"

IGNORE_FOLDERS = ["x_notes", ".git", ".github", BUILD_FOLDER]

SEP = os.path.sep

BUILD_OUTPUT_FOLDER = "build_output"

FILES_BUILD_OUTPUT_FOLDER =  BUILD_OUTPUT_FOLDER + SEP + "files"

FILES_BUILD_OUTPUT_ZIPNAME = "zipped"
FILES_BUILD_OUTPUT_ZIP_EXTEN = ".zip"



CURRENT_BUILD_TARGET = None

VALID_WINDOWS_TARGETS = ["win32", "win64"]
VALID_LINUX_TARGETS = ["linux32", "linux64"]

VALID_TARGETS = VALID_WINDOWS_TARGETS + VALID_LINUX_TARGETS




DLL_FOLDER = BUILD_FOLDER + SEP + "dlls"
def get_lib_path():
    return DLL_FOLDER + SEP + CURRENT_BUILD_TARGET


LOVE_FOLDER = BUILD_FOLDER + SEP + "love"
def get_love_path():
    return LOVE_FOLDER + SEP + CURRENT_BUILD_TARGET


VALID_ARCHES = ["64", "32"]

def get_os_name(os):
    if "windows" in os:
        return "win"
    elif "ubuntu" in os or "linux" in os:
        return "linux"
    raise RuntimeError("unsupported os")



def set_build_target(os, arch):
    assert arch in VALID_ARCHES
    name = get_os_name(os)
    global CURRENT_BUILD_TARGET
    CURRENT_BUILD_TARGET = name + arch


def is_windows():
    return CURRENT_BUILD_TARGET in VALID_WINDOWS_TARGETS

def is_linux():
    return CURRENT_BUILD_TARGET in VALID_LINUX_TARGETS



