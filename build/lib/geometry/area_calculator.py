def calculate_area(shape):
    if not hasattr(shape, 'area') or not callable(shape.area):
        raise TypeError("Объект должен иметь метод area()")
    return shape.area()
