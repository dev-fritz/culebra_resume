import asyncio
import asyncpg

async def run():
    conn: asyncpg.connection = await asyncpg.connect(user='postgres', password='postgres',
                                 database='crabot', host='localhost', port=5432)
    values = await conn.fetch(
        "select 9836936379;"
    )
    print(values)
    await conn.close()

asyncio.run(run())