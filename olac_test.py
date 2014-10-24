from lxml import etree
import codecs

# 'http://www.language-archives.org/OLAC/1.1/static-repository.xml'
# xmlfilepath = 'sample-olac-static-repo.xml'
xmlfilepath = 'sample-olac-kaipuleohone.xml'
mprefix = 'olac'
namespaces = {'oai': 'http://www.openarchives.org/OAI/2.0/', 'olac': 'http://www.language-archives.org/OLAC/1.1/'}

print 'xmlfilepath --> ', xmlfilepath
print 'mprefix --> ', mprefix
print 'namespaces --> ', namespaces


with codecs.open(xmlfilepath, 'r', 'utf-8') as xmlfile:
    text = xmlfile.read()

xml = text.encode('ascii', 'replace')
xml = unicode(xml, 'UTF-8', 'replace')   	 
xml = xml.replace(chr(12), '?')
xml = xml.encode('UTF-8')

tree = etree.XML(xml)
evaluator = etree.XPathEvaluator(tree, namespaces=namespaces)
print 'NOTE --> tree and evaluator are defined'

# NOTE: this grabs the record elements from tree:
records = evaluator('//oai:record')
print 'NOTE --> Records listed'
# print list(records)
r = records[0]

print '---------HEADER---------\n'
h = r[0]
for e in h:
	print '%s --> %s\n\t%s\n\n'% (e.tag, e.text, e.attrib)

print '\n\n---------METADATA SINGLE---------\n'
m = r[1][0]
for e in m:
	print '%s --> %s\n\t%s\n\n'% (e.tag, e.text, e.attrib)

print '\n\n---------METADATA FULL---------\n'
for r in records:
	m = r[1][0]
	for e in m:
		print '%s --> %s\n----> %s'% (e.tag, e.text, e.attrib)




# result = []



# for record_node in records:
# 	record_evaluator = etree.XPathEvaluator(record_node, 
#                                         namespaces=namespaces)
# 	e = record_evaluator.evaluate
# 	# find header node
# 	header_node = e('oai:header')[0]
# 	# create header
# 	header = header_node
# 	# find metadata node
# 	metadata_list = e('oai:metadata')
# 	if metadata_list:
# 	    metadata = metadata_list[0]
# 	    # create metadata
# 	    # metadata = metadata_registry.readMetadata(metadata_prefix, metadata_node)
# 	else:
# 	    metadata = None
# 	# XXX TODO: about, should be third element of tuple
# 	result.append((header, metadata, None))


# etree.tostring(tree, pretty_print=True)

