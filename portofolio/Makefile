DIRS=review/ presentation/
DOCS=review/Review.pdf presentation/Presentation.pdf
ARTICLE=articles/peer-review-process-oakland22.pdf

build: portofolio.zip

$(DOCS): %.pdf:
	make -C $(dir $@) build

portofolio.zip: $(DOCS)
	zip -FSr $@ $^ $(ARTICLE)

clean:
	rm -f portofolio.zip
	for dir in $(DIRS); do    \
		make -C $$dir clean ; \
	done
