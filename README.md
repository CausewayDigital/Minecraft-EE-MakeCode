# Minecraft-EE-MakeCode
A collection of Microsoft MakeCode tutorials created by Causeway Digital

## Creating a Release
When a commit that updates the tutorial's `.md` file or `pxt.json` Github will automatically create a release, incrementing the *patch* number.

## Scripts

### Generate PXT
Generates the `pxt.json` file for Makecode.

**This is automatically ran when a change is made the the tutorials by Github actions**

```shell
python3 scripts/generate-pxt.py
```

#### Ignoring `.md` files in `tutorials` dir

If there's a file you **don't** want add to `pxt.json["files"]` you can add it to `config/ignore.json` into the `ignoredFiles` array as it would appear in the `pxt.json` file.

#### Editing base `pxt.json`
Any hand edits to the `pxt.json` file should be done in `scripts/config/base-pxt.json`.