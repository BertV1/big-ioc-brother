# get list of ioc domains
# unify markup
# no duplicates

# current sources: 
# META threat report
# WHOIS XML API threat report
# Amnesty Tech TI
# citizenslab investigation


ioc_dom_list = open(r'amnesty_tech.txt','r')


def get_doms(a_file):
    iocs = a_file.readlines()
    x=0
    for ioc in iocs:
        ioc = ioc.strip()
        if x < 10:
            print(ioc)
        x+=1
get_doms(ioc_dom_list)

# depending on which format the original list has
# function to parse them

ioc_dom_parsed = []


# recursive, and then filter out duplicates

# ioc_dom_unique = open(r'',a)


ioc_dom_unique = []
