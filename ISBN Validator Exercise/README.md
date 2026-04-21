# Case Study: ISBN Validator Debugging

## 🎯 Project Goal
The objective was to fix a broken ISBN validator that handles both 10 and 13-digit formats. This exercise focused on identifying logic errors and implementing robust error handling.

## 🛠️ The Debugging Process
I identified and resolved several key issues:
- **Weighted Sum Logic**: Corrected the ISBN-10 weight formula using `(10 - index)`.
- **Type Conversion**: Implemented list comprehension `[int(digit) for digit in main_digits]` to safely convert string inputs.
- **Structural Fixes**: Repaired indentation errors that were causing the code to return results prematurely.

## 📚 Key Learning Points
- How to use `enumerate()` to handle index-based math.
- The importance of `try/except` blocks for user input validation.
- Understanding the difference between Modulo 10 (ISBN-13) and Modulo 11 (ISBN-10) checksums.

---
*This exercise is part of my Python Programming Fundamentals journey.*
