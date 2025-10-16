"""
 Inventory Management System (IMS)

 Project Entry File

 This script serves as the main entry point of the IMS backend.
 It simulates how a warehouse management and order system would
 operate, including:
    - Stock adjustment
    - Order creation
    - Payment processing
    - Subscription renewal

 The architecture follows a modular layered design:
    1. Models (data definitions)
    2. Services (business logic)
    3. API (orchestration / simulated endpoints)
    4. Utils (helpers, CSV export/import, etc.)

 Author : Bingcheng Liu
 Version: v1.0 Demo Architecture Edition
"""

import sys
import os

# Ensure Python can locate the app package (for standalone execution)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from app.api.ims_api import IMSApi


def show_banner():
    """Display a startup banner for aesthetics."""
    print("\n" + "=" * 70)
    print("   🧭 Inventory Management System (IMS) — Demo Edition")
    print("=" * 70 + "\n")


def main():
    """
    Main entry point for the Inventory Management System.
    This function simulates an end-to-end business process.
    """
    show_banner()

    # Create IMS API instance (like initializing FastAPI app)
    ims = IMSApi()

    # Simulate end-to-end flow (business demo)
    try:
        ims.demo_flow()
        print("\n✅ All operations completed successfully!")
    except Exception as e:
        print("\n❌ An unexpected error occurred:", e)

    print("\nSystem shutting down...\n")

# Standard Python entrypoint guard

if __name__ == "__main__":
    main()