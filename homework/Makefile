DOC=Performance-Evaluation-Report.pdf
SRC=src/client.py src/test*.py src/requirements.txt

include ../Makefile

homework.zip: $(DOC)
	zip -FSr $@ $< $(SRC)

clean::
	rm -f homework.zip
