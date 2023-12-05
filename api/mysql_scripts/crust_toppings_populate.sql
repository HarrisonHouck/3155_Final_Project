DROP DATABASE IF EXISTS pizza_restaurant_api2;
CREATE DATABASE pizza_restaurant_api2;
USE pizza_restaurant_api2;

#CRUSTS
INSERT INTO crusts (name, price) 
VALUES ("Regular", 4.00);
INSERT INTO crusts (name, price) 
VALUES ("Pan", 5.00);
INSERT INTO crusts (name, price) 
VALUES ("Thin", 4.00);
INSERT INTO crusts (name, price) 
VALUES ("Stuffed", 5.00);
INSERT INTO crusts (name, price) 
VALUES ("Gluten Free", 5.00);

#TOPPINGS
INSERT INTO toppings (name, price)
VALUES ("Ham", 1.50);
INSERT INTO toppings (name, price)
VALUES ("Beef", 2.00);
INSERT INTO toppings (name, price)
VALUES ("Salami", 2.50);
INSERT INTO toppings (name, price)
VALUES ("Pepperoni", 2.00);
INSERT INTO toppings (name, price)
VALUES ("Italian Sausage", 2.00);
INSERT INTO toppings (name, price)
VALUES ("Chicken", 2.00);
INSERT INTO toppings (name, price)
VALUES ("Bacon", 2.50);
INSERT INTO toppings (name, price)
VALUES ("Peppers", 1.00);
INSERT INTO toppings (name, price)
VALUES ("Mushrooms", 1.00);
INSERT INTO toppings (name, price)
VALUES ("Spinach", 1.00);
INSERT INTO toppings (name, price)
VALUES ("Extra Cheese", 2.00);

#PROMOTIONS
INSERT INTO promotions (name, discount_rate, active, start_date, end_date)
VALUES ("49er Discount", 0.5, 1, "1968-09-23", "2099-01-01");

