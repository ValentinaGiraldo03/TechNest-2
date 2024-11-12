# Coding Style Guide

## 1. Naming Conventions
- **Classes**: Class names should use `camelCase`. Example: `clientOrder`, `productReview`.
- **Functions and Methods**: Use `snake_case` for functions and methods. Example: `get_product_details()`, `calculate_total_price()`.
- **Variables**: Use `snake_case` for local variables and attributes. Example: `product_name`, `order_date`.
- **Constants**: Constants should be in uppercase, with words separated by underscores. Example: `MAX_PRODUCT_QUANTITY`.

## 2. Comments
- Use comments to describe complex code blocks, but avoid obvious comments.
- For functions, include a brief description of the purpose, parameters, and return values (if necessary).
- Example:
    ```python
    # Calculate the total price of the products in the cart
    def calculate_total(cart):
        ...
    ```

## 3. Spacing and Indentation
- Use 4 spaces per indentation level (avoid tabs).
- Ensure there is a blank line between functions and two lines between class definitions.
- Limit lines to a maximum of 80 characters if possible.


## 4. Clean Code Style
- Keep functions short; each function should have a single responsibility.
- Avoid code duplication; use reusable functions instead of repeating logic.


