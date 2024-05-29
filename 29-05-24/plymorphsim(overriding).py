# overriding
class Product:
    def disp(self):
        print("this is product info")
class Cal(Product):
    def disp(self):
        print("this is a calculation info")
        super().disp()
p1=Cal()
p1.disp()
    