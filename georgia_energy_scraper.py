from datetime import datetime, timezone
from kubra_scraper import KubraScraper
import os

class GeorgiaEnergyScraper(KubraScraper):
    owner = "Myrrolinz"
    repo = "georgia-energy-outage"
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    filepath = f"outages_data/outages_{timestamp}.json"

    instance_id = "7b38c047-7950-444b-a25c-9b3e5ab986eb"
    view_id = "67b44af5-3847-4ca3-9f4e-9190aac343d6"
    