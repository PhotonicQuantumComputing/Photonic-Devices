#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:53:33 2022

@author: ali
"""

import glimy

x=glimy.Continuum(2, (120,125), 100e-9)

for i in range(5):
    x.add(glimy.geo2D.Rectangle((92,8*i), (120,8*i+5),0,12))
    x.add(glimy.geo2D.Rectangle((92,8*i+5),(120,8*i+8),0,10))
    
x.add(glimy.geo2D.Rectangle((91,40),(92,0),1,233))

#x.add(glimy.geo2D.Rectangle((60,40),(61,0),1,233))

x.add(glimy.geo2D.Rectangle((92,40), (120,125),0,25))

x.add(glimy.geo2D.Circle((50,80),42,5,25))
x.add(glimy.geo2D.Circle((50,80),32,3,100))
x.add(glimy.geo2D.Circle((50,80),27,2,1))


x.add_energizer(glimy.DotSource((100,0), (0,1000000), 1, frequency=49965409e6))

x.view_structure(False)

glimy.Render(x,2800);x.view_field()