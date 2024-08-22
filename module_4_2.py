def test_function():
    def inner_function():
        print( "Я в области видимости функции test_function")
    inner_function() # Вызов внутренней функции
test_function() # Вызов внешней функции