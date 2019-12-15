from plugin.console import Help


def test_help():
    help2 = Help()

    assert help2() == "Usage: help(object)"
