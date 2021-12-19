#! /bin/bash
# centenarien
expert construct -i centenarien/microbiome.txt -o centenarien/ontology.pkl
expert map --to-otlg -i centenarien/metadata.csv -o centenarien/labels.h5 -t centenarien/ontology.pkl
expert convert -i centenarien/source_path.txt -o centenarien/source.h5 --in-cm
expert convert -i centenarien/query_path.txt -o centenarien/query.h5 --in-cm
expert train -i centenarien/source.h5 -t centenarien/ontology.pkl -l centenarien/labels.h5 -o ../model/centenarien/independent_model
expert transfer -m ../../mst/model/disease_model -i centenarien/source.h5 -t centenarien/ontology.pkl -l centenarien/labels.h5 -o ../model/centenarien/transfer_model --update-statistics --finetune
expert search -i centenarien/query.h5 -m ../model/centenarien/independent_model -o ../result/centenarien/independent_result
expert search -i centenarien/query.h5 -m ../model/centenarien/transfer_model -o ../result/centenarien/transfer_result
# elder
expert construct -i elder/microbiome.txt -o elder/ontology.pkl
expert map --to-otlg -i elder/metadata.csv -o elder/labels.h5 -t centenarien/ontology.pkl
expert convert -i elder/source_path.txt -o elder/source.h5 --in-cm
expert convert -i elder/query_path.txt -o elder/query.h5 --in-cm
expert train -i elder/source.h5 -t elder/ontology.pkl -l elder/labels.h5 -o ../model/elder/independent_model
expert transfer -m ../../mst/model/disease_model -i elder/source.h5 -t elder/ontology.pkl -l elder/labels.h5 -o ../model/elder/transfer_model --update-statistics --finetune
expert search -i elder/query.h5 -m ../model/elder/independent_model -o ../result/elder/independent_result
expert search -i elder/query.h5 -m ../model/elder/transfer_model -o ../result/elder/transfer_result