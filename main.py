from modules import DataBase, Messages
from rgbprint import Color


class Book(DataBase, Messages):
    def __init__(self):
        super().__init__()
        Messages.__init__(self)

    def show_books(self) -> None:
        """
        Show all books
        """

        self.print_logo()

        books = self.get_books()

        if not books:
            self.print_error("Книги не найдены!")
            return

        for count, value in enumerate(books, 1):
            print(f"[{Color.red}{value[0]}{Color.reset}] {value[1]}")

    def delete_book(self) -> None:
        """
        Delete book by id
        """

        self.print_logo()

        id_ = input("Введите ID книги\n> ")

        if not id_.isnumeric():
            self.print_error("ID должен быть числом!")
            return

        if not self.del_book(id_):
            self.print_error("Книга не найдена!")
            return

        self.print_success("Книга успешно удалена!")

    def create_book(self) -> None:
        """
        Add book to database
        """

        self.print_logo()

        name = input("Введите название книги\n> ")
        author = input("Введите автора книги\n> ")

        last_genre = self.get_the_last_genre()
        if not last_genre:
            genre = input(f"Введите жанр книги\n> ")

        else:
            genre = input(f"Введите жанр книги ( либо нажмите Enter что-бы использовать последний введенный жанр: "
                          f"{last_genre} )\n> ")

        if genre == "":
            genre = last_genre

        description = input("Введите описание книги\n> ")

        if not name or not author or not genre or not description:
            self.print_error("Вы не заполнили все поля!")
            return

        self.add_book(name, author, genre, description)

        self.print_success("Книга успешно добавлена!")

    def show_book(self) -> None:
        """
        Show book by keyword, or id
        """

        self.print_logo()

        word = input("Введите ключевое слово или ID книги\n> ")

        books = self.find_book(word)

        if not books:
            self.print_error("Книги не найдены!")
            return

        for count, value in enumerate(books, 1):
            print(f"[{Color.red}{value[0]}{Color.reset}] {value[1]} {value[2]} {value[3]} {value[4]}")

    def start(self) -> None:
        """
        Start program
        """

        while True:
            self.clear_console()
            self.open_menu()
            input(f"\n{Color.orange}Нажмите пробел что-бы вернуться в меню{Color.reset}")


if __name__ == '__main__':
    book = Book()
    book.start()
