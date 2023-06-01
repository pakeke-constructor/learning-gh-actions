
import shutil
import os



INVALID_EXTENSIONS = [
    ".md", ".git", ".github"
]



def is_bad_extension(fname):
    _, exten = os.path.splitext(fname)
    for invalid_exten in INVALID_EXTENSIONS:
        if exten == invalid_exten:
            return True
    return False


assert is_bad_extension("hello.md")



# raise RuntimeError( "DON'T RUN THIS!!! YOU WERE ABOUT TO DUPLICATE THE ENTIRE FILESYSTEM")
# If you want to run this locally, set the root properly.
# Else, it will scan the entire filesys.
ROOT = "." # "C:\_PROGRAMMING\PY\learning_gh_actions"

IGNORE_FOLDERS = ["x_notes", ".git", ".github", "build"]

SEP = os.path.sep


BUILD_FOLDER = "build_output"


def should_ignore(dir):
    if BUILD_FOLDER in dir:
        return True
        
    for ignore in IGNORE_FOLDERS:
        if ignore in dir:
            return True
    return False



assert should_ignore("abc/.github")





def ignore(dir, files):
    '''
    returns a list of files that should be ignored.
    '''
    to_ignore = [] # a list of files to be ignored

    if should_ignore(dir):
        return files # ignore all files

    for file in files:
        if is_bad_extension(file):
            to_ignore.append(file)
    return to_ignore





def run():
    dest = ROOT + SEP + BUILD_FOLDER
    shutil.copytree(ROOT, dest, ignore=ignore)


