from app import app
from models import (
    db, Settings, Plant, Customer, Lead, Contract, ProductionBatch,
    BusUnit, BatteryBatch, CityFleet, DailySummary, ViolationRecord, SystemUser
)

CITY_DATA = [
    ("Attock", 9, 2, 696, 284, 96, 13.8),
    ("Bahawalnagar", 15, 3, 1339, 515, 27, 2.0),
    ("Bahawalpur", 22, 4, 3076, 1008, 202, 6.6),
    ("Bhakar", 9, 2, 824, 325, 210, 25.5),
    ("Chakwal", 15, 3, 1558, 587, 35, 2.2),
    ("DG Khan", 24, 4, 2145, 825, 34, 1.6),
    ("Faisalabad", 30, 2, 2778, 1020, 356, 12.8),
    ("Gujjar Khan", 15, 2, 1601, 601, 37, 2.3),
    ("Hafizabad", 9, 2, 1144, 413, 283, 24.7),
    ("Jhang", 25, 3, 6014, 1936, 807, 13.4),
    ("Jhelum", 15, 3, 1957, 737, 112, 5.7),
    ("Khanewal", 9, 2, 784, 317, 60, 7.7),
    ("Khushab", 15, 3, 1144, 320, 112, 9.8),
    ("Lahore", 40, 2, 2318, 854, 166, 7.2),
    ("Mandi Bahauddin", 9, 2, 640, 263, 130, 20.3),
    ("Mianwali", 15, 3, 1378, 530, 78, 5.7),
    ("Muzaffargarh", 12, 4, 2704, 1040, 22, 0.8),
    ("Pakpattan", 15, 3, 1482, 570, 9, 0.6),
    ("Rahim Yar Khan", 18, 4, 1862, 705, 84, 4.5),
    ("Rajan Pur", 15, 3, 2758, 1044, 537, 19.5),
    ("Rawalpindi", 45, 4, 9368, 3579, 2298, 24.5),
    ("Sahiwal", 16, 4, 1407, 531, 6, 0.4),
    ("Sargodha", 33, 4, 1970, 750, 49, 2.5),
    ("TobaTek Sing", 15, 2, 1647, 455, 16, 1.0),
    ("Wazirabad", 15, 2, 1105, 424, 169, 15.3),
]

DAILY_DATA = [
    ("01 Jul", 400, 59, 3897, 0, 483, 12.4, 63, 2520),
    ("02 Jul", 460, 72, 4349, 0, 604, 13.9, 57, 2280),
    ("03 Jul", 460, 72, 4349, 0, 471, 10.8, 57, 2280),
    ("04 Jul", 460, 72, 3778, 0, 375, 9.9, 30, 1200),
    ("05 Jul", 460, 72, 3742, 0, 336, 9.0, 35, 1400),
    ("06 Jul", 460, 72, 4347, 0, 618, 14.2, 77, 3040),
    ("07 Jul", 460, 72, 4349, 0, 652, 15.0, 57, 2280),
    ("08 Jul", 460, 72, 4349, 0, 471, 10.8, 74, 2960),
    ("09 Jul", 460, 72, 4349, 4136, 402, 9.2, 65, 2600),
    ("10 Jul", 460, 72, 4349, 4072, 451, 10.4, 66, 2640),
    ("11 Jul", 460, 72, 3764, 3694, 224, 6.0, 35, 1400),
    ("12 Jul", 460, 72, 3736, 3649, 240, 6.4, 37, 1480),
    ("13 Jul", 460, 72, 4341, 4082, 608, 14.0, 0, 0),
]

VIOLATIONS_DATA = [
    ("01 Jul", 0, 53, 8, 2, 0, 63, 2520),
    ("02 Jul", 0, 44, 13, 0, 0, 57, 2280),
    ("03 Jul", 0, 51, 6, 0, 0, 57, 2280),
    ("04 Jul", 0, 28, 2, 0, 0, 30, 1200),
    ("05 Jul", 0, 34, 1, 0, 0, 35, 1400),
    ("06 Jul", 2, 61, 14, 0, 0, 77, 3040),
    ("07 Jul", 0, 50, 7, 0, 0, 57, 2280),
    ("08 Jul", 0, 63, 9, 0, 2, 74, 2960),
    ("09 Jul", 0, 57, 8, 0, 0, 65, 2600),
    ("10 Jul", 0, 54, 12, 0, 0, 66, 2640),
    ("11 Jul", 0, 27, 8, 0, 0, 35, 1400),
    ("12 Jul", 0, 30, 7, 0, 0, 37, 1480),
]


