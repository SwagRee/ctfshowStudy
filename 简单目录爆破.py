import asyncio
import aiohttp

url = 'https://b1fdb234-7f8d-4be4-bef4-58807c10eadf.challenge.ctf.show/{}/{}/'

def run_tasks(L):
    U = []
    for i in L:
        U.append(asyncio.ensure_future(i))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(U))

class TaskRunner:
    def __init__(self, n) -> None:
        self.L = []
        for i in range(n):
            self.L.append(self.task_function(i))
        self.task_num = n

    async def task_function(self, n):
        pass

    def run(self):
        run_tasks(self.L)
        self.on_over()

    def on_over(self):
        pass

class Scanner(TaskRunner):
    def __init__(self, n, a, b) -> None:
        super().__init__(n)
        self.alive = True
        self.t1 = 0
        self.t2 = 0
        self.a = a
        self.b = b
        self.res = None

    def next(self):
        t1, t2 = self.t1, self.t2
        if t2 > self.b:
            return None
        self.t1 += 1
        if self.t1 > self.a:
            self.t1 = 0
            self.t2 += 1
        return t1, t2

    async def task_function(self, n):
        while self.alive:
            v = self.next()
            if not v:
                break
            a, b = v
            r = await self.login(a, b)
            if r:
                self.res = (a, b)
                break
        self.alive = False

    async def login(self, a, b):
        u = url.format(a, b)
        async with aiohttp.ClientSession() as sess:
            try:
                async with sess.get(url=u, ssl=False) as r:
                    print(a, b, r.status)
                    return r.status == 200
            except Exception as e:
                print(e)
                return False

    async def handle_up(self, u, p):
        pass

a = Scanner(32, 100, 100)
a.run()
print(a.res)