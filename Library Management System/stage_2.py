from utilities import *
from common import *
from constants import *


def command_sd(command):
    global start_date
    start_date = datetime.strptime(command, '%m/%d/%Y')


def command_cb(command):
    info = token_parser(command)
    ## if info
    checkout_obj = Checkout(**info)
    checkouts[checkout_obj.book] = checkout_obj
