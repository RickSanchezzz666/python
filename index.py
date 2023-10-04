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
    
    def getGeneratedBook(self):
        book = Book()

        book.setFormat(' ')
        book.setPage(' ')
        return book
    
class Book:
    def __init__(self):
        self.__format = None
        self.__pages = list()

    def setFormat(self, format):
        self.__format = format

    def setPage(self, page):
        self.__pages.append(page)

    def getFormat(self):
        return self.__format

    def getPages(self):
        return self.__pages

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

class Singleton:
    __instance = None
    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception('This class is a Singleton')
        else:
            Singleton.__instance = self
            self.bookDictionary = dict()

    def addBook(self, book):
        count = len(self.bookDictionary)
        self.bookDictionary[f'{book.description.name}{count}'] = book

    def getDictionary(self):
        return self.bookDictionary
    
singleton = Singleton()


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
    def generate(self):
        raise Exception("this is not book class")
class ScienceBookFactory(AbstractLibraryFactory):
    def create(self):
        book = ScienceBook('ScienceBook')
        book.usedLitList(input('Введіть список викорастної літератури: '))
        book.add_glossarium(input('Введіть глосаріум: '))
        director.setBuilder(CreateBook())
        scienceBook = director.getBook()
        fullBook = CombinedBook(book, scienceBook)
        singleton.addBook(fullBook)
        return fullBook
    def generate(self):
        bookPart1 = ScienceBook('ScienceBook')
        randomUsedList = ''
        for i in range(random.randint(0, 60)):
            randomUsedList += random.choice(wordRegister) + " "
        bookPart1.usedLitList(randomUsedList)

        randomGlossarium = ''
        for i in range(random.randint(0, 60)):
            randomGlossarium += random.choice(wordRegister) + " "
        bookPart1.add_glossarium(randomGlossarium)

        director.setBuilder(CreateBook())
        bookPart2 = director.getGeneratedBook()

        formats = ['A1', 'A2', 'A3', 'A4', 'A5']
        randomFormat = random.choice(formats)

        formatIndex = formats.index(randomFormat)

        bookPart2.setFormat(randomFormat)
        randomPages = ''
        for t in range(random.randint(0, 50)):
            for i in range(random.randint(0, (formatIndex + 1) * 50)):
                randomPages += random.choice(wordRegister) + " "
            bookPart2.setPage(randomPages)

        fullBook = CombinedBook(bookPart1, bookPart2)

        singleton.addBook(fullBook)
        return fullBook
class NovelBookFactory(AbstractLibraryFactory):
    def create(self):
        book = NovelBook('NovelBook')
        book.character_list(input('Введіть список персонажів: '))
        book.brief_description(input('Введіть короткий опис: '))
        director.setBuilder(CreateBook())
        scienceBook = director.getBook()
        fullBook = CombinedBook(book, scienceBook)
        singleton.addBook(fullBook)
        return fullBook
    def generate(self):
        bookPart1 = NovelBook('NovelBook')
        randomCharList = ''
        for i in range(random.randint(0, 60)):
            randomCharList += random.choice(wordRegister) + " "
        bookPart1.character_list(randomCharList)

        randomBriefDesc = ''
        for i in range(random.randint(0, 60)):
            randomBriefDesc += random.choice(wordRegister) + " "
        bookPart1.brief_description(randomBriefDesc)

        director.setBuilder(CreateBook())
        bookPart2 = director.getGeneratedBook()

        formats = ['A1', 'A2', 'A3', 'A4', 'A5']
        randomFormat = random.choice(formats)

        formatIndex = formats.index(randomFormat)

        bookPart2.setFormat(randomFormat)
        randomPages = ''
        for t in range(random.randint(0, 50)):
            for i in range(random.randint(0, (formatIndex + 1) * 50)):
                randomPages += random.choice(wordRegister) + " "
            bookPart2.setPage(randomPages)

        fullBook = CombinedBook(bookPart1, bookPart2)

        singleton.addBook(fullBook)
        return fullBook
class ManualBookFactory(AbstractLibraryFactory):
    def create(self):
        book = ManualBook('ManualBook')
        book.add_image(input('Введіть ссилку на картинку: '))
        director.setBuilder(CreateBook())
        scienceBook = director.getBook()
        fullBook = CombinedBook(book, scienceBook)
        singleton.addBook(fullBook)
        return fullBook
    def generate(self):
        bookPart1 = ManualBook('ManualBook')
        randomImages = ''
        for i in range(random.randint(0, 20)):
            randomImages += '<image>' + " "
        bookPart1.add_image(randomImages)

        director.setBuilder(CreateBook())
        bookPart2 = director.getGeneratedBook()

        formats = ['A1', 'A2', 'A3', 'A4', 'A5']
        randomFormat = random.choice(formats)

        formatIndex = formats.index(randomFormat)

        bookPart2.setFormat(randomFormat)
        randomPages = ''
        for t in range(random.randint(0, 50)):
            for i in range(random.randint(0, (formatIndex + 1) * 50)):
                randomPages += random.choice(wordRegister) + " "
            bookPart2.setPage(randomPages)

        fullBook = CombinedBook(bookPart1, bookPart2)

        singleton.addBook(fullBook)
        return fullBook
    
