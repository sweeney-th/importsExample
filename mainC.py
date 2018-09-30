# here is an example of how to shoot yourself in the foot
from utils import get_money
from OtherUtils.utils_one_dir_down import get_money

# which to use? who the fuck knows? (ends up printing the second part twice)
get_money()
get_money()

"""
    Python has no choice but to use the most recent one, having
    "overwritten" the last one, which makes a certain amount of sense but
    is not going to do what the programmer thought it was going to.
"""
