from data_guard.validator import Validator


def main():
    data = {"name": "krunal", "terms": "yes"}

    validator = Validator(
        data,
        {"terms": ["accepted_if:name,krunal"]},
    )

    response = validator.validate()

    if response.validated:
        print(response.data)
    else:
        print(response.errors)


if __name__ == "__main__":
    main()
