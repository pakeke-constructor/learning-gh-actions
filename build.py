
import os

os.makedirs("build/hello")


for i in range(5):
    with open(f"{i}.txt") as f:
        f.write(f"hello {i}", "w+")


