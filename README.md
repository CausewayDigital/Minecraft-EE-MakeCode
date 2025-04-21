# Minecraft-EE-MakeCode
A collection of Microsoft MakeCode tutorials created by Causeway Digital

# Scripts
This repo contains a number of scripts for helping with development

## Generate PXT

Generates the `pxt.json` file for Makecode

```shell
python3 scripts/generate-pxt.py
```

### Ignoring `.md` files in `tutorials` dir

If there's a file you want to not be added to the `pxt.json["files"]` you can add it to `config/ignore.json` into the `ignoredFiles` array as it would appear in the `pxt.json` file.