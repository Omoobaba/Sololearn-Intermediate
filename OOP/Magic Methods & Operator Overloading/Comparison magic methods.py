class SpecialString:
    def __init__(self, cont) -> None:
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont) + 1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs


"""As you can see, you can define an custom behavior for the overloaded operator"""