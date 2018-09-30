# "from x import y" allows you to call the functions freely with just its name.
# you're said to have brought the fuction into the local "namespace".
from utils import hello_world

"""
    if it's one directory down, you need to access the folder then the code
    with the name of the folder and the . you're essentially  walking down
    the projects's directory structure until you hit the functions. look at
    the OtherUtils folder and it should make sense
"""

from OtherUtils.utils_one_dir_down import hello_world_from_other_dir

# this is a simple import form the same folder
hello_world()

# we call it freely because it's floating around in the namespace

# this is the one from a directory down
hello_world_from_other_dir()
