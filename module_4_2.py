def test_function():
    def inner_function():
        print(f"Я в области видимости функции test_function")
    inner_function()
    print('************************')
    return inner_function
test_function()()   # так работает ))
inner_function()    # так не работает ((
