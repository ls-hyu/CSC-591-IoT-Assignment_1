import aiocoap.resource as resource
import aiocoap
import threading
import logging
import asyncio
 
#logging.basicConfig(level=logging.INFO)
#logging.getLogger("coap-server").setLevel(logging.DEBUG)
with open('100B', 'rb') as f_read:
    hundredB = f_read.read()
    f_read.close()    

with open('10KB', 'rb') as f_read:
    tenKB = f_read.read()
    f_read.close()    

with open('1MB', 'rb') as f_read:
    oneMB = f_read.read()
    f_read.close()    

with open('10MB', 'rb') as f_read:
    tenMB = f_read.read()
    f_read.close()    

def main():
    # Resource tree creation
    root = resource.Site()
    root.add_resource(['100B'], Resource100B())
    root.add_resource(['10KB'], Resource10KB())
    root.add_resource(['1MB'], Resource1MB())
    root.add_resource(['10MB'], Resource10MB())
    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('192.168.56.1', 5683)))
    asyncio.get_event_loop().run_forever()
 
class Resource100B(resource.ObservableResource):
    def __init__(self):
        super(Resource100B, self).__init__()
        self.visible = True
        self.content = hundredB
        
    async def render_get(self, request):
        print('Return content 100B')
        payload = b'%s' % self.content
        response = aiocoap.Message(payload = payload)
        return response

class Resource10KB(resource.ObservableResource):
    def __init__(self):
        super(Resource10KB, self).__init__()
        self.visible = True
        self.content = tenKB
        
    async def render_get(self, request):
        print('Return content 10KB')
        payload = b'%s' % self.content
        response = aiocoap.Message(payload = payload)
        return response

class Resource1MB(resource.ObservableResource):
    def __init__(self):
        super(Resource1MB, self).__init__()
        self.visible = True
        self.content = oneMB
        
    async def render_get(self, request):
        print('Return content 1MB')
        payload = b'%s' % self.content
        response = aiocoap.Message(payload = payload)
        return response

class Resource10MB(resource.ObservableResource):
    def __init__(self):
        super(Resource10MB, self).__init__()
        self.visible = True
        self.content = tenMB
        
    async def render_get(self, request):
        print('Return content 10MB')
        payload = b'%s' % self.content
        response = aiocoap.Message(payload = payload)
        return response

if __name__ == "__main__":
    main()