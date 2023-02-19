import geopandas as gpd
from shapely.geometry import Polygon
from shapely.geometry.multipolygon import MultiPolygon
from shapely import wkt

lon_lat_list_1 = [[-73.88288485610137, 40.6713475761285, ], [-73.88187034963107, 40.671443758922834], [-73.88183653274871, 40.6712578053953], [-73.88291021876313, 40.67108467578281]]
lon_lat_list_2 = [[-73.911871, 40.822129],[-73.911585, 40.822486],[-73.911366, 40.822110],[-73.911803, 40.822056],[-73.911871, 40.822129]]
lon_lat_list_3 = [[-73.99323914300739, 40.75230617940999], [-73.9907378546972, 40.75119382478945], [-73.99088089928028, 40.75099943254187], [-73.99340244093696, 40.75205809080204]]
lon_lat_list_4 = [[-73.87093974982044, 40.82273628803473], [-73.87010229895341, 40.822811582521744], [-73.87003596621149, 40.82261707158884], [-73.87086512548576, 40.822504129495044]]
lon_lat_list_5 = [[-73.91989243077671, 40.83874526858156], [-73.91935571709065, 40.838323892160844], [-73.91947723717053, 40.838178325138465], [-73.92000382418324, 40.838599702484494]]
lon_lat_list_6 = [[-73.99569892445557, 40.754102364435894], [-73.99304001015363, 40.752979699450854], [-73.99311265808538, 40.752825606698856], [-73.9958296907327, 40.753959280736964]]
lon_lat_list_7 = [[-73.98710389540031, 40.750518513614594], [-73.98422193493894, 40.74931378806984], [-73.9843421512827, 40.74910562172596], [-73.98715864847888, 40.75029389583511]]
lon_lat_list_8 = [[-73.84722713332482, 40.887700851471244], [-73.84695659826608, 40.88760498130328], [-73.84721867910423, 40.88707449719653], [-73.84767520701587, 40.887010583161654]]
lon_lat_list_9 = [[-73.90038858261332, 40.85424856293518], [-73.90024486086335, 40.85424856293518], [-73.90079438520144, 40.85295045254363], [-73.90102264915726, 40.85298242601149]]
lon_lat_list_10 = [[-73.95402190296713, 40.648808089778825], [-73.9529561481669, 40.64887770482077], [-73.95290563679325, 40.64871171217062], [-73.95405719286119, 40.64864743940491]]

lon_lat_list_11 = [[-73.98486331891539, 40.75356670490905],[-73.98189801849675, 40.75232430179593],[-73.98199818812141, 40.75221717369166],[-73.98496329590543, 40.75344769124387]]
lon_lat_list_12 = [[-73.9778182202242, 40.757920689080585],[-73.97757119096588, 40.757792379183650],[-73.97799243395804, 40.757312403429815],[-73.97820500257136, 40.757398105878174]]
lon_lat_list_13 = [[-73.94806102842674, 40.7897238776725],[-73.94666950356398, 40.7891438359933],[-73.94675289082168, 40.7890175677465],[-73.94810272205560, 40.7896212856362]]
lon_lat_list_14 = [[-73.94159481957345, 40.80122873303868],[-73.94028668196844, 40.80066851783844],[-73.94037006922609, 40.80056199752055],[-73.94196750237633, 40.80121689755641]]
lon_lat_list_15 = [[-73.91951361395775, 40.83824302610030], [-73.91930136192845, 40.83799743098060], [-73.92064354387850, 40.83745428469561], [-73.92044377726260, 40.83702448752513]] 
lon_lat_list_16 = [[-73.90084136644525, 40.84471307897616], [-73.89956771871985, 40.84457543665383], [-73.90098692618530, 40.84424509391392], [-73.89978605832991, 40.84412580307538]] 
lon_lat_list_17 = [[-73.89673926517392, 40.85279770270785],[-73.89622521462688, 40.85258384914733],[-73.89729186951190, 40.851883959941276],[-73.89668786011921, 40.85167010343143]] 
lon_lat_list_18 = [[-73.79295409939627, 40.707264621840814],[-73.79146358378712, 40.707768035299665],[ -73.7913109747886, 40.70762893647794],[-73.79289902002049, 40.70715810988992]]
lon_lat_list_19 = [[-73.8318673291579, 40.69969620102948],[-73.83166698990858, 40.69975874178097],[-73.83041862612805, 40.69721085373647],[-73.83068378101686, 40.69717511480447]]
lon_lat_list_20 = [[ -73.92506935201055, 40.8101503323559],[-73.92521069079741,40.80992924742742],[-73.92300580572098, 40.80904490034672],[-73.92287388951995,40.80924459265299]]

