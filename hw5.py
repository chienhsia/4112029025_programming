#父類別 Purchaseable, 用於購買書籍
class Purchaseable:
    def purchase(self, quantity, price_per_unit):
            total_cost = quantity* price_per_unit
            return total_cost
#父類別 Spendable, 用於計算消費金額     
class Spendable:
    def calculate_total_spent(self, purchases):
            total_spent= sum(purchases)
            return total_spent
#父類別 Discountable, 用於計算折扣後價格
class Discountable:
    def apply_discount(self, price, discount_percentage):
            if total_cost>=money:
                discounted_price = price*(1-discount_percentage/100)
                return discounted_price
            else:
                return total_cost
#Book 類別同時繼承自  Purchaseable、 Spendable和 Discountable父類別     
class Book(Purchaseable, Spendable, Discountable):
    def __init__(self, isbn, title, author, date, price, stock):
            self.isbn = isbn
            self.title = title
            self.author = author
            self.date = date
            self.price = price
            self.stock = stock
    def display_info(self):
        return f"Title: {self.title}, ISBN:{self.isbn}, Author: {self.author}, Publication_date:{self.date}, Price: ${self.price}, Stock: {self.stock}"
    def new_display_info(self):
        return f"Title: {self.title}, ISBN:{self.isbn}, Author: {self.author}, Publication_date:{self.date}, Price: ${self.price}, Purchase_quantity: {purchase_quantity_input}"
#店家
books=[]
query=int(input("請輸入欲新增的書籍數:"))
for i in range(query):
    isbn=int(input("請輸入書籍的 ISBN:"))
    title=input("請輸入書籍的標題:")
    author=input("請輸入書籍的作者:")
    date=input("請輸入出版日期:")
    price=int(input("請輸入書籍的價錢:"))
    stock=int(input("請輸入庫存數量:"))
    book=Book(isbn,title,author,date,price,stock)
    books.append(book)
money=int(input("請輸入當滿多少元時會有回饋:"))
discount_percentage=int(input("當滿額時會有幾 %回饋:"))
print("書籍資訊:")
for book in books:
    print(book.display_info())
print(f"當滿{money}元時，可以有{discount_percentage}%回饋")
#買家
quantity=int(input("請輸入購買的書籍總數:"))
if quantity<2:
    print("購買數量不足，請再多購買幾本")
else:
    shopping_list=[]
    purchase_quantity=0
    total_cost = 0
    book_found = False
    for i in range(quantity):
        book_name=input("請輸入購買書籍的標題:")
        purchase_quantity_input=int(input("請輸入購買的數量:"))
        for book in books:
            if book_name==book.title and purchase_quantity_input<=book.stock:
                book_found = True
                book.stock-=purchase_quantity_input
                item=Book(book.isbn,book_name,book.author,book.date,book.price,purchase_quantity_input)
                shopping_list.append(item)
                unit_price = book.price
                purchase_quantity += purchase_quantity_input
                total_cost += book.purchase(purchase_quantity_input, unit_price)
                if purchase_quantity==quantity:
                    total_cost = book.purchase(purchase_quantity_input, unit_price)
                    purchases = [total_cost]
                    total_spent = book.calculate_total_spent(purchases)
                    discounted_price = book.apply_discount(book.price, discount_percentage)
                    print("購買成功")
                    print("書籍資訊:")
                    for item in shopping_list:
                        print(item.new_display_info())
                    print(f"總消費金額: ${total_spent}.")
                    print(f"\n折扣後價格: ${discounted_price}.")
                    print(f"更新後庫存:{book.stock}")
                    break
                else:
                    continue
    if not book_found:
        print("書籍不存在")
if "庫存不足" not in [message for message in shopping_list]:
    print("庫存不足")

        