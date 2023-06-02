
import zip_source
import convert_to_exe
import common



# todo: take from env var or something
common.set_build_target("win64")


# zip up the source code
zip_source.run()

# convert to executable program
convert_to_exe.run()


