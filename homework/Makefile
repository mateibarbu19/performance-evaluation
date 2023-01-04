DOC=Performance-Evaluation-Report.pdf
SRC=src/test*.py src/requirements.txt res/chart.py
UTILS=../utils
HEAD=utils/head.tex

include ../Makefile

homework.zip: $(DOC)
	zip -FSr $@ $< $(SRC)

clean::
	rm -f homework.zip
