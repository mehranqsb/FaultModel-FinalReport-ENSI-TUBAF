#!/bin/bash

rm -f \#* *~ *.vtu

gmsh -2 geo2D.geo -o geo2D.msh -format msh2

~/build/release/bin/GMSH2OGS -i geo2D.msh -o geo.vtu -e --gmsh2_physical_id
~/build/release/bin/NodeReordering -i geo.vtu -o geo_reorder.vtu
#
~/build/release/bin/editMaterialID -i geo_reorder.vtu -o geo_reorder.vtu -r -m 0  -n 0
~/build/release/bin/editMaterialID -i geo_reorder.vtu -o geo_reorder.vtu -r -m 1  -n 0
~/build/release/bin/editMaterialID -i geo_reorder.vtu -o geo_reorder.vtu -r -m 2  -n 1
~/build/release/bin/editMaterialID -i geo_reorder.vtu -o geo_reorder.vtu -r -m 3  -n 0
~/build/release/bin/editMaterialID -i geo_reorder.vtu -o geo_reorder.vtu -r -m 4  -n 0
#
mv geo_reorder.vtu geo_domain_2D.vtu
#
~/build/release/bin/createQuadraticMesh -i geo_domain_2D.vtu -o geo_domain_2D_q8.vtu
#
~/build/release/bin/constructMeshesFromGeometry -m geo_domain_2D_q8.vtu -g geo_domain.gml -s 1e-8
python3 materialIDs2D.py

rm -f geo.vtu geo_domain_2D.vtu

# ~/build/release/bin/identifySubdomains -m geo_domain_2D_q8_FM1.vtu geometry_pinj.vtu 