def create_book(bookFactory: AbstractLibraryFactory):
    return bookFactory.create()

    
def generate_book(bookFactory: AbstractLibraryFactory):
    return bookFactory.generate()

textToSplit = 'Але щоб ви зрозуміли, звідки виникає це хибне уявлення людей, цуратись насолоди і вихваляти страждання, я розкрию перед вами всю картину і роз’ясню, що саме говорив цей чоловік, який відкрив істину, якого я б назвав зодчим щасливого життя. Дійсно, ніхто не відкидає, не зневажає, не уникає насолод тільки через те, що це насолоди, але лише через те, що тих, хто не вміє розумно вдаватися насолоді, осягають великі страждання. Так само як немає нікого, хто полюбивши, вважав за краще і зажадав би саме страждання тільки за те, що це страждання, а не тому, що інший раз виникають такі обставини, коли страждання і біль приносять якесь і чималу насолоду. Якщо скористатися найпростішим прикладом, то хто з нас став би займатися якими б то не було тяжкими фізичними вправами, якщо б це не приносило з собою якоїсь користі? І хто міг би по справедливості дорікнути прагнення до насолоди, яке не несло б з собою ніяких неприємностей, або того, хто уникав би такого страждання, яке не приносило б з собою ніякої насолоди?'

wordRegister = textToSplit.split()

while True:
    print('\nВиберіть, що ви хочете робити:\n1. Написати книгу\n2. Переглянути бібліотеку\n3. Згенерувати рандомну книгу\n4. Завершити програму')
    choice = input('Введіть відповідь: ')
    match choice:
        case '1':
            print('\nВиберіть тип книги яку будете писати:\n1. Наукова книга\n2. Роман\n3. Посібник')
            choice = input('Введіть відповідь: ')
            book = None
            match choice:
                case '1':
                    book = create_book(ScienceBookFactory())
                    print('\nВи успішно написали Наукову книгу!')
                case '2':
                    book = create_book(NovelBookFactory())
                    print('\nВи успішно написали Роман!')
                case '3':
                    book = create_book(ManualBookFactory())
                    print('\nВи успішно написали Посібник!')
        case '2':
            dictionary = singleton.getDictionary()
            print('\n')
            for dict in dictionary:
                print(dict)
            print('\n')
            bookName = input('Введіть назву книги з якою хочете взаємодіяти: ')
            if(dictionary.get(bookName) is not None):
                while True:
                    print('\nВиберіть що ви хочете зробити:\n1. Прочитати опис книги\n2. Дізнатись формат книги\n3. Перечитати усю книгу\n4. Прочитати якусь сторінку\n5. Повернутись до головного меню')
                    choice = input('Введіть відповідь: ')
                    match choice:
                        case '1':
                            if(dictionary[bookName].description.name == 'ScienceBook'):
                                print('\nВикористана література: ' + dictionary[bookName].description.used_list + '\n\nГлосаріум: ' + dictionary[bookName].description.glossarium)
                            elif(dictionary[bookName].description.name == 'NovelBook'):
                                print('\nСписок персонажів: ' + dictionary[bookName].description.char_list + '\n\nКороткий опис: ' + dictionary[bookName].description.brief_desc)
                            elif(dictionary[bookName].description.name == 'ManualBook'):
                                print('\nКартинки: ' + dictionary[bookName].description.image)
                        case '2':
                            print('\nФормат книги: ' + dictionary[bookName].book.getFormat())
                        case '3':
                            pages = dictionary[bookName].book.getPages()
                            i = 1
                            for page in pages:
                                print(f'\n{i}: {page}')
                                i += 1
                        case '4':
                            pages = dictionary[bookName].book.getPages()
                            num_page = input('Введіть номер сторінки: ')
                            if (int(num_page) > len(pages)):
                                print('\nТакої сторінки не існує!\n')
                            else:
                                print(f'\n{num_page}: {pages[int(num_page) - 1]}')
                        case '5':
                            break
            else:
                print('\nТакої книги не знайдено!\n')   
        case '3':
            import random
            booksTypes = ['ScienceBook', 'NovelBook', 'ManualBook']
            bookChoice = random.choice(booksTypes)
            match bookChoice:
                case 'ScienceBook':
                    generate_book(ScienceBookFactory())
                    print('\nНаукову книгу успішно згенеровано!\n')
                case 'NovelBook':
                    generate_book(NovelBookFactory())
                    print('\nРоман успішно згенеровано!\n')
                case 'ManualBook':
                    generate_book(ManualBookFactory())
                    print('\nПосібник успішно згенеровано!\n')
        case '4':
            break
