"""
    this is a little more "conservative" in that it doesn't bring it into
    the namespace and you need to access it with . to be more specific.
    with small programs you can usually get away with just reading it into
    the namespace, with bigger programs it pays to be more specific
"""

import utils
import OtherUtils.utils_one_dir_down

# note we still have to specify where you're callng hello_world because
# we just imported utils, not "from utils import hello_world"
utils.hello_world()

# same shit here
OtherUtils.utils_one_dir_down.hello_world_from_other_dir()

"""
    basically this is in case you need to have things with matching names
    so you don't get confused or have a "namespace collision" in which two
    functions have the same name. it's not a great idea to do unless you
    need to do it. You will notice in each of the things that I am importing
    there is a function called get_money(). they have the same name but do
    different things. because we only imported the "first half" of what we
    need to use them, we can do some easily like this:
"""

# which get_money()? the one from utils
utils.get_money()

# which get_money() the one from OtherUtils.utils_one_dir_down
OtherUtils.utils_one_dir_down.get_money()

"""
    you've probaby seen this in R as 'utils::get_money()', using the C++ style
    imports, but I am going to cover all the bases in this in case we stumble
    onto something illuminating

    Python knows which one we mean because we access their path not just thier
    name. it's like we're usng their full name to specify which person we mean
    if we had use "from x import get_money" there would be two functions in
    the namespace called get_money() and the Python interpreter would not
    know which to use
"""
