NAME=sw_chapter_python_simple
VERSION=1.0.0
DOCKER_NAME_FULL=worldsensing/$(NAME):$(VERSION)

clean:
	@find . -iname "*~" | xargs rm 2>/dev/null || true
	@find . -iname "*.pyc" | xargs rm 2>/dev/null || true
	@find . -iname "build" | xargs rm -rf 2>/dev/null || true

build: clean
	docker build -t $(DOCKER_NAME_FULL) .

run: build
	docker run -it \
	    --volume ${PWD}:/tmp \
		--name $(NAME) \
		--rm $(DOCKER_NAME_FULL)

run-compose:
	docker-compose build
	docker-compose up