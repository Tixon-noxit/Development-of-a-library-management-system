from utils.FileReader import FileReader
from utils.FileWriter import FileWriter
from common.Common import FILE_NAME
from model.Model import Library
from common import Controller
from cli.CLI import CLI



def main():
    app_reader = FileReader(FILE_NAME)
    add_writer = FileWriter(FILE_NAME)
    app_library = Library(app_reader, add_writer)
    app_controller = Controller.Controller(app_library)
    app_cli = CLI(app_controller)

    app_cli.display_menu()
    app_cli.handle_choice()

if __name__ == '__main__':
    main()