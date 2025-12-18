"""
Adapted from https://github.com/elixir-europe/rdmkit/blob/master/var/conversions.py
Adapted from https://github.com/AustralianBioCommons/human-omics-data-sharing-field-guide/blob/328e84634d10b0df51e798dbf1cc114c7cb26357/var/tools_table_conversion.py
"""

import pandas as pd
import yaml
import os
from sys import argv

# --------- Variables ---------

#google_id = "1OYx8cp4kQ7g3_Z39NDSH5325WvpZKSsjwKBiiRS9Xs8"
#gid = "0"
#url = f"https://docs.google.com/spreadsheets/d/{google_id}/export?format=csv&gid={gid}"
output_path = "_data/tool_and_resource_list.yml"
rootdir = '../pages'
#allowed_registries = ['biotools', 'fairsharing', 'tess', 'wfh-collection', 'wfh', 'doi', 'template']

# --------- Converting the table ---------

print(f"----> Converting GoogleSheets table to {output_path} started.")
resource_table = pd.read_csv(argv[1], dtype={'Title': str, 'Description': str, 'Type': str, 'URL': str, 'Tag': str})
resource_list = resource_table.to_dict("records")
clean_resource_list = []
for resource in resource_list:
    if not pd.isna(resource['Type']):
        category_list = resource['Type'].rsplit(sep=",")
    else:
        category_list = ""
#    registry_dict = {}
#    for registry in allowed_registries:
#        if not pd.isna(resource[registry]):
#            registry_dict[registry] = resource[registry]
#        del(resource[registry])
    clean_resource = {k: resource[k] for k in resource if not pd.isna(resource[k])}
    clean_resource_list.append(clean_resource)
#    clean_resource['registry'] = registry_dict
    if category_list != "":
        clean_resource['Type'] = category_list

print(os.getcwd())
with open(output_path, 'w+') as yaml_file:
    documents = yaml.dump(clean_resource_list, yaml_file)

print("----> YAML is dumped successfully")