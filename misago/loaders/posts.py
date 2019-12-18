from typing import Awaitable, Optional, Sequence

from ..types import GraphQLContext, Post
from ..threads.get import get_posts_by_id
from .loader import get_loader


def load_post(context: GraphQLContext, post_id: int) -> Awaitable[Optional[Post]]:
    loader = get_loader(context, "post_loader", get_posts_by_id)
    return loader.load(post_id)


def load_posts(
    context: GraphQLContext, ids: Sequence[int]
) -> Awaitable[Sequence[Optional[Post]]]:
    loader = get_loader(context, "post_loader", get_posts_by_id)
    return loader.load_many(ids)