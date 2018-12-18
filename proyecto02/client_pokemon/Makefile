# Shell to use with Make
SHELL := /bin/bash
BOLD := \033[1m
EXC_PATH := client_pokemon/
EXC := ./client.py
ROOT := ./
BACK := ../
DIR_P = Redes/
DIR_PATH = Redes/proyecto02/client_pokemon
DIR = client_pokemon/
# Set important Paths
PROJECT_GIT := https://github.com/Ferch2109/Redes.git

install:
	git clone $(PROJECT_GIT)
	cp -r $(DIR_PATH) $(ROOT)
	rm -rf $(DIR_P)
	cd $(DIR) &&  echo -e "$(BOLD)installing $(DIR) $(shell python setup.py --version)"
	echo -e "$(BOLD) Successfully installed.\n Name of directory: $(DIR)"
	rm "Makefile"

help:
	@echo "Makefile rules:"
	@echo "  help      - This."
	@echo "  run       - Run client app."
	@echo "  install   - Install packages and create necessary directories."
	@echo "  uninstall - Delete the app."
	@echo "  clean     - Delete cache."

run:
	cd $(EXC_PATH) && $(EXC)
# Clean build files
uninstall:
	cd $(BACK) && rm -rf $(DIR)

# Clean build files
clean:
	rm -rf "$(DIR)POKEDEX/"
	mkdir "$(DIR)POKEDEX/"
	cd $(BACK)