lon_lat_list_21 = [[ -73.92506935201055,40.8101503323559],[-73.92521069079741,40.80992924742742],[-73.92300580572098,40.80904490034672],[-73.92287388951995,40.80924459265299]]
lon_lat_list_22 =[[-73.92506935201055,40.8101503323559],[-73.92521069079741,40.80992924742742],[-73.92300580572098,40.80904490034672],[-73.92287388951995, 40.80924459265299]] 
lon_lat_list_23 =[[-73.93667640487321,40.69078696193088],[-73.93654718633638,40.69010536847719],[-73.9364179677988,40.69011388843845],[-73.9365022407581,40.690804001678]]
lon_lat_list_24 = [[-73.93981654777014,40.6496345844032],[-73.93978877431394,40.6493606488379],[-73.93791406599463,40.649413328841774],[-73.93798349963636,40.64976101582292]]       
lon_lat_list_25 =[[-73.87970850719189,40.86966490777934],[-73.87956910913137,40.86946219051654],[-73.87840031000668,40.870151426678945],[-73.87859332270617,40.87024873002966],[-73.87970850719189,40.86966490777934]]
lon_lat_list_26 =[[-73.82002959308566,40.69771065497707],[-73.81994380966331,40.697548060796606],[-73.81819597244018,40.698084620086206],[-73.8183032017181,40.69822282405164],[-73.82002959308566,40.69771065497707]]
lon_lat_list_27 =[[-73.97499146190151,40.63007101348347],[-73.97490567847917,40.629948944154705],[-73.97214988604745,40.631267281097905],[-73.9721927777586,40.63143817472201],[-73.97499146190151,40.63007101348347]]
 


polygon_geom1 = Polygon(lon_lat_list_1)
polygon1 = gpd.GeoDataFrame(index=[0], crs='epsg:3785', geometry=[polygon_geom1])

polygon_geom2 = Polygon(lon_lat_list_2)
polygon2 = gpd.GeoDataFrame(index=[0], crs='epsg:3785', geometry=[polygon_geom2])

polygon_geom3 = Polygon(lon_lat_list_3)
polygon3 = gpd.GeoDataFrame(index=[0], crs='epsg:3785', geometry=[polygon_geom3])

polygon_geom4 = Polygon(lon_lat_list_4)
polygon4 = gpd.GeoDataFrame(index=[0], crs='epsg:3785', geometry=[polygon_geom4])

polygon_geom5 = Polygon(lon_lat_list_5)
polygon5 = gpd.GeoDataFrame(index=[0], crs='epsg:3785', geometry=[polygon_geom5])

polygon_geom6 = Polygon(lon_lat_list_6)
polygon6 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom6])

polygon_geom7 = Polygon(lon_lat_list_7)
polygon7 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom7])

polygon_geom8 = Polygon(lon_lat_list_8)
polygon8 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom8])

polygon_geom9 = Polygon(lon_lat_list_9)
polygon9 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom9])

polygon_geom10 = Polygon(lon_lat_list_10)
polygon10 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom10])


# polygon_geom11 = Polygon(lon_lat_list_11)
# polygon11 = gpd.GeoDataFrame(index=[0], crs='epsg:3785', geometry=[polygon_geom11])

# polygon_geom12 = Polygon(lon_lat_list_12)
# polygon12 = gpd.GeoDataFrame(index=[0], crs='epsg:3785', geometry=[polygon_geom12])

# polygon_geom13 = Polygon(lon_lat_list_13)
# polygon13 = gpd.GeoDataFrame(index=[0], crs='epsg:3785', geometry=[polygon_geom13])

# polygon_geom14 = Polygon(lon_lat_list_14)
# polygon14 = gpd.GeoDataFrame(index=[0], crs='epsg:3785', geometry=[polygon_geom14])

# polygon_geom15 = Polygon(lon_lat_list_15)
# polygon15 = gpd.GeoDataFrame(index=[0], crs='epsg:3785', geometry=[polygon_geom15])

# polygon_geom16 = Polygon(lon_lat_list_16)
# polygon16 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom16])

# polygon_geom17 = Polygon(lon_lat_list_17)
# polygon17 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom17])

# polygon_geom18 = Polygon(lon_lat_list_18)
# polygon18 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom18])

# polygon_geom19 = Polygon(lon_lat_list_19)
# polygon19 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom19])

# polygon_geom20 = Polygon(lon_lat_list_20)
# polygon20 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom20])

# polygon_geom21 = Polygon(lon_lat_list_21)
# polygon21 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom21])

# polygon_geom22 = Polygon(lon_lat_list_22)
# polygon22 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom22])

# polygon_geom23 = Polygon(lon_lat_list_23)
# polygon23 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom23])

# polygon_geom24 = Polygon(lon_lat_list_24)
# polygon24 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom24])

# polygon_geom25 = Polygon(lon_lat_list_25)
# polygon25 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom25])

# polygon_geom26 = Polygon(lon_lat_list_26)
# polygon26 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom26])

# polygon_geom27 = Polygon(lon_lat_list_27)
# polygon27 = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom27])



mutipoly = [polygon_geom1, polygon_geom2, polygon_geom3, polygon_geom4, polygon_geom5, polygon_geom6, polygon_geom7, polygon_geom8, polygon_geom9, polygon_geom10]


def getAreasToAvoid():
    return mutipoly