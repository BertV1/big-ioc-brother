# get list of ioc domains
# unify markup
# no duplicates

# current sources: 
# META threat report
# WHOIS XML API threat report
# Amnesty Tech TI
# citizenslab investigation

import glob

def get_doms_2(ioc_source_file):
    iocs_list = []
    with open(ioc_source_file, "r") as f:
        for pot_ioc in f:
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

ioc_sources = glob.glob("*.txt")
ioc_lists = []
for i, ioc_source in enumerate(ioc_sources):
    ioc_lists.append(get_doms_2(ioc_source))
print(len(ioc_lists))