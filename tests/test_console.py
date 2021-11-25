from plugin.console import Help, main


def test_help():
     help = Help()

     assert help() == "Usage: help(object)"
