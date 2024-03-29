from rgbprint import gradient_print, Color
import os


class Messages:
    def __init__(self):
        self.commands_list = [
            {"title": "Вывести все книги", "function": self.show_books},
            {"title": "Добавить книгу", "function": self.create_book},
            {"title": "Найти книгу", "function": self.show_book},
            {"title": "Удалить книгу", "function": self.delete_book},
            {"title": "Выйти", "function": exit}
        ]

    def print_logo(self) -> None:
        """
        Displays the logo on the screen
        """

        gradient_print("""
.______     ______     ______    __  ___ 
|   _  \   /  __  \   /  __  \  |  |/  / 
|  |_)  | |  |  |  | |  |  |  | |  '  /  
|   _  <  |  |  |  | |  |  |  | |    <   
|  |_)  | |  `--'  | |  `--'  | |  .  \  
|______/   \______/   \______/  |__|\__\                   
""", start_color="#00c6ff", end_color="#0072ff", end="\n\n")

    def open_menu(self) -> None:
        """
        Opens the menu (The data is taken from the variable self.commands_list)
        """

        self.print_logo()

        # Output all functions
        for count, value in enumerate(self.commands_list, 1):
            print(f"[{Color.red}{count}{Color.reset}] {value['title']}")

        user_resp = input("> ")

        if not user_resp.isnumeric():
            self.print_error("Вы ввели не число!")
        else:
            user_resp = int(user_resp)
            if user_resp > len(self.commands_list) or user_resp <= 0:
                self.print_error("Этот параметр не подходит!")

        # Execute the function
        self.clear_console()
        self.commands_list[user_resp - 1]['function']()

    def print_error(self, text: str, exit_: bool = True) -> None:
        """
        Displays the error on the screen

        :param text: Text message
        :param exit_: Go to the menu?
        """

        print(f"\n[{Color.red}ОШИБКА{Color.reset}] {text}")

        if exit_:
            input(f"\n{Color.orange}Нажмите ENTER что-бы вернуться в меню{Color.reset}")
            self.start()

    def print_success(self, text: str) -> None:
        """
        Display a successful message

        :param text: Text message
        """

        print(f"\n[{Color.green}УСПЕХ{Color.reset}] {text}")

    def clear_console(self) -> None:
        """
        Clears the screen
        """

        os.system("cls")
