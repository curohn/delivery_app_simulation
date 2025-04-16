# Delivery App Simulation
The goal of this project is to demonstrate my skills in database design, while teaching myself to simulate data. For this project I'll design a database for my delivery app, create synthetic data with a python script, run analysis on top of it using streamlit, and answer hard questions about the business model.

I'd like to also relate it to the real world by researching actual delivery apps, their pricing models, and make an educated guess on the simulation parameters I'd need to compare them.


## Project Design:
SQL
- Local instance of SQLite
- Will need data structure, and database design
- Make sure normalized

Order Simulation Script
- Simulate different kinds of surges
- Introduce randomness 

Driver simulation Script
- Delivery driver availability?

Data
- Python script to generate synthetic data elements
- order_id, customer_id, resturaunt_id, order_time, delivery_distance, cost, delivery_fee, tip, surge_mult, final_price, delivery_type, etc. 

Vizulization 
- Streamlit
- Distributions, cahrts

Analysis:
- Answer hard questions: expensive times, how much does express cost vs time to deliver, surge pricing effect on consumer, and business, impact of different values in simulated data


## Project Notes

### Locations, Distances, and Travel Time
We are going to be simulating orders in this project. We will have orders populate in random restaurants, from random customers, and assign a driver to those orders. But how do we deal with travel time calculations? Lets keep it simple, and assume our simulated world exists on a two dimentional grid system from 0,0 to 100,100. Each resturaunt, customer, and drivers home can be assigned a random coordinate for their location. 

Now what do we do about drivers? In the real world, a drivers location is always changing, they could be home, at a customers delivery address, at a resteruant, or at a location in between. For the first iteration of this project we are going to simplify that, and have our drivers either be home, a restaurant, or a customers address. No where in between. This will allow us to keep track of our drivers and allocate orders based on available drivers who are closest to the next order. 

Distances will be calculated based on the absolute value differences in corrdinates. For the first iteration, we will assume drivers can only move on the x and y axis, and not diagonally. 
If a driver is located at 5,5 and a restaurant is located at 52,60 then the distance will be:
5 - 52 = -47 = |47|
5 - 60 = -55 = |55|
47 + 55 = **103**

If a driver is located at 72,12, and the destination is at 87,54 the distance will be:
72 - 87 = -15 = |15|
12 - 54 = -42 = |42|
15 + 42 = **57**

Travel time will be 1/2 of the distance in minutes, with a minumum of 1 minute. 

### Open Hours
For the first iteration of this project restaurant will open at 8am, and close at 8pm. Drivers will work those same hours.

### Order Flow
An order will be generated from a customer. 
- Customers can order during open hours of restaurant
- Customers will have a random demand value (0.25-2x daily) assigned each day that will dictate how often they will order that day. 
The order will be assigned to a restaurant. 
- The nearest restaurant with that item will be selected
- The item will have an assigned prep time. 
A driver will be assigned to that order.
- The nearest available driver to that restaurant will be assigned to that order
  - Drivers are available when:
    - Not delivering another order
    - During work hours (8am-8pm)
- Driver will then 'drive' to that restaurant, and pick up order
The driver will deliver that order.
- Driver will drive to customers location to deliver. 
- Driver will then wait at that location until chosen for another order.


## Database Design
`dim_dates` is a helper table to handle dates, day/month/year calculations, as well as determining if dates are holidays or weekends. These fields will be used to add variance to our order simulation script

`dim_customers` Will contain all customers. Customers will be assigned a random address (0,0) - (100,100). They will also be assigned random phone numbers, emails, and names.

`dim_restaurants` Will contain all restaurants, their randomly assinged cordinate address, items they have on their menu (A-Z), each items cost, and a random "prep_time" value to simulate how long it would take to make that item. Restaurants will be assumed to be able to cook multiple items in parallel, so we will just need the MAX(prep_time) for each order. 

`dim_drivers` Will contain drivers, their assigned coordinate address, and some generated names, emails, and phone numbers. 

`fact_orders` Will be our transaction table. It will be populated by the simulation script.

Shit I'm gonna need more tables. 

So I'm thinking a queue:
order drops into queue 
- order time, complete time

restaurant transaction
- restaurant id, drop to restaurant time, prep time, complete time
- can only work one order at a time
- each order takes max(prep_time) of all items on order

Driver transaction
- driver id, pickup time, dropoff time, pickup location, dropoff location
- I'll need to know somehow if a driver is available, and their location

orchestrator
- picks closest, available driver for an order