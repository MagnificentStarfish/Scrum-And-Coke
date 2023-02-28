from fastapi import APIRouter, Depends, Response, HTTPException, Request, status
from typing import List, Union, Optional
from queries.users import UserIn, UserRepository, UserOut, UserOutWithoutPassword, Error, DuplicateUserError, UsersOutAll
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel

class UserForm(BaseModel):
    username: str
    password: str

class UserToken(Token):
    user: UserOut

class UserTokenWithoutPassword(Token):
    user: UserOutWithoutPassword

class HttpError(BaseModel):
    detail: str

router = APIRouter()

@router.post("/users", response_model=UserToken | HttpError)
async def create_user(
    user: UserIn,
    request: Request,
    response: Response,
    repo: UserRepository = Depends(),
):
    hashed_password = authenticator.hash_password(user.password)
    try:
        account = repo.create(user, hashed_password)
    except DuplicateUserError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    form = UserForm(
        username=user.employee_number,
        password=user.password,
       )
    token = await authenticator.login(response, request, form, repo)
    return UserToken(user=account, **token.dict())

@router.get("/users", response_model=Union[Error, UsersOutAll])
def get_all(
    repo: UserRepository = Depends(),
    ):
    # return repo.get_all()
    return {"users": repo.get_all()}


<<<<<<< HEAD

@router.put("/users/{employee_number}", response_model=Union[UserOut, Error])
def update_user(
=======
# update users not yet functional
@router.put("/users/{employee_number}")
async def update_user(
>>>>>>> bc95b70a0885d71da50191c32b31bfa8249b23f1
    employee_number: int,
    user: UserIn,
    response: Response,
    repo: UserRepository = Depends(),
<<<<<<< HEAD
) -> Union[UserOut, Error]:
    return repo.update(employee_number, user)
=======
    account_data: dict = Depends(authenticator.get_current_account_data)
):
    hashed_password = authenticator.hash_password(user.password)
    if account_data:
        return repo.update(employee_number, user, hashed_password)
    else:
        response.status_code = 404
>>>>>>> bc95b70a0885d71da50191c32b31bfa8249b23f1


@router.delete("/users/{user_id}", response_model=bool)
def delete_user(
    user_id: int,
    repo: UserRepository = Depends(),
) -> bool:
    return repo.delete(user_id)


@router.get("/users/{user_id}", response_model=Optional[Union[Error, UserOut]])
def get_one_user(
    user_id: int,
    repo: UserRepository = Depends(),
) -> UserOut:
    user = repo.get_one(user_id)
    return user

@router.get("/token", response_model=UserTokenWithoutPassword | None)
async def get_token(
    request: Request,
    user: UserOutWithoutPassword = Depends(authenticator.try_get_current_account_data)
) -> UserTokenWithoutPassword | None:
    print("THIS IS USER", user, "THIS IS REQUEST", request)
    if user and authenticator.cookie_name in request.cookies:
        return {"access_token": request.cookies[authenticator.cookie_name],
                "type": "Bearer",
                "user": user
            }
