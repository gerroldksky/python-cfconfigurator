#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cfconfigurator.cf import CF

api_url = "https://api.cf.stage-spa.bskyb.com"
admin_user = "gerrold.kuijpers@sky.uk"
admin_password = "Imback04!"

cf = CF(api_url)
cf.login(admin_user, admin_password)

#org = cf.search_org("DL-SCMSRe-platformingDev")
#print(org)

routes = cf.search_route("device-adder")
print(routes)

#services = cf.request('GET', "/v2/services", {"results-per-page": 1})
#print(services)

#services = cf.request('GET', "https://api.test.cf.springer-sbm.com/v2/services", {"results-per-page": 1})
#print(services)

