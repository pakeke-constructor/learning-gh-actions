
import os


DIR = "build/"

os.makedirs(DIR + "hello", exist_ok=True)


for i in range(5):
    with open(DIR + f"{i}.txt", "w+") as f:
        f.write(f"hello {i}")


with open(DIR + "hello/nested.txt", "w+") as f:
    f.write("ok, nested works.")


