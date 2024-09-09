import abc

from data_guard.rule import Rule


class BaseValidator(abc.ABC):
    @abc.abstractmethod
    def validate(self):
        raise NotImplementedError

    def validate_payload(self):
        assert isinstance(self.data, dict), "Data is not a dictionary"

        assert isinstance(self.messages, dict), "Messages is not a dictionary"

        assert isinstance(self.rules, dict), "Field rule items is not a dictionary"

        assert all(
            all(isinstance(item, (str, Rule)) for item in value)
            for value in self.rules.values()
        ), "Not all items in lists are strings or instances of Rule"
