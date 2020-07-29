try:
	foo()
except ArithmeticError as a:
	print(a.args)
except ZeroDivisionError:
    print("ZeroDivisionError")
except AssertionError:
    print("AssertionError")













