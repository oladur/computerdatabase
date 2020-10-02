def whatever():
    return 9/0
def test_whatever():
    with pytest.raises(ZeroDivisionError):
        whatever()