ifeq ($(_MY_MAKEFILE_),)

_MY_MAKEFILE_ := defined

DATE = $(shell date -R | cut -d" " -f 2-4)

CURRENT_DIR := $(notdir $(patsubst %/,%,$(shell pwd)))

CONFIG ?= config_output.yaml

UTILS ?= utils

HEAD ?= $(UTILS)/head.tex

CSL ?= $(UTILS)/ieee.csl

README.pdf README.tex: README.md header.yaml $(CONFIG) $(HEAD)
	pandoc -d $(CONFIG) \
		-M date="$(DATE)" \
		--include-in-header $(HEAD) \
		--csl $(CSL) \
		-o $@

ifndef DOC
	DOC=$(CURRENT_DIR).pdf
endif

$(DOC):: README.pdf
	cp $< $@

build: README.pdf $(DOC)

clean::
	rm -f README.pdf README.tex
	rm -f $(DOC)

endif
