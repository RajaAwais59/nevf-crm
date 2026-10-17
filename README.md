# NEVF CRM

**National Electric Vehicles Factory CRM**: an offline CRM and fleet management system for electric bus manufacturing operations.

## Features
- Customers, leads and contracts
- Manufacturing plants and production batches
- Bus and battery inventory
- City-wise fleet operations, daily summaries and driver violations
- Employees with reporting hierarchy
- Import shipment tracking
- Global search and Excel export for every module

## Tech Stack
Flask, SQLAlchemy, SQLite, openpyxl

## Run Locally
```bash
pip install -r requirements.txt
mkdir database
python app.py
```
Then open http://127.0.0.1:5000

Optional: set a `SECRET_KEY` environment variable for session signing.

## Data Privacy
The SQLite database and employee photos are excluded from version control.
