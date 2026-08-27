"""
NEVF CRM — Database Models
============================
Har business data yahan define hota hai. Ye sab local SQLite file
(database/nevf.db) mein store hoga — matlab internet ki zaroorat
nahi, aur data crash/corrupt nahi hoga (SQLite ACID-safe hai).
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# ------------------------------------------------------------------
# COMPANY / SYSTEM SETTINGS
# ------------------------------------------------------------------
class Settings(db.Model):
    __tablename__ = "settings"
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(120), default="NEVF")
    manufacturing_target = db.Column(db.Integer, default=8000)
    currency = db.Column(db.String(10), default="PKR")


# ------------------------------------------------------------------
# MANUFACTURING PLANTS (jaha buses banti hain)
# ------------------------------------------------------------------
class Plant(db.Model):
    __tablename__ = "plants"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(250))
    capacity_per_month = db.Column(db.Integer, default=0)   # kitni buses/month ban sakti hain
    lines = db.Column(db.Integer, default=1)                # assembly lines ki tadaad
    status = db.Column(db.String(30), default="Operational")  # Operational / Under Construction / Planned
    established_date = db.Column(db.String(20))
    notes = db.Column(db.Text)

    production_batches = db.relationship("ProductionBatch", backref="plant", lazy=True)


# ------------------------------------------------------------------
# SALES & CRM
# ------------------------------------------------------------------
class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    type = db.Column(db.String(30), nullable=False)   # Government / Dealer / Shop
    contact_person = db.Column(db.String(100))
    phone = db.Column(db.String(40))
    email = db.Column(db.String(100))
    city = db.Column(db.String(80))
    status = db.Column(db.String(20), default="Active")
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Lead(db.Model):
    __tablename__ = "leads"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=False)
    lead_type = db.Column(db.String(40))
    value = db.Column(db.Float, default=0)
    stage = db.Column(db.String(30), default="New")
    expected_date = db.Column(db.String(20))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Contract(db.Model):
    __tablename__ = "contracts"
    id = db.Column(db.Integer, primary_key=True)
    ref = db.Column(db.String(80), nullable=False)
    customer_name = db.Column(db.String(150))
    item = db.Column(db.String(40))          # Electric Bus / Battery Pack / Spare Parts
    qty = db.Column(db.Integer, default=0)
    value = db.Column(db.Float, default=0)
    status = db.Column(db.String(30), default="Draft")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ------------------------------------------------------------------
# PRODUCTION / MANUFACTURING
# ------------------------------------------------------------------
class ProductionBatch(db.Model):
    __tablename__ = "production_batches"
    id = db.Column(db.Integer, primary_key=True)
    batch_id = db.Column(db.String(60), nullable=False)
    model = db.Column(db.String(100))
    units = db.Column(db.Integer, default=0)
    plant_id = db.Column(db.Integer, db.ForeignKey("plants.id"))
    date = db.Column(db.String(20))
    qc_status = db.Column(db.String(20), default="Passed")


# ------------------------------------------------------------------
# INVENTORY
# ------------------------------------------------------------------
class BusUnit(db.Model):
    __tablename__ = "bus_units"
    id = db.Column(db.Integer, primary_key=True)
    unit_no = db.Column(db.String(60), nullable=False)
    model = db.Column(db.String(100))
    battery_fitted = db.Column(db.String(10), default="No")
    status = db.Column(db.String(20), default="In Stock")
    location = db.Column(db.String(120))


class BatteryBatch(db.Model):
    __tablename__ = "battery_batches"
    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.String(60), nullable=False)
    capacity_kwh = db.Column(db.Float, default=0)
    supplier = db.Column(db.String(120))
    qty = db.Column(db.Integer, default=0)
    status = db.Column(db.String(30), default="Available")


# ------------------------------------------------------------------
# FLEET OPERATIONS (tumhari Excel ka real data)
# ------------------------------------------------------------------
class CityFleet(db.Model):
    __tablename__ = "city_fleet"
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), nullable=False)
    buses = db.Column(db.Integer, default=0)
    routes = db.Column(db.Integer, default=0)
    planned_trips = db.Column(db.Integer, default=0)
    matured_trips = db.Column(db.Integer, default=0)
    delayed_trips = db.Column(db.Integer, default=0)
    delay_pct = db.Column(db.Float, default=0)


class DailySummary(db.Model):
    __tablename__ = "daily_summary"
    id = db.Column(db.Integer, primary_key=True)
    date_label = db.Column(db.String(20), nullable=False)
    buses = db.Column(db.Integer, default=0)
    routes = db.Column(db.Integer, default=0)
    planned_trips = db.Column(db.Integer, default=0)
    matured_trips = db.Column(db.Integer, default=0)
    delayed_trips = db.Column(db.Integer, default=0)
    delay_pct = db.Column(db.Float, default=0)
    violations = db.Column(db.Integer, default=0)
    penalty_km = db.Column(db.Integer, default=0)


class ViolationRecord(db.Model):
    __tablename__ = "violations"
    id = db.Column(db.Integer, primary_key=True)
    date_label = db.Column(db.String(20), nullable=False)
    smoking = db.Column(db.Integer, default=0)
    calling = db.Column(db.Integer, default=0)
    seatbelt = db.Column(db.Integer, default=0)
    eating = db.Column(db.Integer, default=0)
    uniform = db.Column(db.Integer, default=0)
    total = db.Column(db.Integer, default=0)
    penalty_km = db.Column(db.Integer, default=0)


# ------------------------------------------------------------------
# SYSTEM USERS
# ------------------------------------------------------------------
class SystemUser(db.Model):
    __tablename__ = "system_users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))
    role = db.Column(db.String(40), default="Staff")
    status = db.Column(db.String(20), default="Active")


    # ------------------------------------------------------------------
# EMPLOYEES (Company HR / Hierarchy)
# ------------------------------------------------------------------
class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    designation = db.Column(db.String(100))          # e.g. GM, PMO Officer
    department = db.Column(db.String(80))            # Management / PMO / Manufacturing / Sales / Fleet Operations
    phone = db.Column(db.String(40))
    email = db.Column(db.String(120))
    status = db.Column(db.String(20), default="Active")   # Active / On Leave / Resigned
    joining_date = db.Column(db.String(20))
    photo_filename = db.Column(db.String(200))
    plant_id = db.Column(db.Integer, db.ForeignKey("plants.id"))

    # Self-referencing field — builds the reporting hierarchy.
    # The topmost person (Brig Naeem) has reports_to_id = None.
    reports_to_id = db.Column(db.Integer, db.ForeignKey("employees.id"))

    plant = db.relationship("Plant", backref="employees", foreign_keys=[plant_id])
    manager = db.relationship("Employee", remote_side=[id], backref="direct_reports")


# ------------------------------------------------------------------
# SHIPMENTS (Imports — e.g. containers from China)
# ------------------------------------------------------------------
class Shipment(db.Model):
    __tablename__ = "shipments"
    id = db.Column(db.Integer, primary_key=True)
    shipment_ref = db.Column(db.String(80), nullable=False)
    origin_country = db.Column(db.String(80), default="China")
    supplier_name = db.Column(db.String(150))
    items_description = db.Column(db.String(250))      # e.g. "Battery cells, motor controllers"
    container_count = db.Column(db.Integer, default=1)
    status = db.Column(db.String(30), default="Ordered")  # Ordered/In Transit/At Port/Customs Clearance/Delivered
    port_of_entry = db.Column(db.String(100))          # e.g. Karachi Port
    expected_arrival = db.Column(db.String(20))
    actual_arrival = db.Column(db.String(20))
    value = db.Column(db.Float, default=0)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)