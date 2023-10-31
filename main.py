from CleanApps import CleanApps
from ZenMode import zen
from CleanScs import CleanScs
# Import the curses library to control the terminal using arrows
import curses
# Import the shutil module to get the terminal size
import shutil
import os


menu_options = ["Unused Screenshots", "Unused Apps", "Zen Mode"]

# Define the functions to be executed for each menu option
menu_functions = {
    "Unused Screenshots": CleanScs,
    "Unused Apps": CleanApps,
    "Zen Mode": zen,
}


def print_stars(stdscr):
    # Get the width of the terminal
    terminal_width, _ = shutil.get_terminal_size()

    # Print '*' characters to fill the entire width of the terminal
    stars_line = '*' * terminal_width
    stdscr.addstr(0, 0, stars_line, curses.A_BOLD)


def titleBar(stdscr):
    print_stars(stdscr)

    # Get the terminal width
    terminal_width, _ = shutil.get_terminal_size()

    # Calculate the number of '*' characters for the title
    title = "Agam's Terminal"
    title_length = len(title)
    left_padding = (terminal_width - title_length) // 2
    right_padding = terminal_width - title_length - left_padding

    # Print the title with '*' padding
    title_line = '*' * left_padding + title + '*' * right_padding
    stdscr.addstr(1, 0, title_line, curses.A_BOLD)

    print_stars(stdscr)


def menu(stdscr, selected_row):
    stdscr.clear()

    titleBar(stdscr)

    # Print menu options with the selected option highlighted
    for i, option in enumerate(menu_options):
        if i == selected_row:
            stdscr.addstr(i + 3, 0, f"> {option}", curses.A_STANDOUT)
        else:
            stdscr.addstr(i + 3, 0, f"  {option}")

    stdscr.addstr(3 + len(menu_options), 0, "")
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.keypad(1)
    current_row = 0

    while True:
        menu(stdscr, current_row)
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu_options) - 1:
            current_row += 1
        elif key == 10:  # Enter key
            selected_option = menu_options[current_row]
            # Check if the selected_option is in menu_functions
            if selected_option in menu_functions:
                # Call the corresponding function
                menu_functions[selected_option]()
            os.system("clear")  # Replace with desired action
            break


if __name__ == '__main__':
    curses.wrapper(main)
