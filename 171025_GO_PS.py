#!/usr/bin/env python3

import sys
import pronto

#go_genes = sys.argv[1]
#my_go_id = sys.argv[2]

ont = pronto.ont('/Users/admin/problemset/PFB2017_repository/go.owl')


term_obj = ont['REF:GO:0004691']
term_name = term_obj.name
print (term_name)
#print ("These genes have all been annotated with", my_go_id +',"' + term_name + '"or any of its child terms')

#all_children=
