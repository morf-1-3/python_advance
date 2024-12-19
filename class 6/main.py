import logging
import sqlite3
import os
import requests
import aiohttp
import asyncio
import time

PATH = os.path.abspath(__file__+"/..") + "/log.sqlite3"
print(PATH)
URL1 = "https://api.monobank.ua/bank/currency"
URL2 = "https://en.wikipedia.org/wiki/Main_Page"
URL3 = "https://www.chnu.edu.ua/"

db = sqlite3.Connection(PATH)
cursor = db.cursor()
def create_table():
    query = '''
    CREATE TABLE IF NOT EXISTS log(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    createat DATATIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    level VARCHAR(255) NOT NULL,
    message VARCHAR(255) NOT NULL,
    field2 VARCHAR(255)
    );
    '''
    db.execute(query)
    db.commit()


async def fetch_url(url:str):
    logger.info(f"асихр заходжу в {url} і відправляю реквест ")

    async with aiohttp.request("GET",url) as request:
        
        status_code = request.status
        text = await request.text()
        logger.info(f"асихр отримав респонс code - {status_code}  -- {url}  -")
        print(status_code)

async def async_main():
    time_start = time.time()
    # await fetch_url(URL1)
    # await fetch_url(URL2)
    # await fetch_url(URL3)
    await asyncio.gather(fetch_url(URL1),fetch_url(URL2),fetch_url(URL3))
    print(f"Time async {time.time()-time_start}")


def sync_main():
    time_start = time.time()
    logger.info(f"сихр заходжу в {URL1} і відправляю реквест ")
    response = requests.request("GET",URL1)
    logger.info(f"сихр отримав респонс {response.status_code} --------  {URL1}  ")

    logger.info(f"сихр заходжу в {URL2} і відправляю реквест ")
    response = requests.request("GET",URL2)
    logger.info(f"сихр отримав респонс {response.status_code}------   {URL2}  ")

    logger.info(f"сихр заходжу в {URL2} і відправляю реквест ")
    response = requests.request("GET",URL2)
    logger.info(f"сихр отримав респонс {response.status_code} ----- {URL2}  ")

    
    print(f"Time sync {time.time()-time_start}")


class SqliteHandler(logging.Handler):
    def __init__(self,path_bd:str, level = 0):
        super().__init__(level)
        self.path = path_bd


    def emit(self, record):
        log_entry = self.format(record)
        
        db = sqlite3.connect(PATH)
        db.execute('''
          INSERT INTO log(
                   level,message) 
                   VALUES (?,?)  
        ''',(record.levelname,log_entry))
        db.commit()
        db.close()

logger = logging.getLogger("SqliteHandler")
logger.setLevel(logging.DEBUG)

db_handler = SqliteHandler(PATH)
formatter = logging.Formatter(' %(message)s')
db_handler.setFormatter(formatter)

logger.addHandler(db_handler)

# logger.debug("Це DEBUG повідомлення.")
create_table()
sync_main()
asyncio.run(async_main())




