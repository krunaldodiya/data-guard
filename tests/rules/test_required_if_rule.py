from data_guard.validator import Validator


class TestRequiredIfRule:
    def test_age_required_when_required_if_condition_match(self):
        data = {"name": "krunal", "age": None}

        validator = Validator(data, {"age": "required_if:name,krunal"})

        response = validator.validate()

        assert response.validated == False

        assert response.errors == {"age": ["age is required when name is krunal"]}

        assert response.data == {}

    def test_age_not_required_when_required_if_condition_dont_match(self):
        data = {"name": "test", "age": None}

        validator = Validator(data, {"age": "required_if:name,krunal"})

        response = validator.validate()

        assert response.validated == True

        assert response.errors == {}

        assert response.data == data

    def test_custom_messages(self):
        data = {"name": "krunal", "age": None}

        validator = Validator(
            data,
            {"age": "required_if:name,krunal"},
            {
                "age": "{field} is required when {required_if_key} is given as {required_if_value}"
            },
        )

        response = validator.validate()

        assert response.validated == False

        assert response.errors == {
            "age": ["age is required when name is given as krunal"]
        }

        assert response.data == {}
