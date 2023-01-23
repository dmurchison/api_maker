from fastapi import APIRouter
from app.services.user import UserServices
from app.schemas.user import (
    CreateUserResponse,
    FullUserProfile, 
    MultipleUsersResponse
)



user_router = APIRouter()
user_services = UserServices()


@user_router.get('/user/me', response_model=FullUserProfile)
async def test_endpoint():
    full_user_profile = await user_services.get_user_info(user_id=0)
    return full_user_profile


@user_router.put('/user/{user_id}')
async def update_user(user_id: int, full_profile_info: FullUserProfile):
    await user_services.create_update_user(full_profile_info, user_id)
    return None


@user_router.delete('/user/{user_id}')
async def remove_user(user_id: int):
    await user_services.delete_user(user_id)


@user_router.get('/users', response_model=MultipleUsersResponse)
async def get_all_users_pagination(start: int = 0, limit: int = 2):
    users, total = await user_services.get_all_users_with_pagination(start, limit)
    formatted_users = MultipleUsersResponse(users=users, total=total)
    return formatted_users


@user_router.post('/users', response_model=CreateUserResponse)
async def add_user(full_profile_info: FullUserProfile):
    user_id = await user_services.create_update_user(full_profile_info)
    created_user = CreateUserResponse(user_id=user_id)
    return created_user





