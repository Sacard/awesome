import orm,asyncio
from models import User,Blog,Comment

def test(loop):
    yield from orm.create_pool(loop=loop,user='root',password='s8952871',db='awesome')
    u=User(id='1',name='test3',email='test3@test.com',passwd='test3',image='about:blank3')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()