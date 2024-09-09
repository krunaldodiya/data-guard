from data_guard.validator import Validator


class TestNullableRule:
    def test_passes_when_age_null(self):
        data = {"age": None}

        validator = Validator(data, {"age": "nullable"})

        response = validator.validate()

        assert response.validated == True

        assert response.errors == {}

        assert response.data == data

    def test_passes_when_age_given(self):
        data = {"age": 15}

        validator = Validator(data, {"age": "nullable"})

        response = validator.validate()

        assert response.validated == True

        assert response.errors == {}

        assert response.data == data
