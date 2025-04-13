import KWICMainProgramSubroutine


def user_input_test():
    assert KWICMainProgramSubroutine.user_input() == ["my name is wyatt"]
    assert KWICMainProgramSubroutine.user_input() == ["How are you"]
    assert KWICMainProgramSubroutine.user_input() == ["my 678 is 545"]


def circular_shifterTest():
    assert KWICMainProgramSubroutine.circular_shifter(["my name is wyatt"]) == ["my name is wyatt", "name is wyatt my", "is wyatt my name", "wyatt my name is"]
    print(KWICMainProgramSubroutine.circular_shifter(["my name is wyatt"]))
#def alphabetizerTest():

#def outputTest():

#user_input_test()
circular_shifterTest()
