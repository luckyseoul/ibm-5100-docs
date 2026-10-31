PY ?= python3

.PHONY: all manuals check links fetch verify clean

all: check

manuals:
	$(PY) scripts/render_manuals.py

check: manuals
	$(PY) scripts/linkcheck.py

links:
	$(PY) scripts/linkcheck.py --only links

fetch:
	$(PY) scripts/fetch_manuals.py --dest _archive

verify:
	$(PY) scripts/fetch_manuals.py --dest _archive --verify-only

clean:
	rm -rf _archive __pycache__ scripts/__pycache__
