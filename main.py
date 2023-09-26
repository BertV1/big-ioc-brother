# get list of ioc domains
# unify markup
# no duplicates

# current sources: 
# META threat report
# WHOIS XML API threat report
# Amnesty Tech TI
# citizenslab investigation


amnesty = open(r'amnesty_tech.txt','r')
meta = open(r'meta.txt','r')


def get_doms(a_file):
    iocs_list = []
    iocs = a_file.readlines()
    for ioc in iocs:
        ioc = ioc.strip()
        ioc = ioc.replace('[','').replace(']','')
        iocs_list.append(ioc)
    return iocs_list

amnesty_ioc_list = get_doms(amnesty)
meta_ioc_list = get_doms(meta)



# depending on which format the original list has
# function to parse them

ioc_dom_parsed = []


# recursive, and then filter out duplicates

# ioc_dom_unique = open(r'',a)


ioc_dom_unique = []
