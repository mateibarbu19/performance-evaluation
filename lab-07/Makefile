DOC=$(CURRENT_DIR)-sol.pdf
UTILS=../utils

include ../Makefile

$(DOC):: README.pdf
	pdftk $< attach_files MyTaskManager/MyTaskManager.cpp output $(DOC)
