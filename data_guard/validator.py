from typing import Any, Dict, List
from data_guard.base_validator import BaseValidator
from data_guard.rule import Rule
from data_guard.rules_mapper import RulesMapper
from data_guard.validation_response import ValidationResponse


class Validator(BaseValidator):
    def __init__(
        self,
        data: Dict[str, Any],
        rules: Dict[str, List[str | Rule]],
        messages: Dict[str, Any] | None = None,
    ):
        self.data = data

        self.rules = rules

        self.messages = messages or {}

        self.validate_payload()

        self.__validation_response = ValidationResponse(self.data)

        self.__rules_mapper = RulesMapper()

        self.__rules_mapper.set_rules(self.rules, self.data)

    @property
    def rules_mapper(self) -> RulesMapper:
        return self.__rules_mapper

    def validate(self) -> ValidationResponse:
        try:
            for field, rules in self.rules_mapper.rules.items():
                for rule_item, rule_executor in rules.items():
                    validatable = rule_executor.is_validatable(field, rule_item)

                    if validatable:
                        should_process_next = self.__process_validation(
                            rule_item, rule_executor, self.messages, self.data
                        )

                        if not should_process_next:
                            break

            return self.__validation_response.execute()
        except Exception as e:
            raise Exception(str(e))

    def __process_validation(
        self,
        rule_item: str,
        rule_executor: Rule,
        messages: Dict[str, Any],
        data: Dict[str, Any],
    ):
        validated = rule_executor.validate()

        if not validated:
            formatted_message = rule_executor.get_formatted_message(
                rule_item, messages, data
            )

            self.__validation_response.set_error(
                rule_executor.params.get("field"), formatted_message
            )

            if rule_item in self.__rules_mapper.implicit_rules:
                return False

        return True

    def get_params(self, field_name: str, rule_name: str) -> Dict[str, Any]:
        params = {}

        for field, rules in self.rules_mapper.rules.items():
            for rule, executor in rules.items():
                if field == field_name and rule == rule_name:
                    params = executor.params

        return params
