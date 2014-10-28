from OLACClient import OLACClient
from lxml import etree

xmlfile = 'sample-olac-static-repo.xml' #'sample-olac-kaipuleohone.xml'

client = OLACClient(xmlfile)
records = client.list_records()
for i in records:
    client.tostring(i)

