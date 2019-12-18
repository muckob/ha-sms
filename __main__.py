class Test:
    def __init__(self):
        self._instance = None

#    async def load(self):
#        self._instance = EdgeOS(None, "", "", "", True, ["eth0"], ["device"], "M",
#                                SCAN_INTERVAL, True)

#    async def refresh(self):
#        while True:
#            await self._instance.refresh_data()
#
#            time.sleep(20)


if __name__ == "__main__":
    t = Test()
#    loop.run_until_complete(t.load())
#    loop.run_until_complete(t.refresh())





