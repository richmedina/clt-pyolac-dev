from olac import OLACClient
from lxml import etree


xmlfile =  'http://scholarspace.manoa.hawaii.edu/Kaipuleohone.xml'  #  'sample-olac-static-repo.xml' 'sample-olac-kaipuleohone.xml'



client = OLACClient(xmlfile)
x = client.identify()
# r = client.list_records()
# records = client.list_records()
# for i in records:
#     client.tostring(i)

