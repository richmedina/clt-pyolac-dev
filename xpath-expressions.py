# XPath commands

# Identify
evaluator('//repository:repositoryName')
evaluator('//repository:baseURL')
evaluator('//olac-archive:archiveURL')
evaluator('//olac-archive:participant')
evaluator('//olac-archive:institution')
evaluator('//olac-archive:institutionURL')
evaluator('//olac-archive:shortLocation')
evaluator('//olac-archive:location')
evaluator('//olac-archive:synopsis')
evaluator('//olac-archive:access')
evaluator('//olac-archive:archivalSubmissionPolicy')
evaluator('//olac-archive:olac-archive')[0].get('currenAsOf')

# ListMetadataFormats

# ListRecords
evaluator('//')
records = evaluator('//oai:record')
# example for each record -- 
r = records[0] # a single record
record_evaluator = etree.XPathEvaluator(r, namespaces=namespaces) # create evaluator from single record
hdr = record_evaluator('./oai:header') # get the header node
meta_wrapper = record_evaluator('./oai:metadata') # not needed see next expression
meta_olac = record_evaluator('.//olac:olac') # olac metadata is nested in <olac> node so we can use the // to go direct.



# Metadata types specified by OLAC:
# olac-discourse-type
# olac-language
# olac-linguistic-field
# olac-linguistic-type
# olac-role

# Note data catagories are defined with dcterms:DCMIType



#   <participant name="Beth Tillinghast" role="ScholarSpace Project Manager" email="betht@hawaii.edu"/>
#   <participant name="Andrea Berez" role="Archive Manager" email="andrea.berez@gmail.com"/>
#   <participant name="Daniel Ishimitsu" role="Database Administrator" email="daniel20@hawaii.edu"/>
#   <institution>University of Hawaii at Manoa</institution>
# <institutionURL>http://www.hawaii.edu/</institutionURL>
#  <shortLocation>Honolulu, USA</shortLocation>
# <location>Hamilton Library, University of Hawaii at Manoa, Honolulu, Hawaii 96822, U.S.A.</location>
# <synopsis>Kaipuleohone is a digital ethnographic archive for audio and video recordings as well as photographs, notes, dictionaries, transcriptions, and other materials related to small and endangered languages. The archive was established by the Department of Linguistics at the University of Hawai'i to ensure that priceless and unique research recordings will be digitized, described and safely housed in the longterm. Kaipuleohone conforms to international archiving standards for digital archives. Audio files are stored at high resolution and the metadata conforms to the Open Language Archives Community and Dublin Core. All digital files are curated by the Library system at the University of Hawai'i's DSpace repository, ScholarSpace. Every item in the collection has access conditions specified by the depositor on the deposit form. Kaipuleohone means a 'gourd of sweet words' and we are very grateful to Laiana Wong for suggesting this name and for allowing us to use it as the name of this archive.</synopsis>
# <access>Most material is free to access by the public.  Certain documents are
#     restricted to persons associated with the University of Hawaii and are 
#     password protected.</access>
#   <archivalSubmissionPolicy>ScholarSpace at the University of Hawaii at Manoa 
#      accepts submissions of scholarly material from all members of the UH 
#      community. Submitters must first get permission from the administrators by
#      contacting us at micro@hawaii.edu
#   </archivalSubmissionPolicy>
