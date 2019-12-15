from plugin.console import Help


def test_help():
    help = Help()

    assert help() == "Usage: help(object)"
