from fastapi import APIRouter, status, HTTPException
from schema import UserProfileResponse
from services import user_profile
from logger import get_logger

logger = get_logger(__name__)

user_router = APIRouter()

@user_router.get("/", status_code=status.HTTP_200_OK, response_model=UserProfileResponse)
async def get_user_and_cat_profile():
    """Fetch user profile and a random cat fact."""
    try:
        logger.info("Fetching cat facts and user profile")
        profile = await user_profile.get_profile()
        return profile
    except Exception as e:
        logger.error(f"Error fetching user profile: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
