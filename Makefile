protein_domains_vs_string_degree.png : downloads/%.txt
	python3 project.py

downloads/%.txt :
	bash string_dl.sh

.PHONY : clean
clean : 
	rm -f downloads/*.txt
	rm -f protein_domains_vs_string_degree.png