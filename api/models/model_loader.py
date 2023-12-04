from . import orders, pizzas, crusts, toppings, ratings, promotion, payment_info

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    pizzas.Base.metadata.create_all(engine)
    crusts.Base.metadata.create_all(engine)
    toppings.Base.metadata.create_all(engine)

    #
    ratings.Base.metadata.create_all(engine)
    promotion.Base.metadata.create_all(engine)
    payment_info.Base.metadata.create_all(engine)