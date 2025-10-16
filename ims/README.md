Inventory & Order Management System (IMS)

A lightweight modular inventory and order management system built with Python.
Designed to demonstrate system architecture, design patterns, and backend logic.

⸻

Features

Inventory Management
	•	Add, adjust, and check stock levels.
	•	Warn when stock levels are low.
	•	Support product variants and quantity tracking.

Order System
	•	Create and manage customer orders.
	•	Automatically deduct stock after purchase.
	•	Calculate total price and manage order status.

Payment System
	•	Simulate payment processing between customer and merchant.
	•	Support multiple payment methods (e.g., cash, WeChat, Alipay).
	•	Handle refunds and payment records.

Subscription System
	•	Manage merchant subscriptions (monthly / yearly).
	•	Automatically compute expiration dates.
	•	Check and renew active subscriptions.

⸻

System Architecture

IMS/
├── main.py                        # Entry point for system demonstration
└── app/
    ├── api/
    │   └── ims_api.py             # High-level API controller
    ├── core/
    │   └── config.py              # Configuration management
    ├── models/                    # Data models layer
    │   ├── product.py
    │   ├── inventory.py
    │   ├── order.py
    │   ├── subscription.py
    │   └── tenant.py
    ├── services/                  # Core business logic
    │   ├── inventory_service.py
    │   ├── order_service.py
    │   ├── payment_service.py
    │   └── subscription_service.py
    └── utils/
        └── csv_utils.py           # CSV export utilities

Layered Design
	•	Models – Define data entities.
	•	Services – Implement business logic (e.g., order handling, payment processing).
	•	API – Acts as controller layer for interactions.
	•	Utils – Contain helper utilities like CSV export.
	•	Main.py – Entry point demonstrating the entire workflow.

⸻

⚙️ How to Run

1️⃣ Clone the repository

git clone https://github.com/<yourname>/inventory-system.git
cd inventory-system

2️⃣ Run the main demo

python main.py

3️⃣ Expected Output

======== IMS System Demonstration ========

[STEP 1] Adding stock ...
[Inventory] Variant 101 stock adjusted to 100

[STEP 2] Creating order ...
[OrderService] Created <Order id=1, tenant=1, total=199.8>
[Inventory] Variant 101 stock adjusted to 98

[STEP 3] Processing payment ...
[PaymentService] Payment recorded: <Payment id=1, order=1, amount=199.8, method=cash>
[Payment Completed] Order 1 paid 199.8 USD via cash

[STEP 4] Renewing subscription ...
[SubscriptionService] Renewed: <Subscription tenant=1, plan=monthly, valid_until=2025-11-16>
[Subscription Renewed] Tenant 1 renewed monthly plan, valid until 2025-11-16

======== Demonstration Completed ========


⸻

🧪 Independent Module Testing

Each core service module can be tested separately:

Module	Test File	Command
Inventory	test_inventory_service_demo.py	python test_inventory_service_demo.py
Order	test_order_service_demo.py	python test_order_service_demo.py
Payment	test_payment_service_demo.py	python test_payment_service_demo.py
Subscription	test_subscription_service_demo.py	python test_subscription_service_demo.py


⸻

Technical Highlights
	•	Pure Python implementation with clean modular structure.
	•	Dependency Injection design for service isolation.
	•	Easily portable to Flask or FastAPI frameworks.
	•	Extensible design suitable for databases, APIs, or UI integration.

⸻

Future Extensions
	•	Web frontend (React / Vue)
	•	RESTful API using Flask or FastAPI
	•	Database layer (SQLite / PostgreSQL)
	•	User authentication and role-based permissions
	•	CSV / Excel report exports
	•	Docker container deployment
	•	Automated unit testing (pytest)

⸻

License

This project is for demonstration purposes only.
All rights reserved © 2025 Bingcheng Liu.
