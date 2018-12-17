# Shell to use with Make
SHELL := /bin/bash
BOLD := \033[1m
MAIN := server.py
ROOT := ./
BACK := ../
DIR_P := Redes/
DIR_PATH := Redes/proyecto02/server_pokemon
DIR := server_pokemon/
DB := DB/
# Set important Paths
PROJECT_GIT := git@github.com:Ferch2109/Redes.git

install:
	git clone $(PROJECT_GIT)
	cp -r $(DIR_PATH) $(ROOT)
	rm -rf $(DIR_P)
	cd $(DIR) &&  echo -e "$(BOLD)installing $(DIR) $(shell python setup.py --version)"
	mkdir "$(DIR)$(DIR)$(DB)POKEDEX"
	echo -e "$(BOLD) Successfully installed.\n Name of directory: $(DIR)"
	rm "Makefile"

help:
	@echo "Makefile rules:"
	@echo "  help      - This."
	@echo "  run      - Run main program."
	@echo "  install   - Install packages and create necessary directories."
	@echo "  uninstall - Delete the app."
	@echo "  clean     - Delete cache."

run:
	python $(DIR)$(MAIN)
# Clean build files
uninstall:
	cd $(BACK) && rm -rf $(DIR)

# Clean build files
clean:
	rm -rf "$(DIR)$(DB)POKEDEX/"
	mkdir "$(DIR)$(DB)POKEDEX"
	cd $(BACK)
