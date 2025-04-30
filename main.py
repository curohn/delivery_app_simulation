import random
from datetime import datetime

class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def fetch_restaurants(self):
        self.cursor.execute("SELECT restaurant_id, restaurant_name, address FROM dim_restaurants")
        rows = self.cursor.fetchall()
        return rows

    def fetch_drivers(self):
        self.cursor.execute("SELECT driver_id, driver_name, driver_address FROM dim_drivers")
        rows = self.cursor.fetchall()
        return rows

    def fetch_menu(self, restaurant_id):
        self.cursor.execute("SELECT menu_id, cost, prep_time FROM dim_menu WHERE restaurant_id = ?", (restaurant_id,))
        rows = self.cursor.fetchall()
        return rows
    
    def fetch_customers(self):
        self.cursor.execute("SELECT customer_id, customer_name, address FROM dim_customers")
        rows = self.cursor.fetchall()
        return rows
    
    def fetch_dates(self):
        self.cursor.execute("SELECT date_id, date, day_of_week FROM dim_dates")
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.conn.close()

class Dates:
    def __init__(self, date_id, date, day_of_week):
        self.date_id = date_id
        self.date = date
        self.day = date
        self.day_of_week = day_of_week

class Driver:
    def __init__(self, driver_id, name, location):
        self.driver_id = driver_id
        self.name = name
        self.location = self.parse_location(location)

    def parse_location(self, location):
        # Assuming location is stored as a string like "(x, y)"
        x, y = map(int, location.strip("()").split(","))
        return (x, y)

    def calculate_distance(self, destination):
        x = abs(self.location[0] - destination[0])
        y = abs(self.location[1] - destination[1])
        return x + y
    
class Restaurant:
    def __init__(self, restaurant_id, name, location, menu):
        self.restaurant_id = restaurant_id
        self.name = name
        self.location = self.parse_location(location)
        self.menu = menu

    def parse_location(self, location):
        x, y = map(int, location.strip("()").split(","))
        return (x, y)

class Customer:
    def __init__(self, customer_id, name, location):
        self.customer_id = customer_id
        self.name = name
        self.location = self.parse_location(location)

    def parse_location(self, location):
        x, y = map(int, location.strip("()").split(","))
        return (x, y)
    
    def assign_demand(self, demand):
        self.demand = demand
        self.orders = []

class Order:
    def __init__(self, customer_location, restaurant, driver):
        self.customer_location = customer_location
        self.restaurant = restaurant
        self.driver = driver

    def calculate_total_distance(self):
        to_restaurant = self.driver.calculate_distance(self.restaurant.location)
        to_customer = abs(self.restaurant.location[0] - self.customer_location[0]) + abs(self.restaurant.location[1] - self.customer_location[1])
        return to_restaurant + to_customer
    
# Default Values
db_path = 'delivery_app.db'
mean = 2
std_dev = 1
customer_order_demand = round(random.normalvariate(mean, std_dev))


# Simulate orders for the delivery app
def simulate_orders(db_path):
    # Initialize database connection
    db = Database(db_path)
    
    # Fetch data from the database
    restaurants_data = db.fetch_restaurants()
    drivers_data = db.fetch_drivers()
    customers_data = db.fetch_customers()
    dates_data = db.fetch_dates()

    # Create objects for restaurants, drivers, and customers
    restaurants = []
    for r in restaurants_data:
        menu = db.fetch_menu(r[0])  # Fetch menu for each restaurant
        restaurants.append(Restaurant(r[0], r[1], r[2], menu))

    drivers = [Driver(d[0], d[1], d[2]) for d in drivers_data]
    customers = [Customer(c[0], c[1], c[2]) for c in customers_data]

    # Simulate orders for each day
    for date in dates_data:
        for customer in customers:
            # Assign random daily demand to the customer
            customer_demand = round(random.normalvariate(mean, std_dev))
            customer.assign_demand(customer_demand)

            # Generate orders based on customer demand
            for _ in range(customer.demand):
                # Randomly select a restaurant and menu item
                restaurant = random.choice(restaurants)
                menu_item = random.choice(restaurant.menu)

                # Find the nearest available driver
                nearest_driver = min(drivers, key=lambda driver: driver.calculate_distance(restaurant.location))

                # Create an order
                order = Order(customer.location, restaurant, nearest_driver)

                # Calculate total distance for the order
                total_distance = order.calculate_total_distance()

                # Add the order to the database
                db.cursor.execute(
                    """
                    INSERT INTO fact_orders (customer_id, restaurant_id, driver_id, order_time, delivery_distance, item_id, cost, prep_time)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        customer.customer_id,
                        restaurant.restaurant_id,
                        menu_item[0],  # menu_id
                        nearest_driver.driver_id,
                        order_date, #
                        order_time, #
                        menu_item[2],  # prep_time 
                        1, #quantity 
                        driver_location,
                        pickup_location,
                        estimated_pick_up_time,
                        pick_up_time,
                        delivery_location,
                        estimated_delivery_time,
                        delivery_time,
                        menu_item[1],  # sub_total cost
                        tip,
                        total_cost,
                        simulation_id = datetime.now().strftime("%Y%m%d_%H%M"),
                        version = 1
                    )
                )
                db.conn.commit()

    # Close the database connection
    db.close()

 