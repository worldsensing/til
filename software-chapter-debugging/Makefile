DOCKER_NAME=worldsensing/sw_chapter_debugging
VERSION=1.0.0
NAME=sw_chapter_debugging
DOCKER_NAME_FULL=$(DOCKER_NAME):$(VERSION)


clean:
	@find . -iname "*~" | xargs rm 2>/dev/null || true
	@find . -iname "*.pyc" | xargs rm 2>/dev/null || true
	@find . -iname "build" | xargs rm -rf 2>/dev/null || true

build: clean
	@cp ~/.netrc .
	docker build -t $(DOCKER_NAME_FULL) .
	@rm .netrc

stop:

run: build
	docker run -it \
		--name $(NAME) \
		--rm $(DOCKER_NAME_FULL)

publish: build
	@docker push $(DOCKER_NAME_FULL)

setup:
	@docker-compose -f docker-compose.yml -p sw_chapter_debugging up -d

