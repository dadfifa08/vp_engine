from utils.logger import setup_logger

logger = setup_logger(\"itinerary\")

class ItineraryBuilder:
    def build_for_city(self, city: str) -> list:
        plan = [
            f\"Morning: Explore {city} fan zones\",
            f\"Lunch: Try local dishes in {city}\",
            f\"Evening: Stadium tour + match analysis\"
        ]
        logger.info(f\"Generated itinerary for {city}\")
        return plan
