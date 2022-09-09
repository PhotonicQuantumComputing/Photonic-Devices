import glimy

x=glimy.Continuum(2, (55,275), 100e-9)

for i in range(5):
    x.add(glimy.geo2D.Rectangle((30,8*i), (50,8*i+5),0,12))
    x.add(glimy.geo2D.Rectangle((30,8*i+5), (50,8*i+8),0,10))
    
x.add(glimy.geo2D.Rectangle((29,40),(30,0),1,123))

x.add(glimy.geo2D.Rectangle((50,40),(51,0),1,123))

x.add_energizer(glimy.DotSource((40,0), (0,1000000), 1, frequency=49965409e6))

x.view_structure(False)

glimy.Render(x,500)

x.view_field()