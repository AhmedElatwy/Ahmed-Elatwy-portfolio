# E-Commerce-Revenue-Logistics-Analysis-SQL

## Domain:
E-Commerce / Operations
## Business Problem:
The CMO of a Brazilian marketplace needed to identify revenue drivers and high-value customers, while the Operations Director required a root-cause analysis of delivery delays in remote regions.
## My Approach:
o	Built a local relational database using SQLite to query over 100k orders across 9 connected tables.

o	Executed complex Multi-Table Joins to link Products, Orders, and Customers, enabling a granular revenue analysis.

o	Solved the "Session vs. User" identity challenge by aggregating on customer_unique_id to calculate Customer Lifetime Value (LTV).

## Key Results:
o	Identified Health & Beauty as the top category, revealing an exponential growth trend (from $134 to $119k/month).

o	Pinpointed a critical logistics bottleneck in the Northern Region (Amazon Basin), where average delivery times hit ~29 days (States: RR, AP, AM).

o	Generated a verified "VIP List" of top spenders (Top Whale: R$ 13.4k) for the loyalty program.

## Tech Stack:
SQL (SQLite), Joins, Aggregations, Date Functions.

