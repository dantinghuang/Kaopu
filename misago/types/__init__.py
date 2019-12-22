from datetime import datetime
from typing import (
    Any,
    Awaitable,
    Callable,
    Dict,
    List,
    Optional,
    Protocol,
    Sequence,
    Tuple,
    Type,
    TypedDict,
    Union,
)

from pydantic import BaseModel, PydanticTypeError, PydanticValueError
from starlette.requests import Request

from ..errors import ErrorsList
from .asyncvalidator import AsyncValidator
from .category import Category
from .closethread import (
    CloseThreadAction,
    CloseThreadFilter,
    CloseThreadInput,
    CloseThreadInputAction,
    CloseThreadInputFilter,
    CloseThreadInputModel,
    CloseThreadInputModelAction,
    CloseThreadInputModelFilter,
)
from .createusertoken import (
    CreateUserTokenAction,
    CreateUserTokenFilter,
    CreateUserTokenPayloadAction,
    CreateUserTokenPayloadFilter,
)
from .editpost import (
    EditPostAction,
    EditPostFilter,
    EditPostInput,
    EditPostInputAction,
    EditPostInputFilter,
    EditPostInputModel,
    EditPostInputModelAction,
    EditPostInputModelFilter,
)
from .editthreadtitle import (
    EditThreadTitleAction,
    EditThreadTitleFilter,
    EditThreadTitleInput,
    EditThreadTitleInputAction,
    EditThreadTitleInputFilter,
    EditThreadTitleInputModel,
    EditThreadTitleInputModelAction,
    EditThreadTitleInputModelFilter,
)
from .graphqlcontext import GraphQLContext, GraphQLContextAction, GraphQLContextFilter
from .post import Post
from .postreply import (
    PostReplyAction,
    PostReplyFilter,
    PostReplyInput,
    PostReplyInputAction,
    PostReplyInputFilter,
    PostReplyInputModel,
    PostReplyInputModelAction,
    PostReplyInputModelFilter,
)
from .postthread import (
    PostThreadAction,
    PostThreadFilter,
    PostThreadInput,
    PostThreadInputAction,
    PostThreadInputFilter,
    PostThreadInputModel,
    PostThreadInputModelAction,
    PostThreadInputModelFilter,
)
from .thread import Thread
from .user import User


AuthenticateUserAction = Callable[[GraphQLContext, str, str], Awaitable[Optional[User]]]
AuthenticateUserFilter = Callable[
    [AuthenticateUserAction, GraphQLContext, str, str], Awaitable[Optional[User]]
]

CacheVersions = Dict[str, str]


class CreatePostAction(Protocol):
    async def __call__(
        self,
        thread: Thread,
        body: dict,
        *,
        poster: Optional[User] = None,
        poster_name: Optional[str] = None,
        edits: Optional[int] = 0,
        posted_at: Optional[datetime] = None,
        extra: Optional[dict] = None,
    ) -> Post:
        ...


class CreatePostFilter(Protocol):
    async def __call__(
        self,
        action: CreatePostAction,
        thread: Thread,
        body: dict,
        *,
        poster: Optional[User] = None,
        poster_name: Optional[str] = None,
        edits: Optional[int] = 0,
        posted_at: Optional[datetime] = None,
        extra: Optional[dict] = None,
    ) -> Post:
        ...


class CreateThreadAction(Protocol):
    async def __call__(
        self,
        category: Category,
        title: str,
        *,
        first_post: Optional[Post] = None,
        starter: Optional[User] = None,
        starter_name: Optional[str] = None,
        replies: int = 0,
        is_closed: bool = False,
        started_at: Optional[datetime] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> Thread:
        ...


class CreateThreadFilter(Protocol):
    async def __call__(
        self,
        action: CreateThreadAction,
        category: Category,
        title: str,
        *,
        first_post: Optional[Post] = None,
        starter: Optional[User] = None,
        starter_name: Optional[str] = None,
        replies: int = 0,
        is_closed: bool = False,
        started_at: Optional[datetime] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> Thread:
        ...


class CreateUserAction(Protocol):
    async def __call__(
        self,
        name: str,
        email: str,
        *,
        password: Optional[str] = None,
        is_moderator: bool = False,
        is_admin: bool = False,
        joined_at: Optional[datetime] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> User:
        ...


class CreateUserFilter(Protocol):
    async def __call__(
        self,
        action: CreateUserAction,
        name: str,
        email: str,
        *,
        password: Optional[str] = None,
        is_moderator: bool = False,
        is_admin: bool = False,
        joined_at: Optional[datetime] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> User:
        ...


GetAuthUserAction = Callable[[GraphQLContext, int], Awaitable[Optional[User]]]
GetAuthUserFilter = Callable[
    [GetAuthUserAction, GraphQLContext, int], Awaitable[Optional[User]]
]

GetUserFromContextAction = Callable[[GraphQLContext], Awaitable[Optional[User]]]
GetUserFromContextFilter = Callable[
    [GetUserFromContextAction, GraphQLContext], Awaitable[Optional[User]],
]

GetUserFromTokenAction = Callable[[GraphQLContext, str], Awaitable[Optional[User]]]
GetUserFromTokenFilter = Callable[
    [GetUserFromTokenAction, GraphQLContext, str], Awaitable[Optional[User]],
]

GetUserFromTokenPayloadAction = Callable[
    [GraphQLContext, Dict[str, Any]], Awaitable[Optional[User]]
]
GetUserFromTokenPayloadFilter = Callable[
    [GetUserFromTokenPayloadAction, GraphQLContext, Dict[str, Any]],
    Awaitable[Optional[User]],
]


RegisterInput = Dict[str, Any]
RegisterInputAction = Callable[
    [GraphQLContext, Dict[str, List[AsyncValidator]], RegisterInput, ErrorsList],
    Awaitable[Tuple[RegisterInput, ErrorsList]],
]
RegisterInputFilter = Callable[
    [RegisterInputAction, GraphQLContext, RegisterInput],
    Awaitable[Tuple[RegisterInput, ErrorsList]],
]

RegisterInputModel = Type[BaseModel]
RegisterInputModelAction = Callable[[GraphQLContext], Awaitable[RegisterInputModel]]
RegisterInputModelFilter = Callable[
    [RegisterInputModelAction, GraphQLContext], Awaitable[RegisterInputModel],
]

RegisterUserAction = Callable[[GraphQLContext, "RegisterInput"], Awaitable[User]]
RegisterUserFilter = Callable[
    [RegisterUserAction, GraphQLContext, "RegisterInput"], Awaitable[User]
]


class SettingImage(TypedDict):
    path: str
    width: int
    height: int


Setting = Union[bool, int, str, List[str], SettingImage]
Settings = Dict[str, Setting]

TemplateContext = Dict[str, Any]
TemplateContextAction = Callable[[Request], Awaitable[TemplateContext]]
TemplateContextFilter = Callable[
    [TemplateContextAction, Request], Awaitable[TemplateContext]
]
