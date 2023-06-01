
import shutil
import os
import subprocess



MD_EXTENSION = ".md"

LEN_EXTEN = len(MD_EXTENSION)



def is_bad_extension(fname):
    is_md = fname[-LEN_EXTEN:] == MD_EXTENSION
    return is_md


assert is_bad_extension("hello.md")



ROOT = "C:\_PROGRAMMING\PY\learning_gh_actions"

BUILD_FOLDER = "_build"

IGNORE_FOLDERS = ["x_notes", ".git", ".github"]

SEP = os.path.sep




def should_ignore(dir):
    if BUILD_FOLDER in dir:
        return True
    for ignore in IGNORE_FOLDERS:
        if ignore in dir:
            return True




def copy_over_file(rt, fname):
    full_src = os.path.join(rt, fname)
    full_dst = os.path.join(rt, BUILD_FOLDER + SEP + fname)
    shutil.copyfile(full_src, full_dst)



def remove(root, fname):
    full = os.path.join(root, fname)
    print("FULL:", full)
    os.remove(full)




def ignore(dir, files):
    '''
    returns a list of files that should be ignored.
    '''
    to_ignore = [] # a list of files to be ignored
    if should_ignore(dir):
        to_ignore = files
        return to_ignore
    for file in files:
        if is_md_file(file):
            to_ignore.append(file)
    return to_ignore





def run():
    dest = ROOT + SEP + BUILD_FOLDER
    shutil.copytree(ROOT, dest, ignore=ignore)



run()
