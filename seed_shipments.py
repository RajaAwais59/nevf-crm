"""
One-time script to add sample shipment records (China imports).
Run once with:  python seed_shipments.py
Safe to re-run — it skips if shipments already exist.
"""

from app import app
from models import db, Shipment

SAMPLE_SHIPMENTS = [
    {
        "shipment_ref": "NEVF-SHP-2026-001",
        "origin_country": "China",
        "supplier_name": "CATL Battery Co.",
        "items_description": "Lithium battery cells (250 kWh packs)",
        "container_count": 3,
        "status": "Delivered",
        "port_of_entry": "Karachi Port",
        "expected_arrival": "2026-06-10",
        "actual_arrival": "2026-06-12",
        "value": 45000000,
    },
    {
        "shipment_ref": "NEVF-SHP-2026-002",
        "origin_country": "China",
        "supplier_name": "Yutong Bus Parts Ltd.",
        "items_description": "Motor controllers and drive axles",
        "container_count": 2,
        "status": "In Transit",
        "port_of_entry": "Karachi Port",
        "expected_arrival": "2026-09-05",
        "actual_arrival": "",
        "value": 18500000,
    },
    {
        "shipment_ref": "NEVF-SHP-2026-003",
        "origin_country": "China",
        "supplier_name": "BYD Component Supply",
        "items_description": "Electric bus chassis frames",
        "container_count": 4,
        "status": "At Port",
        "port_of_entry": "Port Qasim",
        "expected_arrival": "2026-08-20",
        "actual_arrival": "",
        "value": 62000000,
    },
    {
        "shipment_ref": "NEVF-SHP-2026-004",
        "origin_country": "China",
        "supplier_name": "CATL Battery Co.",
        "items_description": "Battery management systems (BMS units)",
        "container_count": 1,
        "status": "Customs Clearance",
        "port_of_entry": "Karachi Port",
        "expected_arrival": "2026-08-15",
        "actual_arrival": "",
        "value": 9200000,
    },
    {
        "shipment_ref": "NEVF-SHP-2026-005",
        "origin_country": "China",
        "supplier_name": "Yutong Bus Parts Ltd.",
        "items_description": "Bus interior seating and flooring kits",
        "container_count": 2,
        "status": "Ordered",
        "port_of_entry": "Karachi Port",
        "expected_arrival": "2026-10-01",
        "actual_arrival": "",
        "value": 12000000,
    },
]

with app.app_context():
    if Shipment.query.first() is None:
        for s in SAMPLE_SHIPMENTS:
            db.session.add(Shipment(**s))
        db.session.commit()
        print(f"Added {len(SAMPLE_SHIPMENTS)} sample shipments.")
    else:
        print("Shipments already exist — skipping.")