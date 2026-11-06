.PHONY: verify check-readme lint package clean

verify:
	python3 scripts/verify-prompts.py

check-readme:
	python3 scripts/check-readme.py

lint:
	npx markdownlint-cli2 "**/*.md" "#node_modules" --config .markdownlint.json

package:
	mkdir -p dist
	zip -r dist/grok-automations-$(shell date +%Y%m%d).zip \
	  01-sourcing-auctions 02-pricing-comps 03-listings-inventory \
	  04-youtube-content 05-social-shortform 06-business-intel \
	  07-weekly-synthesis AGENTS.md README.md NOTION-GROK-PLAYBOOK.md \
	  scripts -x "*/node_modules/*"

clean:
	rm -rf dist
