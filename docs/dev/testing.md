
# Testing Overview

The Trading Strategy Tester project places a strong emphasis on code quality and reliability. Comprehensive testing has been conducted to ensure that the system behaves as expected across a wide range of scenarios.

---

## Test Coverage

- **Total Unit Tests**: Approximately **600**
- **Lines of Code Covered**: **86%**

This extensive test suite covers the core logic, including:
- Trade execution and management
- Strategy validation and evaluation
- Indicator calculations and TradingSeries implementations
  - Indicator values are tested against TradingView values available on the website.
- Performance metrics calculations
- Training data generation for LLMs
- Input validation modules

---

## Notes on Coverage

While an 86% coverage rate demonstrates a high level of confidence in the system's correctness, achieving 100% coverage is not practical or necessary for this project. Some areas intentionally remain uncovered, particularly:

- **Visualization modules**: Functions related to plotting and graphical representation are harder to unit test due to their reliance on external libraries and graphical outputs.

---

## How to Run Tests

To run the tests, use the following command from the root directory of the project:

```bash
python -m unittest discover -s tests
  ```

It will automatically discover and execute all test cases in the `tests` directory. You can also use your IDE to run the tests. In this case it is important to set a default testing framework to `unittest`.

## Conclusion

The testing strategy balances thoroughness with practicality, ensuring that the critical business logic is rigorously tested while recognizing that some visual and auxiliary components are better validated through manual inspection or integration testing.

Thanks to this strong testing foundation, the Trading Strategy Tester is robust, maintainable, and ready for extension and real-world usage.
