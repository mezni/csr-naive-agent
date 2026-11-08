import random
from src.backend.database import Base, SessionLocal, engine
from src.backend.models import Customer, Product

Base.metadata.create_all(bind=engine)


def seed():
    db = SessionLocal()
    print("Seeding database...")

    # Seed Customers
    if not db.query(Customer).first():
        db.add_all(
            [
                Customer(name="Alice Smith", email="alice@example.com", tier="Gold"),
                Customer(name="Bob Jones", email="bob@example.com", tier="Silver"),
            ]
        )

    # Seed Products
    if not db.query(Product).first():
        categories = ["Voice", "Data", "Bundle", "Hardware"]
        for i in range(15):
            db.add(
                Product(
                    name=f"Plan/Device {i + 1}",
                    price=round(random.uniform(15.0, 150.0), 2),
                    category=random.choice(categories),
                )
            )

    db.commit()
    db.close()
    print("Seeding completed successfully!")


if __name__ == "__main__":
    seed()
