from . import orders, crusts, toppings, pizzas, ratings, promotion, payment_info


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(crusts.router)
    app.include_router(toppings.router)
    app.include_router(pizzas.router)

    app.include_router(ratings.router)
    app.include_router(promotion.router)
    app.include_router(payment_info.router)