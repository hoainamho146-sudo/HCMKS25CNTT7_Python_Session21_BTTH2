"""
Business logic for Highlands Mini POS.
"""

import logging


DRINK_MENU = {
    "P1": {
        "name": "Phin Sữa Đá",
        "price": 35000
    },
    "F1": {
        "name": "Freeze Trà Xanh",
        "price": 55000
    },
    "T1": {
        "name": "Trà Sen Vàng",
        "price": 45000
    }
}


class ItemNotFoundError(Exception):
    """Raised when drink code does not exist."""


class InvalidQuantityError(Exception):
    """Raised when quantity is invalid."""


def format_currency(amount):
    """
    Format money with comma separator.

    Args:
        amount (int): Money amount.

    Returns:
        str: Formatted currency.
    """
    return f"{amount:,}"


def display_menu_items():
    """Display drink menu."""
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")

    for code, item in DRINK_MENU.items():
        print(
            f"[{code}] - {item['name']} - "
            f"{format_currency(item['price'])} VNĐ"
        )


def add_to_order(order, drink_code, quantity):
    """
    Add item to order.

    Args:
        order (list): Current order list.
        drink_code (str): Product code.
        quantity (int): Quantity.

    Raises:
        ItemNotFoundError
        InvalidQuantityError
    """
    drink_code = drink_code.strip().upper()

    if drink_code not in DRINK_MENU:
        raise ItemNotFoundError(drink_code)

    if quantity <= 0:
        raise InvalidQuantityError(quantity)

    order.append(
        {
            "code": drink_code,
            "quantity": quantity
        }
    )

    logging.info(
        "Added %s of %s to order",
        quantity,
        drink_code
    )


def calculate_total(order):
    """
    Calculate total order amount.

    Args:
        order (list): Current order.

    Returns:
        int: Total amount.
    """
    total = 0

    for item in order:
        price = DRINK_MENU[item["code"]]["price"]

        total += price * item["quantity"]

    return total


def display_order(order):
    """
    Display current order.

    Args:
        order (list): Current order.
    """
    if not order:
        print(
            "Giỏ hàng trống, vui lòng chọn món "
            "(Chức năng 2)."
        )
        return

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print(
        "Mã SP | Tên đồ uống          | "
        "Đơn giá  | Số lượng | Thành tiền"
    )

    print("-" * 64)

    for item in order:
        code = item["code"]
        quantity = item["quantity"]

        drink = DRINK_MENU[code]

        subtotal = (
            drink["price"] * quantity
        )

        print(
            f"{code:<5} | "
            f"{drink['name']:<20} | "
            f"{format_currency(drink['price']):<8} | "
            f"{quantity:<8} | "
            f"{format_currency(subtotal)} VNĐ"
        )

    print("-" * 64)

    total = calculate_total(order)

    print(
        f"Tổng tiền cần thanh toán: "
        f"{format_currency(total)} VNĐ"
    )


def checkout(order):
    """
    Checkout current order.

    Args:
        order (list): Current order.
    """
    if not order:
        print(
            "Giỏ hàng trống, vui lòng chọn món "
            "(Chức năng 2)."
        )
        return

    total = calculate_total(order)

    print("\n--- THANH TOÁN ---")

    print(
        f"Tổng tiền cần thanh toán: "
        f"{format_currency(total)} VNĐ"
    )

    confirm = input(
        f"Xác nhận thanh toán "
        f"{format_currency(total)} VNĐ? (y/n): "
    ).strip().lower()

    if confirm == "y":
        print("Thanh toán thành công.")

        logging.info(
            "Checkout successful"
        )

        order.clear()

        print(
            "Giỏ hàng đã được làm trống."
        )

    elif confirm == "n":
        print(
            "Đã hủy thao tác thanh toán. "
            "Quay lại menu chính."
        )

    else:
        print(
            "Lựa chọn không hợp lệ. "
            "Thanh toán đã bị hủy."
        )
