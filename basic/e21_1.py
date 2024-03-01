import geopandas
import matplotlib.pyplot  as plt
world_shape_file=geopandas.datasets.get_path('naturalearth_lowres')
world=geopandas.read_file(world_shape_file)
cities_shape_file=geopandas.datasets.get_path('naturalearth_cities')
cities=geopandas.read_file(cities_shape_file)
base=world.plot(color='violet')
cities.plot(ax=base,color='green',markersize=10)
plt.show()

