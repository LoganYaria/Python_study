
def test_01(function_counter, class_counter, module_counter, session_counter):
    assert function_counter == True
    assert class_counter == True
    assert module_counter == True
    assert session_counter == True

def test_02(function_counter, class_counter, module_counter, session_counter):
    assert function_counter == True
    assert class_counter == True
    assert module_counter == True
    assert session_counter == True

class TestClass:

    def test_03(self, function_counter, class_counter, module_counter, session_counter):
        assert function_counter == True
        assert class_counter == True
        assert module_counter == True
        assert session_counter == True

    def test_04(self, function_counter, class_counter, module_counter, session_counter):
        assert function_counter == True
        assert class_counter == True
        assert module_counter == True
        assert session_counter == True