ifeq ($(_MY_MAKEFILE_),)

_MY_MAKEFILE_ := defined

CURRENT_DIR := $(notdir $(patsubst %/,%,$(shell pwd)))

ifndef CONFIG
	CONFIG=config_output.yaml
endif

ifndef UTILS
	UTILS=utils
endif

ifndef HEAD
	HEAD=$(UTILS)/head.tex
endif

README.pdf README.tex: README.md header.yaml $(CONFIG) $(HEAD)
	pandoc -d $(CONFIG) \
		-M date="`date "+%d %B %Y"`" \
		--include-in-header $(HEAD) \
		-o $@

ifndef DOC
	DOC=$(CURRENT_DIR).pdf
endif

$(DOC):: README.pdf
	cp $< $@

build: README.pdf $(DOC)

clean:
	rm -f README.pdf README.tex
	rm -f $(DOC)
endif
