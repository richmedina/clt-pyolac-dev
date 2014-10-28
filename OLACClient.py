# OLACClient.py
from lxml import etree
from collections import namedtuple
import codecs, json

OlacRecord = namedtuple('OlacRecord',['header', 'metadata'])
OlacData = namedtuple('OlacData', ['text', 'attributes'])
OlacMetadataItem = namedtuple('OlacMetadataItem', ['fieldname', 'data'])

olac_dc_reader = {
    'spatial':       './/dcterms:spatial',
    'bibliographicCitation': './/dcterms:bibliographicCitation',
    'tableOfContents': './/dcterms:tableOfContents',
    'coverage': './/dc:coverage',
    'date': './/dc:date',
    'description': './/dc:description',
    'identifier': './/dc:identifier',
    'language': './/dc:language',
    'subject': './/dc:subject',
    'title': './/dc:title',
    'type:': './/dc:type',
    'contributor': './/dc:contributor'
    }

class OLACClient(object):
    """
    A loose implementation of client OAI protocol.
    Designed to parse and load an OLAC 'static repository' xml document.
    E.g., http://www.language-archives.org/OLAC/1.1/static-repository.xml
    """

    def __init__(self, xmlfilepath):
        """
        xmlfilepath: a local file or url of an OLAC stati repository.
        """
        self.root = self.build_tree_root(xmlfilepath)

    def build_tree_root(self, xmlfilepath):
        with codecs.open(xmlfilepath, 'r', 'utf-8') as xmlfile:
            text = xmlfile.read()

        xml = text.encode('ascii', 'replace')
        xml = unicode(xml, 'UTF-8', 'replace')       
        xml = xml.replace(chr(12), '?')
        xml = xml.encode('UTF-8')
        return etree.XML(xml)

    def get_namespaces(self):
        namespaces = {
            'oai': 'http://www.openarchives.org/OAI/2.0/', 
            'olac': 'http://www.language-archives.org/OLAC/1.1/',
            'dcterms': 'http://purl.org/dc/terms/',
            'dc': 'http://purl.org/dc/elements/1.1/',
            'repository': 'http://www.openarchives.org/OAI/2.0/static-repository',
            'olac-archive': 'http://www.language-archives.org/OLAC/1.1/olac-archive',
            'oai-identifier': 'http://www.openarchives.org/OAI/2.0/oai-identifier',
            'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        }
        return namespaces

    def build_header(self, element):
        hdr_evaluator = etree.XPathEvaluator(element, namespaces=self.get_namespaces())
        identifier = hdr_evaluator('.//oai:identifier')
        datestamp = hdr_evaluator('.//oai:datestamp')
        setspec = hdr_evaluator('.//oai:setSpec')
        
        header = {}
        try:
            identifier_key = self.strip_namespace_string(identifier[0].tag)
            datestamp_key = self.strip_namespace_string(datestamp[0].tag)
            # setspec_key = self.strip_namespace_string(setspec[0].tag)
            header[identifier_key] = identifier[0].text
            header[datestamp_key] = datestamp[0].text
            # header[setspec_key] = setspec[0].text
        except:
            print 'Malformed xml: Expecting values for identifier, datestamp, and setSpec in record header'

        return header

    def build_metadata(self, element):
        meta_evaluator = etree.XPathEvaluator(element, namespaces=self.get_namespaces())
        metadata = []
        for fieldname, xpath in olac_dc_reader.items():
            data = meta_evaluator(xpath)

            for i in data:
                attributes = {}

                for key, value in i.attrib.items():
                    attributes[self.strip_namespace_string(key)] = value

                item = OlacMetadataItem(fieldname, OlacData(i.text, attributes))
                metadata.append( item )
            
        return metadata

    def identify(self):
        evaluator = etree.XPathEvaluator(self.root, namespaces=self.get_namespaces())
        identify = evaluator('//repository:Identify')
        return identify

    def list_metatdata_formats(self):
        evaluator = etree.XPathEvaluator(self.root, namespaces=self.get_namespaces())
        listmetadataformats = evaluator('//repository:ListMetadataFormats')
        return listmetadataformats

    def list_records(self):
        evaluator = etree.XPathEvaluator(self.root, namespaces=self.get_namespaces())
        records = evaluator('//oai:record')
        
        record_list = []
        for record_node in records:
            record_evaluator = etree.XPathEvaluator(record_node, namespaces=self.get_namespaces()) # create evaluator from single record
            header = self.build_header(record_evaluator('./oai:header')[0]) # get the header node
            metadata = self.build_metadata(record_evaluator('.//olac:olac')[0]) # olac metadata is nested in <olac> node so we can use the // to go direct.
            record_list.append(OlacRecord(header, metadata))

        return record_list

    def tostring(self, record):
        print '\n-------HEADER-------'
        for i,j in record.header.items():
            print '%s --> %s'% (i,j)
        
        print '-------METADATA-------'
        for item in record.metadata:
            # print item
            print '%s-->%s\n -- %s'%(item.fieldname, item.data.text, json.dumps(item.data.attributes))
        
        return None

    def strip_namespace_string(self, ns_str):
        s = ns_str
        try:
            if s[0] == '{':
                ns_str = s[1:].split('}')[1]
        except:
            pass
        
        return ns_str

# metadata dictionary sample:
# {tag: (text, attrib)}


