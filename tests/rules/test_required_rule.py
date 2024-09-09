from data_guard.validator import Validator


class TestRequiredRule:
    def test_fails_when_age_null(self):
        data = {"age": None}

        validator = Validator(data, {"age": "required"})

        response = validator.validate()

        assert response.validated == False

        assert response.errors == {"age": ["age is required"]}

        assert response.data == {}

    def test_custom_messages(self):
        data = {"age": None}

        validator = Validator(
            data,
            {"age": "required"},
            {"age.required": "The field ({field}) is required."},
        )

        response = validator.validate()

        assert response.validated == False

        assert response.errors == {"age": ["The field (age) is required."]}

        assert response.data == {}

    def test_passes_when_age_is_given(self):
        data = {"age": 15}

        validator = Validator(data, {"age": "required"})

        response = validator.validate()

        assert response.validated == True

        assert response.errors == {}

        assert response.data == data
