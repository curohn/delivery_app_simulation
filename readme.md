# Delivery App Simulation
The goal of this project is to demonstrate my skills in database design, while teaching myself to simulate data. For this project I'll design a database for my delivery app, create synthetic data with a python script, run analysis on top of it using streamlit, and answer hard questions about the business model.

I'd like to also relate it to the real world by researching actual delivery apps, their pricing models, and make an educated guess on the simulation parameters I'd need to compare them.


## Project Design:
SQL
- Local instance of sql (probably sqlite, or other free option)
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

## To Do:
- [x] Create ERD for tables
- [ ] Design database
- [ ] Create order simulation script
- [ ] Create driver simulation script, or fold into one data simulation script
- [ ] Create synthetic data with script
- [ ] Visualize using [streamlit]{https://streamlit.io/}
- [ ] Research Real World delivery apps, their business models, and pricing strategies
- [ ] Compare, using best guesses from research, different real world delivery apps