# DataGuard

[![Documentation](https://img.shields.io/badge/docs-online-blue)](https://data-guard.gitbook.io/docs) [![PyPI](https://img.shields.io/pypi/v/data-guard)](https://pypi.org/project/data-guard/)

# Introduction

**DataGuard** is a powerful and flexible Python library designed to streamline data validation processes. Whether you're building data pipelines, developing web applications, or handling complex datasets, DataGuard offers a comprehensive suite of tools to ensure your data is clean, consistent, and reliable.

#### Key Features

- **Comprehensive Rule Set**:
  - Validate data with a wide range of built-in rules, including checks for required fields, conditional presence, format validation, and more.
  - Examples include rules for ensuring fields are present, validating email formats, checking numeric ranges, and enforcing unique constraints.
- **Custom Validators**:
  - Easily create and integrate custom validation rules tailored to your specific needs.
  - Extend the library with your own validation logic to handle any specific data requirements.
- **Chainable Validation**:
  - Build complex validation logic by chaining multiple rules together for more nuanced data integrity checks.
  - Combine rules like `Required`, `Min`, and `Email` in a single, readable chain to enforce multiple conditions on a single field.
- **Detailed Error Reporting**:
  - Generate clear, actionable error messages that help you quickly identify and resolve data issues.
  - Each validation failure is accompanied by descriptive messages indicating the nature of the error and the affected data fields.
- **Ease of Use**:
  - Designed with simplicity in mind, DataGuard's intuitive API allows you to validate data with minimal code.
  - Quickly set up validations using a declarative syntax that integrates seamlessly into your Python projects.
- **Highly Extensible**:
  - Flexible architecture that integrates seamlessly with other libraries and frameworks, making it ideal for use in a variety of projects.
  - Whether you're working with Flask, Django, or standalone scripts, DataGuard adapts to your environment.

# Installation

```bash
pip install data-guard
```

```python
from data_guard.validator import Validator

# Define the data to be validated
data = {"name": "John Doe", "email": "johndoe@example.com"}

# Define the validation rules
rules = {
    "name": ["required"],
    "email": ["required", "email"],
}

# Create a Validator instance
validator = Validator(data,rules)

# Perform the validation
response = validator.validate()

# Check if validation failed and print the errors if any
if response.validated:
    print("Validation passed!", response.data)
else:
    print("Validation failed with errors:", response.errors)
```

After installing the `DataGuard` package, providing a list of available validation rules is a great way to help users quickly understand the capabilities of the library..

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request on [GitHub](https://github.com/krunaldodiya/data-guard).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## More Information

For more information, visit the [documentation](https://data-guard.gitbook.io/docs) or view the package on [PyPI](https://pypi.org/project/data-guard).
