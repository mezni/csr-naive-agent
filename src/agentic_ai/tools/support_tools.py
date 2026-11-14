from typing import Any


ORDERS = {
    4821: {
        "order_id": 4821,
        "customer_id": 101,
        "status": "shipped",
    }
}

SHIPPING = {
    4821: {
        "order_id": 4821,
        "status": "delayed",
        "estimated_delivery": "2026-11-16",
    }
}


def get_order(order_id: int) -> dict[str, Any]:
    order = ORDERS.get(order_id)

    if order is None:
        return {
            "error": "Order not found",
            "order_id": order_id,
        }

    return order


def get_shipping_status(
    order_id: int,
) -> dict[str, Any]:
    shipping = SHIPPING.get(order_id)

    if shipping is None:
        return {
            "error": "Shipping information not found",
            "order_id": order_id,
        }

    return shipping
