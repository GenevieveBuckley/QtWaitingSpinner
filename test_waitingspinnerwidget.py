from demo import Demo


def test_demo(qtbot):
    print("Success")
    window = Demo()
    window.show()
    qtbot.addWidget(window)
