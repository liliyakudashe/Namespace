def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
#inner_function() # Результат выполнения программы:
# NameError: name 'inner_function' is not defined