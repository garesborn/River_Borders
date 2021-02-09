from PIL import Image
import sqlite3 as sql
import pandas as pd
from sqlalchemy import create_engine
import math

img = Image.open('river_states.png')
#img = img.convert('RGB')
pixels = img.load()


NE = [['CT', 'RI', "MA", 'NH'], 'green', 'Merrimack']
NS = [['ME','NH'], 'yellow', 'Penobscot']
CT = [['CT', 'MA', 'VT', 'NY'], 'teal', 'Connecticut']
NJ = [['NJ', 'NY'], 'yellow', 'Mullica']
hudson = [['NY'], 'gray', 'Hudson']
LongI = [['NY'], 'black', 'Nissequogue']
philly = [['PA', 'DE'], 'black', 'Susquehanna']
chess = [['PA', 'MD', 'DC'], 'yellow', 'Chesapeake']
pitt = [['PA', 'NY', 'MD', 'WV'], 'teal', 'Allegheny']
DE = [['VA', 'DE', 'MD'], 'green', 'Delaware']#10
huron = [['MI', 'OH', 'IN'], 'black', 'Huron']
midsouth = [['KY', 'TN', 'VA', 'AL', "MS", 'WV'], 'black', 'Cumberland']
appal = [['AL', 'GA', 'SC', 'NC', 'TN', 'VA'], 'teal', 'Appalachia'] 
caro = [['SC', 'NC', 'VA'], 'yellow', 'Neuse']
VA = [['VA','PA','NC', 'WV', 'MD'], 'gray', 'Potomac']
GA = [['GA','FL'], 'gray', 'Altamaha']
sav = [['GA', 'SC', 'NC'], 'green', 'Savannah']
Miami = [['FL'], 'teal', 'Okeechobee']
eastfl = [['FL'], 'green', 'Kissimmee']
tampa = [['FL'], 'black', 'Waccasassa']#20
erie = [['OH', 'PA', 'NY'], 'green', 'Erie'] 
eastoh = [['OH', 'IN'], 'teal', 'Muskingum']
OH = [['OH', 'IN'], 'gray', 'Ohio']
MI = [['MI', 'IL', 'IN', 'WI'], 'yellow', 'Michigan']
AL = [['AL', 'FL', 'GA', 'MS'], 'yellow', 'Alabama']
Miss = [['MS', 'LA', 'TN', 'AL', 'KY'], 'green', 'Mississippi']
sup = [['MN', 'WI', 'MI'], 'teal', 'Superior'] 
mo = [['MO', 'SD', 'IA', 'MN', 'KS'], 'black', 'Missouri']
LA = [['LA','TX', 'AR'], 'teal', 'Louisiana']
ho = [['TX'], 'black', 'Houston']#30
RG = [['TX', 'NM'], 'yellow', 'Pecos']
AR = [['AR', 'OK','LA', 'KS', 'MO'], 'gray', 'Ozark']
DK = [['ND','SD','NE','MT', 'WY'], 'green', 'Oahe']
AZ = [['AZ','CO',"NM", 'UT'], 'black', 'South Colorado']
den = [['CO', 'WY', 'NE', 'SD'], 'yellow', 'Platte']
KS = [['OK', 'CO', 'NE', 'KS', 'NM'], 'teal', 'Solomon']
OK = [['OK', 'TX', 'CO', 'NE', 'KS', 'NM', 'UT'], 'green', 'North Colorado']
WA = [['WA', 'OR'], 'green', 'Puget'] 
saltlake = [['UT', 'MT', 'WY', 'ID', 'ND', 'SD', 'CO', 'AZ'], 'gray', 'Salt Lake']
losA = [['CA'], 'gray', 'Havasu']#40
SD = [['CA'], 'teal', 'Salton']
carson = [['NV', 'UT'], 'yellow', 'Humboldt']
bayarea = [['CA'], 'black', 'San Joaquin']
nocal = [['CA', 'OR'], 'green', 'Mokelumne'] 
YS = [["MT", 'ND', 'WY', 'WA', 'ID'], 'teal', 'Yellowstone']
will = [['OR', 'WA', 'CA'], 'yellow', 'Willamette']
OR = [['OR', 'WA', 'NV'], 'gray', 'Deschutes']
Sac = [['ID', 'OR', 'WY', 'MT'], 'black', 'Boise']


