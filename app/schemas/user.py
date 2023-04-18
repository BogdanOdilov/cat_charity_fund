from fastapi_users import models


class UserCreate(models.BaseUserCreate):
    '''Cхема для регистрации пользователя; в неё обязательно
    должны быть переданы email и password.
    '''
    pass


class UserUpdate(models.BaseUserUpdate):
    '''Cхема для обновления объекта пользователя; содержит все базовые поля модели
    (в том числе и пароль). Все поля опциональны.
    '''
    pass



