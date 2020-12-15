# River_Borders
An exploration of US state borders as dictated by the major riverways of North America

I used pixel manipulation to redraw the lower 48 using the major water ways of North America. Using County population and geographical coordinates data, I was able to calculate the population for each new state (source https://en.wikipedia.org/wiki/User:Michael_J/County_table).

The biggest hurdle was converting the geographical coordinates of each county to a corresponding pixel on the working image. This was due to the wonky scaling behind the Mercator projection. After deriving the proper equations, I could easily allocate the correct county populations to the proper state. I attempted to create states of roughly similar populations, but unsurprisingly rivers don't run based on population densities.

A black dot was placed in the pixel that corresponds to the proper geographical coordinates of each county. Once states were redrawn, retrieving the color of these pixels from the working image and summing the populations of like colors allowed me to calculate state populations.
