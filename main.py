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
citizen_lab2 = open(r'citizens_lab2.txt','r')
citizen_lab3 = open(r'citizens_lab3.txt','r')


def get_doms(a_file):
    iocs_list = []
    pot_iocs = a_file.readlines()
    print(pot_iocs)
    for pot_ioc in pot_iocs:
        pot_ioc = pot_ioc.strip()
        pot_ioc = pot_ioc.replace('[','').replace(']','')
        if ' ' not in pot_ioc and pot_ioc != '':
            iocs_list.append(pot_ioc)
        elif '.' in pot_ioc:
            if pot_ioc.find('.') < pot_ioc.find(' '):
                pot_ioc = pot_ioc.split('\t')[0]
                iocs_list.append(pot_ioc)
    return iocs_list

amnesty_ioc_list = get_doms(amnesty)
meta_ioc_list = get_doms(meta)
cl3_ioc_list = get_doms(citizen_lab3)

x=0
for ioc in cl3_ioc_list:
    if x<10:
        print(ioc)
    x+=1

# depending on which format the original list has
# function to parse them

ioc_dom_parsed = []


# recursive, and then filter out duplicates

# ioc_dom_unique = open(r'',a)


ioc_dom_unique = []
