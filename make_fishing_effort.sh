rm osm_param-effort.csv
for i in {0..100}
do
    echo "mortality.fishing.spatial.distrib.file.sp$i;Fishing_effort__density_boats_under60_filtered_satellitebiaiscorrected.csv" >> osm_param-effort.csv
done
