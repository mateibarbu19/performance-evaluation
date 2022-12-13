DOC=Lab-07-Sol.pdf
HEAD=../utils/head.tex

include ../Makefile

build-doc: README.pdf
	pdftk README.pdf attach_files MyTaskManager/MyTaskManager.cpp output $(DOC)

clean-doc: clean
	rm -f $(DOC)