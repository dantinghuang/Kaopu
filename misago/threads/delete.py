from asyncio import gather
from typing import Sequence, cast

from sqlalchemy import and_, desc, func, not_, select

from ..database import database
from ..database.queries import delete, delete_many
from ..tables import posts as posts_table, threads as threads_table
from ..types import Post, Thread
from .update import update_thread


async def delete_thread(thread: Thread):
    await delete(threads_table, thread.id)


async def delete_threads(threads: Sequence[Thread]):
    await delete_many(threads_table, [i.id for i in threads])


async def delete_thread_post(thread: Thread, post: Post) -> Thread:
    return await delete_thread_posts(thread, [post])


async def delete_thread_posts(thread: Thread, posts: Sequence[Post]) -> Thread:
    posts_ids = [i.id for i in posts]
    posts_count_query = (
        select([func.count()])
        .select_from(posts_table)
        .where(
            and_(
                posts_table.c.thread_id == thread.id,
                not_(posts_table.c.id.in_(posts_ids)),
            )
        )
    )
    last_reply_query = (
        posts_table.select(None)
        .where(
            and_(
                posts_table.c.thread_id == thread.id,
                not_(posts_table.c.id.in_(posts_ids)),
            )
        )
        .order_by(desc(posts_table.c.id))
        .limit(1)
    )
    posts_count, last_post = await gather(
        database.fetch_val(posts_count_query), database.fetch_one(last_reply_query),
    )

    updated_thread = await update_thread(
        thread,
        replies=posts_count - 1,  # first post doesnt count to replies,
        last_post=Post(**cast(dict, last_post)),
    )

    await delete_many(posts_table, posts_ids)

    return updated_thread