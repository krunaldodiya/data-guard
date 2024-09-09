import os
import sys
import re

from colorama import Fore, init
from data_guard.libs.helpers import snake_to_pascal

init(autoreset=True)


class RuleCreator:
    def __init__(self, directory_name: str | None = None):
        self.directory_name = directory_name
        self.template_file = os.path.join(
            os.path.dirname(__file__), "rule_template.txt"
        )

    def __load_template(self):
        """Load the template from the file."""
        try:
            with open(self.template_file, "r") as file:
                return file.read()
        except FileNotFoundError:
            print(Fore.RED + f"Error: Template file '{self.template_file}' not found.")
            sys.exit(1)

    def __create_rule_file(self, file_name, force=False):
        """Creates a Python file with the specified rule template."""
        class_name = snake_to_pascal(file_name)

        try:
            template = self.__load_template()
            formatted_template = template.format(class_name=class_name)

            os.makedirs(self.directory_name, exist_ok=True)
            file_path = os.path.join(self.directory_name, f"{file_name}.py")

            if os.path.exists(file_path) and not force:
                print(
                    Fore.RED
                    + f"Error: File '{file_path}' already exists. Use --force to overwrite."
                )
                sys.exit(1)

            with open(file_path, "w") as file:
                file.write(formatted_template)

            print(Fore.GREEN + f"File '{file_path}' created successfully.")

        except Exception as e:
            print(Fore.RED + f"An error occurred: {str(e)}")
            sys.exit(1)

    def create(self):
        if len(sys.argv) < 2 or len(sys.argv) > 3:
            print(
                Fore.YELLOW
                + "Usage: python create_rule.py rule_name_in_snake_case [--force]"
            )
            sys.exit(1)

        file_name = sys.argv[1]
        force = "--force" in sys.argv

        if not re.match(r"^[a-z_][a-z0-9_]*$", file_name):
            print(
                Fore.RED
                + "Invalid file name. Please use a valid snake_case identifier."
            )
            sys.exit(1)

        self.__create_rule_file(file_name, force=force)
