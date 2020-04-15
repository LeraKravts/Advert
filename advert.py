class ColorizeMixin:
    def __init__(self, repr_color_code):
        self.repr_color_code = repr_color_code


class Advert(ColorizeMixin):
    def __init__(self,  mapping, price=0):
        self.price = price
        self.repr_color_code = 33
        for key in mapping:
            if isinstance(mapping[key], dict):
                value = Advert(mapping[key])
            else:
                value = mapping[key]
            self.__setattr__(key, value)

    def __setattr__(self, key, value):
        if key == 'price' and value < 0:
            raise Exception('ValueError: price must be >= 0')
        if key == 'class':
            key = 'class_'
        self.__dict__[key] = value

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};45m {self.title} | {self.price} ₽'
    
