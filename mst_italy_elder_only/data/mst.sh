#! /bin/bash#! /bin/bash
# centenarian
expert construct -i centenarian/microbiome.txt -o centenarian/ontology.pkl
expert map --to-otlg -i centenarian/metadata.csv -o centenarian/labels.h5 -t centenarian/ontology.pkl
expert convert -i centenarian/source_path.txt -o centenarian/source.h5 --in-cm
expert convert -i centenarian/query_path.txt -o centenarian/query.h5 --in-cm
expert train -i centenarian/source.h5 -t centenarian/ontology.pkl -l centenarian/labels.h5 -o ../model/centenarian/independent_model
expert transfer -m ../../mst/model/disease_model -i centenarian/source.h5 -t centenarian/ontology.pkl -l centenarian/labels.h5 -o ../model/centenarian/transfer_model --update-statistics --finetune
expert search -i centenarian/query.h5 -m ../model/centenarian/independent_model -o ../result/centenarian/independent_result
expert search -i centenarian/query.h5 -m ../model/centenarian/transfer_model -o ../result/centenarian/transfer_result
# expert search --measure-unknown -i centenarian/query.h5 -m ../model/centenarian/independent_model -o ../result/centenarian/independent_result
# expert search --measure-unknown -i centenarian/query.h5 -m ../model/centenarian/transfer_model -o ../result/centenarian/transfer_result

# elder
expert construct -i elder/microbiome.txt -o elder/ontology.pkl
expert map --to-otlg -i elder/metadata.csv -o elder/labels.h5 -t elder/ontology.pkl
expert convert -i elder/source_path.txt -o elder/source.h5 --in-cm
expert convert -i elder/query_path.txt -o elder/query.h5 --in-cm
expert train -i elder/source.h5 -t elder/ontology.pkl -l elder/labels.h5 -o ../model/elder/independent_model
expert transfer -m ../../mst/model/disease_model -i elder/source.h5 -t elder/ontology.pkl -l elder/labels.h5 -o ../model/elder/transfer_model --update-statistics --finetune
expert search -i elder/query.h5 -m ../model/elder/independent_model -o ../result/elder/independent_result
expert search -i elder/query.h5 -m ../model/elder/transfer_model -o ../result/elder/transfer_result
# expert search --measure-unknown -i elder/query.h5 -m ../model/elder/independent_model -o ../result/elder/independent_result
# expert search --measure-unknown -i elder/query.h5 -m ../model/elder/transfer_model -o ../result/elder/transfer_result

# centenarian
expert construct -i centenarian/microbiome.txt -o centenarian/ontology.pkl
expert map --to-otlg -i centenarian/metadata.csv -o centenarian/labels.h5 -t centenarian/ontology.pkl
expert convert -i centenarian/source_path.txt -o centenarian/source.h5 --in-cm
expert convert -i centenarian/query_path.txt -o centenarian/query.h5 --in-cm
expert train -i centenarian/source.h5 -t centenarian/ontology.pkl -l centenarian/labels.h5 -o ../model/centenarian/independent_model
expert transfer -m ../../mst/model/disease_model -i centenarian/source.h5 -t centenarian/ontology.pkl -l centenarian/labels.h5 -o ../model/centenarian/transfer_model --update-statistics --finetune
expert search -i centenarian/query.h5 -m ../model/centenarian/independent_model -o ../result/centenarian/independent_result
expert search -i centenarian/query.h5 -m ../model/centenarian/transfer_model -o ../result/centenarian/transfer_result
# expert search --measure-unknown -i centenarian/query.h5 -m ../model/centenarian/independent_model -o ../result/centenarian/independent_result
# expert search --measure-unknown -i centenarian/query.h5 -m ../model/centenarian/transfer_model -o ../result/centenarian/transfer_result

# elder
expert construct -i elder/microbiome.txt -o elder/ontology.pkl
expert map --to-otlg -i elder/metadata.csv -o elder/labels.h5 -t elder/ontology.pkl
expert convert -i elder/source_path.txt -o elder/source.h5 --in-cm
expert convert -i elder/query_path.txt -o elder/query.h5 --in-cm
expert train -i elder/source.h5 -t elder/ontology.pkl -l elder/labels.h5 -o ../model/elder/independent_model
expert transfer -m ../../mst/model/disease_model -i elder/source.h5 -t elder/ontology.pkl -l elder/labels.h5 -o ../model/elder/transfer_model --update-statistics --finetune
expert search -i elder/query.h5 -m ../model/elder/independent_model -o ../result/elder/independent_result
expert search -i elder/query.h5 -m ../model/elder/transfer_model -o ../result/elder/transfer_result
# expert search --measure-unknown -i elder/query.h5 -m ../model/elder/independent_model -o ../result/elder/independent_result
# expert search --measure-unknown -i elder/query.h5 -m ../model/elder/transfer_model -o ../result/elder/transfer_result
