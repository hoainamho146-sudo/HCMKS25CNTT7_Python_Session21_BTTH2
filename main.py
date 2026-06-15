"""
CLI application for Highlands Mini POS.
"""

import logging

from pos_logic import (
    add_to_order,
    calculate_total,
    checkout,
    display_menu_items,
    display_order,
    DRINK_MENU,
    ItemNotFoundError,
    InvalidQuantityError
)


logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s - "
        "%(levelname)s - "
        "%(message)s"
    )
)


def display_main_menu():
    """Display POS menu."""
    print("\n========== HIGHLANDS MINI POS ==========")
    print("1. Xem thực đơn")
    print("2. Thêm món vào giỏ")
    print("3. Xem giỏ hàng & Tính tổng tiền")
    print("4. Thanh toán & Xóa giỏ hàng")
    print("5. Thoát ca làm việc")
    print("========================================")


def add_item_menu(order):
    """
    Handle add item process.

    Args:
        order (list): Current order.
    """
    print("\n--- THÊM MÓN VÀO GIỎ ---")

    try:
        drink_code = input(
            "Nhập mã đồ uống: "
        )

        quantity = int(
            input("Nhập số lượng: ")
        )

        add_to_order(
            order,
            drink_code,
            quantity
        )

        code = (
            drink_code.strip().upper()
        )

        print(
            f"Đã thêm {quantity} x "
            f"{DRINK_MENU[code]['name']} "
            f"vào giỏ hàng."
        )

    except ValueError:
        print(
            "Vui lòng nhập số lượng "
            "là một số nguyên!"
        )

        logging.error(
            "ValueError - "
            "Invalid quantity input"
        )

    except ItemNotFoundError as error:
        print(
            "Mã đồ uống không hợp lệ, "
            "vui lòng kiểm tra lại "
            "thực đơn!"
        )

        logging.warning(
            "ItemNotFoundError - "
            "Code: %s",
            error
        )

    except InvalidQuantityError as error:
        print(
            "Số lượng phải lớn hơn 0!"
        )

        logging.warning(
            "InvalidQuantityError - "
            "Quantity: %s",
            error
        )


def main():
    """Program entry point."""
    current_order = []

    while True:
        display_main_menu()

        choice = input(
            "Chọn chức năng (1-5): "
        )

        if choice == "1":
            display_menu_items()

        elif choice == "2":
            add_item_menu(
                current_order
            )

        elif choice == "3":
            display_order(
                current_order
            )

        elif choice == "4":
            checkout(
                current_order
            )

        elif choice == "5":
            logging.info(
                "Cashier logged out. "
                "System shutdown."
            )

            print(
                "Đã thoát ca làm việc. "
                "Hẹn gặp lại!"
            )

            break

        else:
            print(
                "Lựa chọn không hợp lệ."
            )


if __name__ == "__main__":
    main()
