from plugin.console import GTKInterpreterConsole, Help, main


def test_help():
     help = Help()

     assert help() == "Usage: help(object)"


