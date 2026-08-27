"""
Comprehensive sample data — adds realistic variety across every module
so you can fully test filters, sorting, and charts.

Run once with:  python seed_all_data.py
Safe to re-run — each section skips if data already exists there.
"""

from app import app
from models import (
    db, Plant, Customer, Lead, Contract, ProductionBatch,
    BusUnit, BatteryBatch, Employee
)

with app.app_context():

    # ---------------- PLANTS ----------------
    if Plant.query.count() <= 1:
        plants = [
            {"name": "NEVF Assembly Plant - Taxila", "city": "Taxila",
             "address": "Industrial Estate, Taxila Cantt", "capacity_per_month": 120,
             "lines": 2, "status": "Operational", "established_date": "2024-03-01"},
            {"name": "NEVF Battery Fitting Unit - Wah", "city": "Wah Cantt",
             "address": "Wah Industrial Zone", "capacity_per_month": 200,
             "lines": 1, "status": "Operational", "established_date": "2025-01-15"},
            {"name": "NEVF Plant 2 - Hattar", "city": "Hattar",
             "address": "Hattar Economic Zone, Phase III", "capacity_per_month": 150,
             "lines": 2, "status": "Under Construction", "established_date": "2026-05-01"},
            {"name": "NEVF Plant 3 - Faisalabad (Planned)", "city": "Faisalabad",
             "address": "Under land acquisition", "capacity_per_month": 100,
             "lines": 1, "status": "Planned", "established_date": ""},
        ]
        for p in plants:
            existing = Plant.query.filter_by(name=p["name"]).first()
            if not existing:
                db.session.add(Plant(**p))
        db.session.commit()
        print("Plants seeded.")

    plant_ids = [p.id for p in Plant.query.all()]

    # ---------------- CUSTOMERS ----------------
    if Customer.query.count() <= 2:
        customers = [
            {"name": "Punjab Mass Transit Authority", "type": "Government", "contact_person": "Procurement Desk",
             "phone": "042-99230011", "email": "procurement@pmta.gov.pk", "city": "Lahore", "status": "Active"},
            {"name": "Rawalpindi Metro Bus Authority", "type": "Government", "contact_person": "Asim Raza",
             "phone": "051-9280012", "email": "info@rmba.gov.pk", "city": "Rawalpindi", "status": "Active"},
            {"name": "Faisalabad Transport Company", "type": "Government", "contact_person": "Tariq Mehmood",
             "phone": "041-2630044", "email": "ftc@punjab.gov.pk", "city": "Faisalabad", "status": "Active"},
            {"name": "Multan Development Authority", "type": "Government", "contact_person": "Sana Yousaf",
             "phone": "061-9200110", "email": "mda@punjab.gov.pk", "city": "Multan", "status": "Inactive"},
            {"name": "Al-Noor Auto Traders", "type": "Dealer", "contact_person": "Imran Malik",
             "phone": "0300-5541122", "email": "info@alnoorauto.pk", "city": "Taxila", "status": "Active"},
            {"name": "City Wheels Motors", "type": "Dealer", "contact_person": "Farhan Sheikh",
             "phone": "0321-7789900", "email": "sales@citywheels.pk", "city": "Lahore", "status": "Active"},
            {"name": "Green Line EV Showroom", "type": "Shop", "contact_person": "Bilal Hussain",
             "phone": "0333-4456778", "email": "greenline@gmail.com", "city": "Islamabad", "status": "Active"},
            {"name": "Wah EV Sales Point", "type": "Shop", "contact_person": "Adnan Yousuf",
             "phone": "0345-2233445", "email": "wahev@gmail.com", "city": "Wah Cantt", "status": "Inactive"},
        ]
        for c in customers:
            existing = Customer.query.filter_by(name=c["name"]).first()
            if not existing:
                db.session.add(Customer(**c))
        db.session.commit()
        print("Customers seeded.")

    # ---------------- LEADS ----------------
    if Lead.query.count() <= 1:
        leads = [
            {"title": "Multan City Bus Tender", "lead_type": "Government Tender", "value": 450000000,
             "stage": "Proposal Sent", "expected_date": "2026-09-15"},
            {"title": "Sialkot Transport Authority - 50 Bus Order", "lead_type": "Government Tender",
             "value": 920000000, "stage": "Negotiation", "expected_date": "2026-10-01"},
            {"title": "Al-Noor Auto Traders - Bulk Battery Order", "lead_type": "Battery Supply",
             "value": 15000000, "stage": "Won", "expected_date": "2026-08-01"},
            {"title": "Gujranwala Dealer Inquiry - 10 Units", "lead_type": "Dealer Inquiry",
             "value": 85000000, "stage": "Contacted", "expected_date": "2026-09-30"},
            {"title": "Sargodha City Tender", "lead_type": "Government Tender", "value": 310000000,
             "stage": "New", "expected_date": "2026-11-15"},
            {"title": "Private School Fleet Inquiry", "lead_type": "Dealer Inquiry", "value": 22000000,
             "stage": "Lost", "expected_date": "2026-07-01"},
        ]
        for l in leads:
            existing = Lead.query.filter_by(title=l["title"]).first()
            if not existing:
                db.session.add(Lead(**l))
        db.session.commit()
        print("Leads seeded.")

    # ---------------- CONTRACTS ----------------
    if Contract.query.count() <= 1:
        contracts = [
            {"ref": "NEVF-PMTA-2026-001", "customer_name": "Punjab Mass Transit Authority",
             "item": "Electric Bus", "qty": 460, "value": 9200000000, "status": "In Production"},
            {"ref": "NEVF-RMBA-2026-002", "customer_name": "Rawalpindi Metro Bus Authority",
             "item": "Electric Bus", "qty": 45, "value": 900000000, "status": "Delivered"},
            {"ref": "NEVF-FTC-2026-003", "customer_name": "Faisalabad Transport Company",
             "item": "Electric Bus", "qty": 30, "value": 600000000, "status": "Confirmed"},
            {"ref": "NEVF-ANT-2026-004", "customer_name": "Al-Noor Auto Traders",
             "item": "Battery Pack", "qty": 20, "value": 30000000, "status": "Draft"},
            {"ref": "NEVF-CWM-2026-005", "customer_name": "City Wheels Motors",
             "item": "Spare Parts", "qty": 100, "value": 5000000, "status": "Delivered"},
        ]
        for c in contracts:
            existing = Contract.query.filter_by(ref=c["ref"]).first()
            if not existing:
                db.session.add(Contract(**c))
        db.session.commit()
        print("Contracts seeded.")

    # ---------------- PRODUCTION BATCHES ----------------
    if ProductionBatch.query.count() <= 1 and plant_ids:
        batches = [
            {"batch_id": "BATCH-2026-001", "model": "NEVF E-Bus 12m", "units": 460,
             "plant_id": plant_ids[0], "date": "2026-07-01", "qc_status": "Passed"},
            {"batch_id": "BATCH-2026-002", "model": "NEVF E-Bus 9m", "units": 120,
             "plant_id": plant_ids[0], "date": "2026-07-20", "qc_status": "Passed"},
            {"batch_id": "BATCH-2026-003", "model": "NEVF E-Bus 12m", "units": 85,
             "plant_id": plant_ids[min(1, len(plant_ids)-1)], "date": "2026-08-05", "qc_status": "Pending"},
            {"batch_id": "BATCH-2026-004", "model": "NEVF E-Bus 12m", "units": 40,
             "plant_id": plant_ids[0], "date": "2026-08-18", "qc_status": "Rework"},
        ]
        for b in batches:
            existing = ProductionBatch.query.filter_by(batch_id=b["batch_id"]).first()
            if not existing:
                db.session.add(ProductionBatch(**b))
        db.session.commit()
        print("Production batches seeded.")

    # ---------------- BUS UNITS ----------------
    if BusUnit.query.count() <= 1:
        buses = [
            {"unit_no": "NEVF-CH-10001", "model": "NEVF E-Bus 12m", "battery_fitted": "Yes",
             "status": "Dispatched", "location": "Rawalpindi Depot"},
            {"unit_no": "NEVF-CH-10002", "model": "NEVF E-Bus 12m", "battery_fitted": "Yes",
             "status": "Dispatched", "location": "Lahore Depot"},
            {"unit_no": "NEVF-CH-10003", "model": "NEVF E-Bus 9m", "battery_fitted": "No",
             "status": "In Stock", "location": "Taxila Plant Yard"},
            {"unit_no": "NEVF-CH-10004", "model": "NEVF E-Bus 12m", "battery_fitted": "Yes",
             "status": "Under QC", "location": "Taxila Plant Yard"},
            {"unit_no": "NEVF-CH-10005", "model": "NEVF E-Bus 12m", "battery_fitted": "No",
             "status": "In Stock", "location": "Taxila Plant Yard"},
            {"unit_no": "NEVF-CH-10006", "model": "NEVF E-Bus 9m", "battery_fitted": "Yes",
             "status": "Dispatched", "location": "Faisalabad Depot"},
        ]
        for b in buses:
            existing = BusUnit.query.filter_by(unit_no=b["unit_no"]).first()
            if not existing:
                db.session.add(BusUnit(**b))
        db.session.commit()
        print("Bus units seeded.")

    # ---------------- BATTERY BATCHES ----------------
    if BatteryBatch.query.count() <= 1:
        batteries = [
            {"batch": "BATT-2026-001", "capacity_kwh": 250, "supplier": "CATL / Local Assembler",
             "qty": 460, "status": "Fitted to Buses"},
            {"batch": "BATT-2026-002", "capacity_kwh": 250, "supplier": "CATL Battery Co.",
             "qty": 85, "status": "Available"},
            {"batch": "BATT-2026-003", "capacity_kwh": 200, "supplier": "BYD Component Supply",
             "qty": 40, "status": "Reserved"},
        ]
        for b in batteries:
            existing = BatteryBatch.query.filter_by(batch=b["batch"]).first()
            if not existing:
                db.session.add(BatteryBatch(**b))
        db.session.commit()
        print("Battery batches seeded.")

    # ---------------- MORE EMPLOYEES ----------------
    zaheer = Employee.query.filter_by(name="Sir Zaheer").first()
    if zaheer and Employee.query.count() <= 5:
        extra_employees = [
            {"name": "Kamran Sheikh", "designation": "Plant Manager", "department": "Manufacturing",
             "phone": "0300-1112233", "status": "Active", "reports_to_id": zaheer.id},
            {"name": "Nadia Aslam", "designation": "Sales Manager", "department": "Sales",
             "phone": "0311-2223344", "status": "Active", "reports_to_id": zaheer.id},
            {"name": "Waqas Iqbal", "designation": "Fleet Operations Manager", "department": "Fleet Operations",
             "phone": "0322-3334455", "status": "Active", "reports_to_id": zaheer.id},
        ]
        for e in extra_employees:
            existing = Employee.query.filter_by(name=e["name"]).first()
            if not existing:
                db.session.add(Employee(**e))
        db.session.commit()
        print("Extra employees seeded.")

    print("\nAll sample data seeding complete.")