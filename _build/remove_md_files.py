
import shutil
import os
import subprocess



MD_EXTENSION = ".md"

LEN_EXTEN = len(MD_EXTENSION)



def is_md_file(fname):
    return fname[:LEN_EXTEN] == MD_EXTENSION



ROOT = "C:\_PROGRAMMING\PY\learning_gh_actions"

BUILD_FOLDER = "_build"

IGNORE_FOLDERS = ["x_notes", ".git", ".github"]

SEP = os.path.sep



def should_ignore(name):
    for ignore in IGNORE_FOLDERS:
        if ignore in name:
            return True




def copy_over_file(rt, fname):
    full_src = os.path.join(rt, fname)
    full_dst = os.path.join(rt, BUILD_FOLDER + SEP + fname)
    print(full_src, full_dst)
    shutil.copyfile(full_src, full_dst)



for rt, dirs, files in os.walk(ROOT):
    for dirname in dirs:
        if dirname.startswith(BUILD_FOLDER):
            continue
        if not should_ignore(dirname):
            os.makedirs(os.path.join(rt,dirname), exist_ok=True)
    for filename in files:
        if should_ignore(filename) or filename.startswith(BUILD_FOLDER):
            continue
        if not is_md_file(filename):
            copy_over_file(rt, filename)




