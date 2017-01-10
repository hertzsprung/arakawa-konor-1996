#!/bin/bash
set -e
rm -rf [0-9]*
blockMesh
setTheta
setExnerBalancedH
thermoVars
cp constant/Uf 0/Uf
cp constant/radiation 0/radiation
exnerFoamH
