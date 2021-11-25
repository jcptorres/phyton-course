from io import open  as o

fichero1 = o ('archivo.txt',"w+")
fichero2 = o ('archivo1.txt', "w+")
fichero3 = o ('archivo3.txt',"w+")
fichero4 = o ('archivo4.txt',"w+")
fichero5 = o ('archivo5.txt',"w+")

fichero1.write ('Cupcake ipsum dolor sit amet. Gingerbread lollipop macaroon cookie croissant dragée. Sweet roll sesame snaps toffee marzipan powder tiramisu sugar plum marzipan. I love donut I love liquorice chocolate gummi bears tart. Apple pie sweet roll gummies pastry lollipop. Candy canes I love bear claw oat cake cookie pie topping pastry dragée. Brownie lollipop pudding I love sugar plum brownie. I love cotton candy marshmallow jelly-o cake brownie sweet roll. Jujubes jelly-o toffee chocolate carrot cake sugar plum I love gingerbread cheesecake. Tiramisu macaroon pastry liquorice I love soufflé ice cream apple pie dragée. Cookie I love I love gummi bears danish chupa chups sweet chocolate I love. Toffee toffee gummi bears bear claw croissant pie I love. Jelly croissant pastry jelly beans tart candy canes ice cream.')
fichero2.write ('Bear claw I love I love powder sweet powder. Jelly beans jujubes donut I love oat cake liquorice sweet roll wafer. Cheesecake tootsie roll soufflé sweet pudding. Soufflé marzipan chupa chups icing topping brownie. Powder I love cake pie pastry biscuit. Apple pie powder ice cream gummi bears sweet. Chocolate cake danish sesame snaps sweet pastry gummies powder muffin dragée. Lollipop pudding pastry bear claw sweet roll. I love candy canes I love chocolate marzipan. Pastry apple pie chocolate bar toffee wafer cheesecake cotton candy. Sweet roll halvah lollipop pastry jelly-o toffee gummies caramels croissant. Macaroon tart I love oat cake danish fruitcake I love caramels brownie. Shortbread cake liquorice tootsie roll lemon drops marzipan. Croissant dessert carrot cake I love sesame snaps.')
fichero3.write ('Fruitcake jujubes bear claw dragée croissant croissant candy canes I love cookie. Chocolate bar carrot cake gummi bears chocolate cake cake chocolate bar cake. Cookie bonbon fruitcake tootsie roll sugar plum halvah. Chocolate bar cheesecake brownie muffin danish muffin pudding oat cake danish. I love sweet sweet roll bear claw sweet roll pudding dragée sweet roll. Dessert chocolate bar fruitcake croissant pudding tart bear claw. Jelly beans lemon drops danish chocolate cake donut. Pie brownie candy powder dragée brownie shortbread. Topping ice cream I love cheesecake I love. Cake jelly beans soufflé oat cake cheesecake halvah. Soufflé sweet cupcake gummies soufflé apple pie powder icing. Gingerbread marshmallow topping biscuit bonbon topping jujubes cookie danish.')
fichero4.write ('Candy canes sweet roll dragée dragée chupa chups cookie biscuit bonbon. Candy tart cake apple pie cheesecake tiramisu tiramisu jelly-o pie. Sweet roll candy canes lollipop sesame snaps dessert pie pastry candy canes. Sesame snaps dragée gingerbread cupcake jelly beans candy ice cream brownie. Halvah oat cake chocolate cake cake gummi bears cupcake oat cake I love jelly. Shortbread muffin chocolate marshmallow fruitcake chocolate bar. Pie jelly jelly beans toffee shortbread pastry pie oat cake I love. Jelly halvah gummies pie sweet roll croissant. Gummi bears candy canes sweet I love gummi bears cake gummies cotton candy shortbread. Pie danish I love sesame snaps I love tootsie roll tart muffin. Shortbread pudding oat cake chocolate bar marzipan oat cake marshmallow. Powder I love powder I love liquorice. Croissant sesame snaps bonbon fruitcake jelly')
fichero5.write ('Candy canes cake chocolate fruitcake muffin muffin jelly. Cake powder apple pie sugar plum cupcake sweet. I love cheesecake halvah lemon drops bear claw I love jelly beans jujubes. Apple pie I love ice cream dragée gummi bears caramels jujubes I love. Jelly lemon drops liquorice tart pie gummies. Topping chupa chups jelly-o icing jelly candy carrot cake soufflé sugar plum. Jelly-o sugar plum I love macaroon toffee lollipop macaroon I love candy canes. Liquorice shortbread jelly candy cotton candy liquorice jujubes sweet roll tiramisu. Marzipan cotton candy dragée biscuit dessert. Sweet roll fruitcake muffin I love candy canes I love. Liquorice sweet roll cotton candy pie I love I love gingerbread sugar plum. Fruitcake I love sesame snaps lemon drops I love marshmallow chocolate bar lemon drops cake. Jelly beans topping jelly-o chupa chups I love chocolate bar bear claw candy macaroon. Soufflé wafer apple pie I love jelly I love oat cake toffee.')

t1 = fichero1.read()
print(t1.replace('.','.\n'))


fichero1.close()
fichero2.close()
fichero3.close()
fichero4.close()
fichero5.close()

print (t1)
