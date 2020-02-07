##  ldc-rightzone.py: identifies Austin sites to right-zone
##  Copyright (C) 2020  Daniel Hardesty Lewis (GitHub: dhardestylewis)

##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.

##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.

##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <https://www.gnu.org/licenses/>.


import geopandas as gpd
import numpy as np

##  Import City of Austin land use inventory and LDC Draft 2 zoning
##  Inventory permalink:
##      https://data.austintexas.gov/Locations-and-Maps/Land-Use-Inventory-Detailed/fj9m-h5qy
inventory = gpd.read_file("../Land_Use_Inventory_Detailed/geo_export_ed6a563c-90dd-40d2-8e33-608d902989e7.shp")
##  LDC Draft 2 zoning link:
##      https://app.box.com/s/af8defnrglqdwnqihhiulnnvozvg5164
zoning = gpd.read_file("../Proposed_Zoning_Second_Reading/Proposed_Zoning_Second_Reading.shp")

multiplexes = inventory[inventory['land_use']==210.0]

multiplex_zoning = gpd.sjoin(multiplexes.to_crs(zoning.crs),zoning,op='intersects',how='left')

##  These sites were originally build as three- and fourplexes under a previous
##      code. They have since been downzoned.
multiplexes_downzoned = multiplex_zoning[multiplex_zoning['LDC_ZONE_S'].isin(['LA', 'RR', 'R2A', 'R2B', 'R2B-HD', 'R2C'])]
multiplexes_downzoned = multiplexes_downzoned.drop(columns=['index_right', 'OBJECTID', 'SHAPE_Leng', 'SHAPE_Area'])

##  Under LDC Draft 1 Reading Amendment Tovo #4, these are the properties which
##      the city must right-zone.
multiplexes_downzoned.to_file("ALDC-ACBA-Rightzoned_missing_middle.shp")