def seed():
    with app.app_context():
        db.create_all()

        if Settings.query.first() is None:
            db.session.add(Settings(company_name="NEVF", manufacturing_target=8000, currency="PKR"))

        if CityFleet.query.first() is None:
            print("Seeding City Summary (real data)...")
            for city, buses, routes, planned, matured, delayed, delay_pct in CITY_DATA:
                db.session.add(CityFleet(city=city, buses=buses, routes=routes, planned_trips=planned,
                                          matured_trips=matured, delayed_trips=delayed, delay_pct=delay_pct))

        if DailySummary.query.first() is None:
            print("Seeding Daily Summary (real data)...")
            for date, buses, routes, planned, matured, delayed, delay_pct, violations, penalty in DAILY_DATA:
                db.session.add(DailySummary(date_label=date, buses=buses, routes=routes, planned_trips=planned,
                                             matured_trips=matured, delayed_trips=delayed, delay_pct=delay_pct,
                                             violations=violations, penalty_km=penalty))

        if ViolationRecord.query.first() is None:
            print("Seeding Violations (real data)...")
            for date, smoking, calling, seatbelt, eating, uniform, total, penalty in VIOLATIONS_DATA:
                db.session.add(ViolationRecord(date_label=date, smoking=smoking, calling=calling, seatbelt=seatbelt,
                                                eating=eating, uniform=uniform, total=total, penalty_km=penalty))

        if Plant.query.first() is None:
            print("Seeding sample Plant...")
            db.session.add(Plant(name="NEVF Assembly Plant (Sample)", city="Taxila",
                                  address="Industrial Estate, Taxila Cantt", capacity_per_month=120,
                                  lines=2, status="Operational", established_date="2024-03-01",
                                  notes="Replace with your real plant details."))

        if Customer.query.first() is None:
            print("Seeding sample Customers...")
            db.session.add(Customer(name="Punjab Mass Transit Authority (Sample)", type="Government",
                                     contact_person="Procurement Desk", phone="042-99xxxxxx", city="Lahore"))
            db.session.add(Customer(name="Al-Noor Auto Traders (Sample)", type="Dealer",
                                     contact_person="Imran Malik", phone="0300-xxxxxxx", city="Taxila"))

        if Lead.query.first() is None:
            print("Seeding sample Lead...")
            db.session.add(Lead(title="Multan City Bus Tender (Sample)", lead_type="Government Tender",
                                 value=450000000, stage="Proposal Sent", expected_date="2026-09-15"))

        if Contract.query.first() is None:
            print("Seeding sample Contract...")
            db.session.add(Contract(ref="NEVF-PMTA-2026-001 (Sample)", customer_name="Punjab Mass Transit Authority",
                                     item="Electric Bus", qty=460, value=9200000000, status="In Production"))

        if ProductionBatch.query.first() is None:
            print("Seeding sample Production batch...")
            db.session.add(ProductionBatch(batch_id="BATCH-2026-001 (Sample)", model="NEVF E-Bus 12m",
                                            units=460, plant_id=1, date="2026-07-01", qc_status="Passed"))

        if BusUnit.query.first() is None:
            print("Seeding sample Bus unit...")
            db.session.add(BusUnit(unit_no="NEVF-CH-10001 (Sample)", model="NEVF E-Bus 12m",
                                    battery_fitted="Yes", status="Dispatched", location="Rawalpindi Depot"))

        if BatteryBatch.query.first() is None:
            print("Seeding sample Battery batch...")
            db.session.add(BatteryBatch(batch="BATT-2026-001 (Sample)", capacity_kwh=250,
                                         supplier="CATL / Local Assembler", qty=460, status="Fitted to Buses"))

        if SystemUser.query.first() is None:
            db.session.add(SystemUser(name="Awais Nadeem", email="owaisnad2@gmail.com", role="Owner"))

        db.session.commit()
        print("\nDone. Database ready at database/nevf.db")


if __name__ == "__main__":
    seed()