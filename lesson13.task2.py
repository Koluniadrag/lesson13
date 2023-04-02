def outer():
    def inner():
        print("Это внутренняя функция")
    return inner

inner= outer()

inner()
