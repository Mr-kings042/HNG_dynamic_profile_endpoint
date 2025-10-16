import os
import httpx
from datetime import datetime, timezone
from dotenv import load_dotenv
from logger import get_logger
from schema import UserProfileResponse, UserInfo

load_dotenv()
logger = get_logger(__name__)


class UserProfile:
    @staticmethod
    async def get_profile():
        """Fetch user profile and a random cat fact."""
        user_info = {
            "email": os.getenv("USER_EMAIL"),
            "name": os.getenv("USER_NAME"),
            "stack": os.getenv("USER_STACK"),
        }
        cat_url = os.getenv("CAT_FACT_URL")
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(cat_url)
                if response.status_code == 200:
                    data = response.json()
                    cat_fact = data.get("fact", "No fact found.")
                    logger.info(f"Fetched cat fact: {cat_fact}")
                else:
                    cat_fact = "Could not fetch cat fact at this time."
        except httpx.HTTPError as e:
            logger.error(f"HTTP error while fetching cat fact: {e}")
            raise Exception(f"Error fetching cat fact: {e}")
        return UserProfileResponse(
            status="success",
            user=UserInfo(**user_info),
            timestamp=datetime.now(timezone.utc).isoformat(),
            fact=cat_fact
        )
user_profile = UserProfile()