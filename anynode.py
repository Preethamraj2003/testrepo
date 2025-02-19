class Category : 
    def __init__(self, name, parent_category=None):
        self.name = name
        self.parent_category=parent_category
class Product : 
    def __init__(self,pname,category):
        self.pname=pname
        self.category=category

    def display(self) :
        print(self.pname,end="_")
        print(self.category.name,end="_")
        cat = self.category.parent_category
        while cat : 
            print(cat.name, end="_")
            cat=cat.parent_category



def filter(productlist,filtername) : 

    for products in productlist: 
        cat = products.category
        while cat : 
            if cat==filtername: 
                print(products.pname) 
                break
            cat = cat.parent_category
                


eletronics = Category('electronics', None)
mobile=Category('Mobile', eletronics)
TV =Category('TV', eletronics)

Sony=Category('sony',TV)
Panasonic=Category('Panasonic',TV)
Android=Category('Android', mobile)
IOS = Category('IOS', mobile)


product1=Product('Ipad',IOS)
product2=Product('IPHONE', IOS)
product3=Product('S24',Android)
product4=Product('SonyTV',Sony)
product5=Product('PanasonicTV',Panasonic)
product6=Product('Realme',Android)




filter([product1,product2,product3,product4,product5,product6],mobile)
