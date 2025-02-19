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
    for products in productlist : 
        if products.category==filtername : 
            print(products.pname)

eletronics = Category('electronics', None)
mobile=Category('Mobile', eletronics)
Android=Category('Android', mobile)
IOS = Category('Iphone', mobile)

pr1=Product('Ipad',IOS)
pr2=Product('Iprg', IOS)
pr3=Product('S24',Android)

filter([pr1,pr2,pr3],Android)
