from data_guard.libs.rule_creator import RuleCreator


def main():
    creator = RuleCreator(directory_name="data_guard/rules")

    creator.create()


if __name__ == "__main__":
    main()
