# River_Borders
An exploration of US state borders as dictated by the major riverways of North America

I used pixel manipulation to redraw the lower 48 using the major water ways of North America. The final product can be found here https://github.com/garesborn/River_Borders/blob/main/United_water_ways_of_america.png. Using County population and geographical coordinates data, I was able to calculate the population for each new state (source https://en.wikipedia.org/wiki/User:Michael_J/County_table).

The biggest hurdle was converting the geographical coordinates of each county to a corresponding pixel on the working image. This was due to the wonky scaling behind the Mercator projection. After deriving the proper equations, (shown https://github.com/garesborn/River_Borders/blob/main/eqs.png and https://github.com/garesborn/River_Borders/blob/main/pixelconversion.PNG) I could easily allocate the correct county populations to the proper state. I attempted to create states of roughly similar populations, but unsurprisingly rivers don't run based on population densities.

A black dot was placed in the pixel that corresponds to the proper geographical coordinates of each county. Once states were redrawn, retrieving the color of these pixels from the working image and summing the populations of like colors allowed me to calculate state populations.


The resultant populations are as follows (also found https://github.com/garesborn/River_Borders/blob/main/River_States.db):

Alabama - 6,506,300
Allegheny - 3,598,191
Altamaha - 6,046,025
Appalachia - 7,085,690
Boise - 1,240,606
Chesapeake - 6,827,718
Connecticut - 9,073,416
Cumberland - 8,933,257
Delaware - 1,392,713
Deschutes - 2,556,940
Erie - 6,110,187
Havasu - 14,210,296
Brazos - 11,839,858
Hudson - 4,409,751
Humboldt - 2,513,481
Huron - 8,221,501
Kissimmee - 3,133,147
Sabine - 4,981,301
Merrimack - 8,771,294
Michigan - 19,669,563
Mississippi - 6,568,909
Missouri - 7,921,657
Mokelumne - 5,978,887
Mullica - 8,791,894
Muskingum - 4,672,988
Neuse - 6,918,785
Nissequogue - 8,037,034
North Colorado - 3,379,835
Oahe - 1,266,333
Ohio - 7,694,960
Okeechobee - 6,617,139
Ozark - 8,070,063
Pecos - 12,097,772
Penobscot - 1,887,688
Platte - 3,093,215
Potomac - 8,805,925
Puget - 5,822,700
Salt Lake - 3,410,371
Salton - 8,469,714
San Joaquin - 8,566,449
Savannah - 4,589,348
Solomon - 5,292,684
South Colorado - 6,988,424
Superior - 6,269,716
Susquehanna - 7,222,886
Waccasassa - 7,603,047
Willamette - 1,806,877
Yellowstone - 1,708,471
