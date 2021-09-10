FoxyProxy Config Builder
========================

This is a little tool to help programatically manage proxy rules for FoxyProxy.  You pass it a specially crafted YAML descritption and out pops some JSON.  I usually run it like this:

```bash
./buildFoxyProxy.py FoxyProxy.example.yaml | jq '.'
```

to checkout what it looks like, and then

```bash
./buildFoxyProxy.py FoxyProxy.example.yaml > FoxyProxy.json
```

to get a JSON file that you can load in FoxyProxy using "Import Settings". (Just kidding, I usually edit my yaml, forget to backup my settings, load the new json and cry...)


You'll need docopt and ruamel.yaml:

```
pip3 install docopt ruamel.yaml
```
