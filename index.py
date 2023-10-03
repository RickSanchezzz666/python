#-----------------------------------------------------------------------------------------
#                                     Builder
#-----------------------------------------------------------------------------------------

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder
    
    def getBook(self):
        book = Book()

        format = self.__builder.getFormat()
        book.setFormat(format)

        while True:
            page = self.__builder.getPage()
            if(page == 'quni'):
                break
            book.setPage(page)
        return book
    
class Book:
    def __init__(self):
        self.__format = None
        self.__pages = list()

    def setFormat(self, format):
        self.__format = format

    def setPage(self, page):
        self.__pages.append(page)

class Builder:
    def getFormat(self): pass
    def getPage(self): pass
    
class CreateBook(Builder):
    def getFormat(self):
        format = input('Введіть формат: ')
        return format
    
    def getPage(self):
        page = input('Пишіть: ')
        return page
    

director = Director()


#-----------------------------------------------------------------------------------------
#                                     Abstract Factory
#-----------------------------------------------------------------------------------------

class CombinedBook: 
    def __init__(self, part1, part2):
        self.description = part1
        self.book = part2

class AbstractLibrary:
    def sell(self):
        raise Exception("no books to sell")
class ScienceBook(AbstractLibrary):
    def usedLitList(self, used_list):
        self.used_list = used_list
    def add_glossarium(self, glossarium ):
        self.glossarium = glossarium
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return (f"{self.name}")
class NovelBook(AbstractLibrary):
    def character_list(self, list):
        self.char_list = list
    def brief_description(self, desc):
        self.brief_desc = desc
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return (f"{self.name}")
class ManualBook(AbstractLibrary):
    def add_image(self, image):
        self.image = image
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return (f"{self.name}")
    
class AbstractLibraryFactory:
    def create(self):
        raise Exception("this is not book class")
class ScienceBookFactory(AbstractLibraryFactory):
    def create(self):
        book = ScienceBook('Science Book')
        book.usedLitList(input('Введіть список викорастної літератури: '))
        book.add_glossarium(input('Введіть глосаріум: '))
        director.setBuilder(CreateBook())
        scienceBook = director.getBook()
        fullBook = CombinedBook(book, scienceBook)
        return fullBook
class NovelBookFactory(AbstractLibraryFactory):
    def create(self):
        book = NovelBook('Novel Book')
        book.character_list(input('Введіть список персонажів: '))
        book.brief_description(input('Введіть короткий опис: '))
        director.setBuilder(CreateBook())
        scienceBook = director.getBook()
        fullBook = CombinedBook(book, scienceBook)
        return fullBook     
class ManualBookFactory(AbstractLibraryFactory):
    def create(self):
        book = ManualBook('Manual Book')
        book.add_image(input('Введіть ссилку на картинку: '))
        director.setBuilder(CreateBook())
        scienceBook = director.getBook()
        fullBook = CombinedBook(book, scienceBook)
        return fullBook
    
def create_book(bookFactory: AbstractLibraryFactory):
    return bookFactory.create()

scienceBook = create_book(ScienceBookFactory())
