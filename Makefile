VERSION = 0.0.1

help:
	@echo "| :: Usage:"
	@echo "| ::    make ........... : generates this message"
	@echo "| ::    make lupdate ... : updates .ts files"
	@echo "| ::    make release ... : convert .ts files into .qm resources"
	@echo "| ::    make build ..... : run 'make lupdate' and 'make release'"
	@echo "| ::    make run ....... : run application (venv needs to be activated)"
	@echo "| ::    make git ....... : run 'make lupdate' with -no-location, 'make release' and clean a ready to commit"
	@echo "| ::    make clean ..... : "
	@echo "| :: Version: $(VERSION)"

lupdate:
	lupdate app.pro

lupdate_noloc:
	lupdate -locations none app.pro

release:
	lrelease app.pro

build: res release

git: clean lupdate_noloc release

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.pyc

run:
	python -m app
