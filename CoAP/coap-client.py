import logging
import asyncio
from re import X
import time
from aiocoap import *
import openpyxl
from openpyxl import Workbook

logging.basicConfig(level=logging.INFO)

filename = '1MB'
columns = 3
times = 100
firstRow = 'C1'
excel_file = openpyxl.load_workbook('CoAPdata/time.xlsx')
sheet = excel_file.active


async def main():
    sheet[firstRow] = filename
    for i in range(times):
        requestTime = time.time()
        context = await Context.create_client_context()
        request = Message(code=GET, uri="coap://192.168.56.1/" + filename)
        try:
            response = await context.request(request).response
        except Exception as e:
            print('Failed to fetch resource:')
            print(e)
        else:
            file = open('CoAPdata/' + filename,'w+')
            file.write('%s\n%r'%(response.code, response.payload))
            file.close()
            recieveTime = time.time()
            sheet.cell(column=columns, row=i+2).value = recieveTime - requestTime
    excel_file.save('CoAPdata/time.xlsx')

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())