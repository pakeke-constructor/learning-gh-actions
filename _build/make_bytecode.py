
import os
import subprocess





LUA_EXTENSION = ".lua"

BYTECODE_EXTENSION = ".out"

LUA_EXTEN_LEN = len(LUA_EXTENSION)



def replace_lua_exten(fname):
    return fname[:LUA_EXTEN_LEN] + BYTECODE_EXTENSION


def is_lua_src_file(fname):
    return fname[:LUA_EXTEN_LEN] == LUA_EXTENSION


def convert_to_bytecode(fname):
    out_fname = replace_lua_exten(fname)
    result = subprocess.check_output(f"luajit.exe -b {fname} {out_fname}")
    print(result)





root = "C:\_PROGRAMMING\PY\learning_gh_actions"

for rt, dirs, files in os.walk(root):
    for filename in files:
        if is_lua_src_file(filename):
            convert_to_bytecode(os.path.join(rt, filename))
    for dirname in dirs:
        pass


