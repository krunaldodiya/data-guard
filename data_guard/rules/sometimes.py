from data_guard.rule import Rule


class Sometimes(Rule):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def validate(self) -> bool:
        return True
