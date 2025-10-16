"""
app/core/config.py
Basic configuration management for the IMS project.
"""

import os


class Config:
    """
    Basic configuration class for the Inventory Management System.
    In a real-world system, these would be environment variables or .env values.
    """

    PROJECT_NAME = "Intelligent Inventory Management System"
    VERSION = "1.0.0"
    ENV = os.getenv("ENV", "development")
    DEBUG = ENV == "development"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///ims_demo.db")

    # Subscription settings
    DEFAULT_PLAN = "monthly"
    PLAN_PRICES = {
        "monthly": 19.99,
        "yearly": 199.99
    }

    @staticmethod
    def show_info():
        """Display current configuration summary."""
        print(f"\n[Config] Running {Config.PROJECT_NAME} v{Config.VERSION}")
        print(f"Environment: {Config.ENV}")
        print(f"Database URL: {Config.DATABASE_URL}\n")