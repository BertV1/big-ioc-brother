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
whois_xml_api = open(r'whoisxmlapi.txt','r')
citizen_lab1 = open(r'citizens_lab.txt','r')
citizen_lab2 = open(r'citizens_lab2.txt','r')
citizen_lab3 = open(r'citizens_lab3.txt','r')


def get_doms(a_file):
    iocs_list = []
    pot_iocs = a_file.readlines()
    for pot_ioc in pot_iocs:
        pot_ioc = pot_ioc.strip()
        pot_ioc = pot_ioc.replace('[','').replace(']','')
        if ' ' not in pot_ioc and pot_ioc != '':
            iocs_list.append(pot_ioc)
        elif '.' in pot_ioc:
            pot_ioc_tuple = pot_ioc.split('\t')
            for pot_ioc_t in pot_ioc_tuple:
                if '.' in pot_ioc_t.strip() and ' ' not in pot_ioc_t.strip():
                    iocs_list.append(pot_ioc_t.strip())
    return iocs_list

# amnesty_ioc_list = get_doms(amnesty)
# meta_ioc_list = get_doms(meta)
#cl1_ioc_list = get_doms(citizen_lab1)
cl3_ioc_list = get_doms(citizen_lab3)

x=0
for ioc in cl3_ioc_list:
    if x<100:
        print(str(x)+" "+ioc)
    x+=1

# depending on which format the original list has
# function to parse them

ioc_dom_parsed = []


# recursive, and then filter out duplicates

# ioc_dom_unique = open(r'',a)


ioc_dom_unique = []
