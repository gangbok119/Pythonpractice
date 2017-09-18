class Shop:
    def __init__(self,name,shop_type,address):
        self.name = name
        self._shop_type = shop_type
        self.address = address
    def show_info(self):
        print('상점 (<{}>)\n  유형:{}\n  주소:{}'.format(self.name,self._shop_type,self.address))

    def change_type(self,new_shop_type):
        self._shop_type = new_shop_type


    @staticmethod
    def make_dummy():
        '''
        name: untitled
        shop_type: undefined
        address: unknown
        의 속성을 갖는 Shop객체를 생성해 리턴
        '''
        return Shop('untitled', 'undefined', 'unknown')

    @classmethod
    def make_dummy(cls):
        return cls('untitled', 'undefined', 'unknown')



    
class Restaurant(Shop):
    def show_info(self):
        print('식당 (<{}>)\n  유형:{}\n  주소:{}'.format(self.name,self._shop_type,self.address))


class Restaurant(Shop):
    """docstring forRestaurant."""
    def __init__(self, name, shop_type, address, rating=None):
        super().__init__(self, name, shop_type, address)
                self.arg = arg
