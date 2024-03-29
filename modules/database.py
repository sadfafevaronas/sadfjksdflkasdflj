import sqlite3


class DataBase:
    def __init__(self):
        self._con = sqlite3.connect("db.db")
        self._cur = self._con.cursor()

        self._create_table()

    def _create_table(self) -> None:
        """
        Create table if not exists
        """

        self._cur.execute("""CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            genre TEXT,
            description TEXT
        )""")

        self._con.commit()

    def get_the_last_genre(self) -> str | None:
        """
        Get the last genre from the database
        :return:
        """

        self._cur.execute("SELECT genre FROM books ORDER BY ROWID DESC LIMIT 1")
        genres = self._cur.fetchone()
        if genres:
            return genres[0]

        return None

    def find_book(self, word: str) -> list:
        """
        Find book by keyword
        """

        self._cur.execute("SELECT * FROM books WHERE name LIKE ? OR author LIKE ? OR genre LIKE "
                          "? OR description LIKE ? OR id LIKE ?", (f"%{word}%", f"%{word}%", f"%{word}%", f"%{word}%",
                                                                   f"%{word}%"))

        return self._cur.fetchall()

    def add_book(self, name: str, author: str, genre: str, description: str) -> None:
        """
        Add book to database
        """

        self._cur.execute("INSERT INTO books (name, author, genre, description) VALUES (?, ?, ?, ?)",
                          (name, author, genre, description))
        self._con.commit()

    def get_books(self) -> list:
        """
        Get all books from the database
        """

        self._cur.execute("SELECT * FROM books")
        return self._cur.fetchall()

    def del_book(self, id_) -> bool:
        """
        Delete book by ID
        """

        self._cur.execute("SELECT * FROM books WHERE id = ?", (id_, ))
        book = self._cur.fetchone()

        if not book:
            return False

        self._cur.execute("DELETE FROM books WHERE id = ?", (id_, ))
        self._con.commit()

        return True
