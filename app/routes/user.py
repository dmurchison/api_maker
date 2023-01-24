import logging
from fastapi import APIRouter, HTTPException
from app.services.user import UserServices
from app.schemas.user import (
    CreateUserResponse,
    FullUserProfile, 
    MultipleUsersResponse
)


logger = logging.getLogger(__name__)
print(__name__)


def create_user_router() -> APIRouter:
    user_router = APIRouter(
        prefix='/user',
        tags=['user']
    )
    user_services = UserServices()


    @user_router.get('/all', response_model=MultipleUsersResponse)
    async def get_all_users_pagination(start: int = 0, limit: int = 2):
        users, total = await user_services.get_all_users_with_pagination(start, limit)
        formatted_users = MultipleUsersResponse(users=users, total=total)
        return formatted_users


    @user_router.get('/{user_id}', response_model=FullUserProfile)
    async def get_user_by_id(user_id: int):
        full_user_profile = await user_services.get_user_info(user_id)
        
        return full_user_profile


    @user_router.put('/{user_id}')
    async def update_user(user_id: int, full_profile_info: FullUserProfile):
        await user_services.create_update_user(full_profile_info, user_id)
        return None


    @user_router.delete('/{user_id}')
    async def remove_user(user_id: int):
        await user_services.delete_user(user_id)


    @user_router.post('/', response_model=CreateUserResponse)
    async def add_user(full_profile_info: FullUserProfile):
        user_id = await user_services.create_update_user(full_profile_info)
        created_user = CreateUserResponse(user_id=user_id)
        return created_user


    return user_router


