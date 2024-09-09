from data_guard.rule import Rule


class Numeric(Rule):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def validate(self) -> bool:
        self.require_params_count(0)

        value = self.params.get("value")

        if isinstance(value, (int, float)):
            return True

        if isinstance(value, str):
            try:
                int(value)
                return True
            except ValueError:
                pass

            try:
                float(value)
                return True
            except ValueError:
                pass

        return False

    def get_message(self) -> str:
        return "{field} must be a numeric value."
