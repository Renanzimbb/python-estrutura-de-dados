from average_two_numbers import average_two_numbers

def test_2_3():
    result = average_two_numbers(2,3)
    assert result ==2.5

def test_0_100():
    result = average_two_numbers(0,100)
    assert result == 50

if __name__ == '__name__':
    test_2_3()
    test_0_100()

