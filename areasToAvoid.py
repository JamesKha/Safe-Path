import geopandas as gpd
from shapely.geometry import Polygon
from shapely.geometry.multipolygon import MultiPolygon
from shapely import wkt

lon_lat_list_1 = [[-73.88288485610137, 40.6713475761285, ], [-73.88187034963107, 40.671443758922834], [-73.88183653274871, 40.6712578053953], [-73.88291021876313, 40.67108467578281]]
lon_lat_list_2 = [[-77.01980620652286, 38.89373064645292], [-77.01597313336877, 38.89366456008459], [-77.01592461345543, 38.89350406435629], [77.01985472643615, 38.89351350528131]]
lon_lat_list_3 = [[-73.99323914300739, 40.75230617940999], [-73.9907378546972, 40.75119382478945], [-73.99088089928028, 40.75099943254187], [-73.99340244093696, 40.75205809080204]]
lon_lat_list_4 = [[-73.87093974982044, 40.82273628803473], [-73.87010229895341, 40.822811582521744], [-73.87003596621149, 40.82261707158884], [-73.87086512548576, 40.822504129495044]]
lon_lat_list_5 = [[-73.91989243077671, 40.83874526858156], [-73.91935571709065, 40.838323892160844], [-73.91947723717053, 40.838178325138465], [-73.92000382418324, 40.838599702484494]]
lon_lat_list_6 = [[-73.99569892445557, 40.754102364435894], [-73.99304001015363, 40.752979699450854], [-73.99311265808538, 40.752825606698856], [-73.9958296907327, 40.753959280736964]]
lon_lat_list_7 = [[-73.98710389540031, 40.750518513614594], [-73.98422193493894, 40.74931378806984], [-73.9843421512827, 40.74910562172596], [-73.98715864847888, 40.75029389583511]]
lon_lat_list_8 = [[-73.84722713332482, 40.887700851471244], [-73.84695659826608, 40.88760498130328], [-73.84721867910423, 40.88707449719653], [-73.84767520701587, 40.887010583161654]]
lon_lat_list_9 = [[-73.90038858261332, 40.85424856293518], [-73.90024486086335, 40.85424856293518], [-73.90079438520144, 40.85295045254363], [-73.90102264915726, 40.85298242601149]]
lon_lat_list_10 = [[-73.95402190296713, 40.648808089778825], [-73.9529561481669, 40.64887770482077], [-73.95290563679325, 40.64871171217062], [-73.95405719286119, 40.64864743940491]]

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

mutipoly = [polygon_geom1, polygon_geom2, polygon_geom3, polygon_geom4, polygon_geom5, polygon_geom6, polygon_geom7, polygon_geom8, polygon_geom9, polygon_geom10]


def getAreasToAvoid():
    return mutipoly