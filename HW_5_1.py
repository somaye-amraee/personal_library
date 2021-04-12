book_shelf = []

'''
frist we creat a book class
'''
class Book:

    def __init__(self, title, author, publish_year, language, price, pages,  status=None):
        '''

        :param title: book title
        :param author: book author
        :param publish_year: book publish year
        :param language: book language
        :param price: book price
        :param pages:book pages
        :param status: status
        '''
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.language = language
        self.price = price
        self.pages = pages
        self.status = status

    '''
    we creat a read method to calculate unread pages 
    '''
    def read(self, num_read_page):
        self.unread = self.pages - num_read_page
        print(f'u read {num_read_page} more pages u have {self.unread} more pages to finish the book and status is {self.status}')

    '''
    we creat a status method to return the status of book according to read pages
    '''
    def get_status(self,num_read_page):
        if num_read_page == self.pages:
            self.status = 'finished'
        elif 0 < num_read_page < self.pages:
            self.status = 'reading'
        elif num_read_page == 0 :
            self.status = 'unread'
        else:
            print('sth went wrong enter again')


    def __str__(self):
        return f" book title: {self.title} book author : {self.author}  published year : {self.publish_year}" \
               f"  language : {self.language} price : " \
               f" {self.price}  pages: {self.pages}  "


'''
a function to get data for how many books u like to add 
'''
def get_data(num_book):

    for i in range(num_book):
        title = input(f'Enter the book {i + 1} title here:')
        author = input(f'Enter the author {title} here:')
        publish_year = int(input(f'Enter the {title} publish_year here:'))
        language = input(f'Enter the language of book {title} here :')
        price = int(input(f'Enter the price of book {title} here:'))
        pages = int(input(f'Enter pages of book {title} here:'))
        book = Book(title, author, publish_year, language, price, pages, status=None)
        book_shelf.append(book)
        print(book.__str__())


num_book = int(input('Enter the number  of books here:'))
get_data(num_book)

for item in book_shelf:
    num_read = int(input(f'Enter the read pages of book {item.title} here :'))
    item.get_status(num_read)
    item.read(num_read)
print([item.title for item in book_shelf])


