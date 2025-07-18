#!/bin/bash

rm -f *.bin *.mesh 
~/build/release-petsc/bin/partmesh -i geo_domain_2D_q8_FM1.vtu --ogs2metis
~/build/release-petsc/bin/partmesh -n 12 -m -i geo_domain_2D_q8_FM1.vtu -- geometry_*.vtu
