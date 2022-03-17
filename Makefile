
help:
	@echo "| :: Usage:"
	@echo "| ::    make [help] ......... : generates this message"
	@echo "| ::    make ui ............. : generates the UI"
	@echo "| ::    make lupdate ........ : updates .ts files"
	@echo "| ::    make release ........ : convert .ts files into .qm resources"
	@echo "| ::    make translations ... : run 'make lupdate' and 'make release'"
	@echo "| ::    make run ............ : run application (venv needs to be activated)"
	@echo "| ::    make git ............ : run 'make lupdate' with -no-location, 'make release' and clean a ready to commit"
	@echo "| ::    make clean .......... : remove 'build', 'dist' and '*.pyc' files/directories"

ui:
	@echo "| :: Building UI"
	python setup.py build_res

lupdate:
	@echo "| :: Updating .ts files"
	lupdate app.pro

lupdate_noloc:
	@echo "| :: lupdate -no-location app.pro"
	lupdate -locations none app.pro

release:
	@echo "| :: Generating .qm files"
	lrelease app.pro

translations: lupdate release

git: clean ui lupdate_noloc release

clean:
	@echo "| :: Cleaning up"
	@rm -rfv build/
	@rm -rfv dist/
	@rm -rfv *.pyc

dist:
	@echo "| :: Building distribution"
	python setup.py bdist_app

run:
	@echo "| :: Running application"
	python -m app
