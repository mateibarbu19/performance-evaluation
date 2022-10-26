UTILS=../utils

build: README.pdf

README.pdf: HEADER.YAML README.md
	pandoc \
		--katex \
		--toc \
		--citeproc \
		-V colorlinks=true \
		-M date="`date "+%d %B %Y"`" \
		--include-in-header $(UTILS)/head.tex \
		HEADER.YAML README.md \
		-o README.pdf

clean:
	rm -f README.pdf