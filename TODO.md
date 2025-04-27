# TODO:
- [x] ERD diagram
- [x] Choose SQL (probably sqlite)
- [ ] Create database and tables
  - [x] dim_dates
  - [ ] dim_drivers
  - [ ] dim_customers
  - [ ] dim_resturaunts
  - [ ] fact_orders
  - [ ] fact_driver_location
- [ ] Identify traits of the data
  - More orders during rush (12pm and 7pm)
  - Variability in order pickup and delivery +/- 5% to start
  - x% failed orders
  - Cost should be normal distibution around lets say $10
  - tip could go up based on fast delivery
- [ ] Create order simulation script
- [ ] Create synthetic data with script
- [ ] Visualize using [streamlit]{https://streamlit.io/}

## Version 2
- [ ] Research Real World delivery apps, their business models, and pricing strategies
- [ ] Compare, using best guesses from research, different real world delivery apps
- [ ] Normalize Tables better



## Version 3
- [ ] Create driver schedule to be 4-8 hours a day, random hours distributed around 3pm
  - fact_schedule (driver_id, date, start_time, end_time)
- [ ] Create resteraunt schedule, with different types (breakfast only, lunch & dinner, all)
  - open_time, close_time
- [ ] Create driver simulation script, or fold into one data simulation script
- [ ] Cluster resturaunt coordinates, to simulate town center
- [ ] Allow drivers to move diagnally
- [ ] Create order queue, instead of populating all data at once, so data can be vizualized in real time
  - [ ] Create orchestrator to pick nearest available driver
  - [ ] Create driver transaction table, to know availability, and current location
  - [ ] Create restaurant transaction to know current queue, and estimated time for all orders