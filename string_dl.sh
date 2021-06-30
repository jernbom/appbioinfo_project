# Download STRING H.Sapiens data
curl -o downloads/STRING_h_sapiens.txt.gz https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz
gunzip -f downloads/STRING_h_sapiens.txt.gz
# Download protein domain data
curl -L -o downloads/Ensembl_protein_domain.txt https://stockholmuniversity.box.com/shared/static/n8l0l1b3tg32wrzg2ensg8dnt7oua8ex