from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
DATABASE_DIR = PROJECT_ROOT / "database"
REPORTS_DIR = PROJECT_ROOT / "reports"

CUSTOMERS_FILE = RAW_DIR / "customers.csv"
PRODUCTS_FILE = RAW_DIR / "products.csv"
ORDERS_FILE = RAW_DIR / "orders.csv"

DATABASE_FILE = PROCESSED_DIR / "sales.db"
QUALITY_REPORT_FILE = REPORTS_DIR / "data_quality_report.json"
SCHEMA_FILE = DATABASE_DIR / "schema.sql"


def create_directories() -> None:
    """Create project directories when they do not exist."""
    for directory in (
        RAW_DIR,
        PROCESSED_DIR,
        DATABASE_DIR,
        REPORTS_DIR,
    ):
        directory.mkdir(parents=True, exist_ok=True)