states = [NE, NS, CT, NJ, LongI, hudson, philly, chess, pitt, DE, huron, midsouth, appal, 
          caro, VA, GA, sav, Miami, tampa, eastfl, erie, eastoh, OH, MI, AL, Miss, sup, mo, LA, ho, RG, AR,
          DK, AZ, den, KS, OK, WA, saltlake, losA, SD, carson, bayarea, nocal,
          YS, OR, will, Sac]


cnx = create_engine('sqlite:///C:/Users/Gar/OneDrive/River_Borders/us_county_data.db').connect() 

st_df = pd.read_sql_table('US_COUNTY_DATA', cnx)

df = st_df

# =============================================================================
#                   series of tests for color of given pixel
# =============================================================================

def is_black(rgb):
    th = 15 #threshold for amount of r g or b in a given pixel
    if rgb[0] < th and rgb[1] < th and rgb[2] < th:
        return True
    else:
        return False
    
def is_white(rgb):
    th = 15
    if 255- rgb[0] < th and 255 - rgb[1] < th and 255 - rgb[2] < th:
        return True
    else:
        return False


def is_gray(rgb):
    th = 15
    if abs(128 - rgb[0]) < th and  abs(128 - rgb[1]) < th and  abs(128 - rgb[2]) < th:
        return True
    else:
        return False
    
def is_teal(rgb):
    th = 15
    if 255 - rgb[0] > 240 and 255 - rgb[1] < th and 255 - rgb[2] < th:
        return True
    else:
        return False
    
def is_green(rgb):
    th = 15
    if 255 - rgb[0] > 240 and 255 - rgb[1] < th and 255 - rgb[2] > 240:
        return True
    else:
        return False
    
def is_yellow(rgb):
    th = 15
    if 255 - rgb[0] < th and 255 - rgb[1] < th and 255 - rgb[2] > 240:
        return True
    else:
        return False

# =============================================================================
#  Conversion of latitude and longitude to x,y pixel coordinates in image
# =============================================================================
    
def geopixel(long, lat, img = img, mnlong = -127, mxlong = -65, mnlat = 23, mxlat = 51):
    x = (long-mnlong)*(img.width/(mxlong-mnlong))
    #convert latitudes to rad
    rmnlat = mnlat*math.pi/180 
    rmxlat = mxlat*math.pi/180
    
    #scale min and max latitudes of field of view to Mercator Projection
    mn = math.log(math.tan((math.pi/4)+(rmnlat/2))) 
    mx = math.log(math.tan((math.pi/4)+(rmxlat/2)))
    
    #calculate pixels per radian of mercator proj
    pxscl = img.height/(mx-mn) 
    
    #convert desired lat to radians
    latRad = lat * math.pi /180 
    
    #scale desired lat to merc proj
    scaled = math.log(math.tan((math.pi/4)+(latRad/2))) 
    
    z = scaled-mn #find distance of desired lat from bottom of FOV (mercator scaled radians)
    y = img.height - pxscl * z #convert distance to pixels to calc final pixel y value
    
    return (round(x),round(y))


# =============================================================================
#           Pass pixel rgb tuple, return if pixel is given color
# =============================================================================
def bol(rgb, color):
    if color == 'white':
        bol = is_white(rgb)
    elif color == 'black':
        bol = is_black(rgb)
    elif color == 'green':
        bol = is_green(rgb)
    elif color == 'gray':
        bol = is_gray(rgb)
    elif color == 'teal':
        bol = is_teal(rgb)
    elif color == 'yellow':
        bol = is_yellow(rgb)
    return bol
    
#                   TROUBLESHOOTING TEST CODE
# =============================================================================
# state = []
# 
# for x in range(img.width):
#     for y in range(img.height):
#         
#         if x < 3 or x > img.width - 3:
#             pass
#         elif y < 3 or y > img.height - 3:
#             pass
#         else:
#             pix = img.getpixel((x,y))
#             if is_white(pix):
#                 state.append((x,y))
# =============================================================================


