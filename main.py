from CleanScs import CleanScs
# Import the curses library to control the terminal using arrows
import curses
# Import the shutil module to get the terminal size
import shutil
import os


# Define the menu options
menu_options = ["Unused Screenshots", "Exit"]

# Define the functions to be executed for each menu option
menu_functions = {
    "Unused Screenshots": CleanScs,
    "Exit": 0
}


def print_stars(stdscr, pos=0):
    # Get the width of the terminal
    terminal_width, _ = shutil.get_terminal_size()

    # Print '*' characters to fill the entire width of the terminal
    stars_line = '*' * terminal_width
    stdscr.addstr(pos, 0, stars_line, curses.A_BOLD)


def footer(stdscr):
    print_stars(stdscr)

    # Get the terminal width
    terminal_width, _ = shutil.get_terminal_size()

    # Calculate the number of '*' characters for the title
    title = "  Buzz Terminal  "
    title_length = len(title)
    left_padding = ((terminal_width - title_length) // 2)
    right_padding = terminal_width - title_length - left_padding

    # Print the title with '*' padding
    title_line = '*' * left_padding + title + '*' * right_padding
    stdscr.addstr(1, 0, title_line, curses.A_BOLD)
    print_stars(stdscr, 2)


def titleBar(stdscr):
    print_stars(stdscr)

    # Get the terminal width
    terminal_width, _ = shutil.get_terminal_size()

    # Calculate the number of '*' characters for the title
    title = "  Buzz Terminal  "
    title_length = len(title)
    left_padding = ((terminal_width - title_length) // 2)
    right_padding = terminal_width - title_length - left_padding

    # Print the title with '*' padding
    title_line = '*' * left_padding + title + '*' * right_padding
    stdscr.addstr(1, 0, title_line, curses.A_BOLD)
    print_stars(stdscr, 2)


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
    quit = True
    while quit:
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
                if selected_option == "Exit":
                    quit = False
                    break
                else:
                    # Call the corresponding function
                    menu_functions[selected_option]()
                    curses.napms(1500)
    os.system("clear")
    stdscr.addstr(3, 0, "Thank you for using Buzz Terminal!", curses.A_BOLD)
    stdscr.refresh()  # Refresh the screen to make the message visible
    curses.napms(1500)  # Pause for a few seconds (2 seconds in this example)
    os.system("clear")


if __name__ == '__main__':
    curses.wrapper(main)
