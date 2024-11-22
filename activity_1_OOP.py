
class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title  
        self.author = author 
        self.genre = genre  
        self.__pages = pages  # Private attribute (encapsulation)
    
    
    def get_pages(self):
        return self.__pages
    
    # Setter for the private attribute
    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            print("Invalid page count! Pages must be positive.")
    
    # A method to describe the book
    def describe(self):
        return f"'{self.title}' by {self.author}, Genre: {self.genre}, Pages: {self.__pages}"
    
    # Method to simulate reading
    def read(self, pages):
        if pages > 0:
            print(f"You read {pages} pages of '{self.title}'. Keep going!")
        else:
            print("Reading pages must be positive!")

# Subclass representing an eBook, inheriting from Book
class EBook(Book):
    def __init__(self, title, author, genre, pages, file_size):
        super().__init__(title, author, genre, pages)  # Call the parent class constructor
        self.file_size = file_size  # Additional attribute specific to EBook
    
    # Overriding the describe method to include file size
    def describe(self):
        base_description = super().describe()  # Get the base class description
        return f"{base_description}, File Size: {self.file_size}MB"
    
    # Additional method specific to eBooks
    def download(self):
        print(f"Downloading '{self.title}'... File size: {self.file_size}MB")

# Subclass representing an Audiobook, inheriting from Book
class Audiobook(Book):
    def __init__(self, title, author, genre, pages, duration):
        super().__init__(title, author, genre, pages)  # Call the parent class constructor
        self.duration = duration  # Additional attribute specific to Audiobook
    
    # Overriding the describe method to include duration
    def describe(self):
        base_description = super().describe()
        return f"{base_description}, Duration: {self.duration} hours"
    
    # Additional method specific to Audiobooks
    def play(self):
        print(f"Playing the audiobook '{self.title}'... Duration: {self.duration} hours")

# Demonstrate functionality
if __name__ == "__main__":
    # Create a general Book object
    book = Book("1984", "George Orwell", "Dystopian", 328)
    print(book.describe())
    book.read(50)
    
    # Create an EBook object
    ebook = EBook("Python Programming", "John Zelle", "Education", 450, 10)
    print(ebook.describe())
    ebook.download()
    ebook.read(100)
    
    # Create an Audiobook object
    audiobook = Audiobook("Becoming", "Michelle Obama", "Biography", 400, 19)
    print(audiobook.describe())
    audiobook.play()
