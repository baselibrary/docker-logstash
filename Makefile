NAME     = baselibrary/logstash
REPO     = git@github.com:baselibrary/docker-logstash.git
VERSIONS = $(foreach df,$(wildcard */Dockerfile),$(df:%/Dockerfile=%))

all: build

build: $(VERSIONS)

release: $(VERSIONS)
	docker push ${NAME}

update:
	docker run --rm -v $$(pwd):/work -w /work buildpack-deps ./update.sh

branches:
	git fetch $(REPO) master
	@$(foreach tag, $(VERSIONS), git branch -f $(tag) FETCH_HEAD;)
	@$(foreach tag, $(VERSIONS), git push $(REPO) $(tag);)
	@$(foreach tag, $(VERSIONS), git branch -D $(tag);)

.PHONY: all build library $(VERSIONS)
$(VERSIONS):
	docker build --rm -t $(NAME):$@ $@
