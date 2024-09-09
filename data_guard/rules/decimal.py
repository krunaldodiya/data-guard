from data_guard.rule import Rule


class Decimal(Rule):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def validate(self) -> bool:
        self.require_params_count(0)

        value = self.params.get("value")

        return isinstance(value, float)

    def get_message(self) -> str:
        return "{field} must be a decimal value."