# =============================================================================
#               For test to ensure no duplicate counts
# =============================================================================
ct_locs = {}
c = 0
for i in df.index:
    #   retieve lat and long of each county
    lat = df['Latitude'][i]
    lat = float(lat[:-1])
    long = df['Longitude'][i]
    long = float(long[:-1].replace('\U00002013', '-'))
    #   convert geocoords of each county to pixel coords
    coords = geopixel(long, lat)
    #print((df['Longitude'][i],df['Latitude'][i]))
    #print(coords, df['State'][i])
    #   append tuple to dictionary of pixel coords with county pop, us state, and county name
    ct_locs[coords] = (df['Population(2010)'][i], df['State'][i], df['County [2]'][i])

st_pops = {}
used_locs = [] # test to ensure no duplicate counting of county populations

# NYC created an issue due to how tightly packed their counties are on the working image. 
# used a manual work around to fix this
ny = [(1434, 395),
 (1440, 345),
 (1437, 362),
 (1431, 398),
 (1422, 375),
 (1437, 374),
 (1443, 328),
 (1429, 384),
 (1445, 306),
 (1437, 384)]

for st in states:
    df = pd.read_sql_table('US_COUNTY_DATA', cnx)
    dfbol = df.State.isin(st[0])
    #create a new DF with only states given in state tuple
    # EX. states[0] = NE, DF created from NE[0] only contains counties from CT, RI, MA, NH (line 12  for reference)
    df = df[dfbol].reset_index()
    temp_loc = {}
    c = 0
    for i in df.index:
        lat = df['Latitude'][i]
        lat = float(lat[:-1])
        long = df['Longitude'][i]
        long = float(long[:-1].replace('\U00002013', '-'))
        coords = geopixel(long, lat)
        #print((df['Longitude'][i],df['Latitude'][i]))
        #print(coords, df['State'][i])
        temp_loc[coords] = (df['Population(2010)'][i], df['State'][i], df['County [2]'][i])
    
    
    pop = []
    for i in temp_loc:
        if bol(img.getpixel(i), st[1]): #From line 153, if pixel is color st[0] (see line 12 for ex. format)
            #manual exception
            if i == (1322, 345) or i == (1339, 344):
                if st == pitt:
                    pop.append(temp_loc[i])
                    used_locs.append(i)
                else:
                    pass
            #manual exception
            elif i in ny:
                if st == CT:
                    pop.append(temp_loc[i])
                    used_locs.append(i)
            else:
                #add current county population to working state pop list
                pop.append(temp_loc[i])
                # add current county to used locations to ensure no duplicates
                used_locs.append(i)
                
    tot = 0
    for i in pop:
        tot = tot+ i[0]
    # add new state population, color to dictionary where key is new state name
    st_pops[st[2]] = tot, st[1]


sts = []
pops = []


tot = 0
for k,v in sorted(st_pops.items()):
    votes = int(v[0]/698630 +2) 
    # I calculated theoretical electoral votes, 
    # but didnt include them in the final product as the politics of 
    # these states would be drastically different than the current US
    print(k, v[0])
    sts.append(k)
    pops.append(v[0])
    tot = tot + v[0]
    
print(tot) # confirming that the county populations counted sum to continental US population (2010)

#Check for missed counties
missed = []
for i in ct_locs:
    if i not in used_locs and i[0] >= 0 and i[1] >= 0:
        missed.append(i)

dup = []
lst = []

for i in used_locs:
    if i not in lst:
        lst.append(i)
    else:
        dup.append(i)  
              
for i in missed:
    print(ct_locs[i], i)
    pixels[i[0], i[1]] = (255,0,0)
    


img.save('missed_counties.png')

riv_df = pd.DataFrame({'State': sts, 'Population': pops})


conn = sql.connect('River_States.db')    
c = conn.cursor()
riv_df.to_sql('New_State_Populations', conn, if_exists = 'replace', index = False)

st_df.to_sql('US_County_Data', conn, if_exists = 'replace', index = False)

conn.close()