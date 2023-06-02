
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


LOVE_FOLDER = BUILD_FOLDER + SEP + "dlls"
def get_love_path():
    return LOVE_FOLDER + SEP + CURRENT_BUILD_TARGET


def set_build_target(targ):
    assert targ in VALID_TARGETS
    global CURRENT_BUILD_TARGET
    CURRENT_BUILD_TARGET = targ


def is_windows():
    return CURRENT_BUILD_TARGET in VALID_WINDOWS_TARGETS

def is_linux():
    return CURRENT_BUILD_TARGET in VALID_LINUX_TARGETS



