# cdisc-rules-engine
Open source offering of the cdisc rules engine

### Code formatter
This project uses the `black` code formatter and `flake8` linter for python.
It also uses `pre-commit` to run `black` and `flake8` when you commit.
Both dependencies are added to *requirements.txt*.

**Required**

Setting up `pre-commit` requires one extra step. After installing it you have to run

`pre-commit install`

This installs `pre-commit` in your `.git/hooks` directory.

### Running The Tests
From the root of the project run the following command:

`python -m pytest tests/unit/`
### Running a validation

Clone the repository and run `core.py --help` to see the full list of commands.

Run `core.py validate --help` to see the list of validation options.

```
  -ca, --cache TEXT               Relative path to cache files containing pre
                                  loaded metadata and rules
  -p, --pool-size INTEGER         Number of parallel processes for validation
  -d, --data TEXT                 Path to directory containing data files
  -dp, --dataset-path TEXT        Absolute path to dataset file
  -l, --log-level [info|debug|error|critical|disabled|warn]
                                  Sets log level for engine logs, logs are
                                  disabled by default
  -rt, --report-template TEXT     File path of report template to use for
                                  excel output
  -s, --standard TEXT             CDISC standard to validate against
                                  [required]
  -v, --version TEXT              Standard version to validate against
                                  [required]
  -ct, --controlled-terminology-package TEXT
                                  Controlled terminology package to validate
                                  against, can provide more than one
  -o, --output TEXT               Report output file destination
  -of, --output-format [JSON|XLSX]
                                  Output file format
  -rr, --raw-report               Report in a raw format as it is generated by
                                  the engine. This flag must be used only with
                                  --output-format JSON.
  -dv, --define-version TEXT      Define-XML version used for validation
  --whodrug TEXT                  Path to directory with WHODrug dictionary
                                  files
  --meddra TEXT                   Path to directory with MedDRA dictionary
                                  files
  --disable-progressbar           Disable progress bar
  -r, --rules TEXT
  -vo, --verbose-output           Specify this option to print rules as they
                                  are completed
  --help                          Show this message and exit.

```

#### Validate folder
To validate a folder using rules for SDTM-IG version 3.4 use the following command:

`python core.py validate -s sdtmig -v 3-4 -d path/to/datasets`

#### Additional Core Commands

* update-cache - update locally stored cache data (Requires an environment variable - `CDISC_LIBRARY_API_KEY`)
    * python core.py update-cache`

* list-rules - list rules available in the cache

    * list all rules:

    `python core.py list-rules`

    * list rules for standard:

    `python core.py list-rules -s sdtmig -v 3-4`

* list-rule-sets - lists all standards and versions for which rules are available:
    `python core.py list-rule-sets`

### Creating an executable version

**Linux**

`pyinstaller core.py --add-data=venv/lib/python3.9/site-packages/xmlschema/schemas:xmlschema/schemas --add-data=resources/cache:resources/cache --add-data=resources/templates:resources/templates`

**Windows**

`pyinstaller core.py --add-data=".venv/Lib/site-packages/xmlschema/schemas;xmlschema/schemas" --add-data="resources/cache;resources/cache" --add-data="resources/templates;resources/templates"`

_Note .venv should be replaced with path to python installation or virtual environment_

This will create an executable version in the `dist` folder. The version does not require having Python installed and
can be launched by running `core` script with all necessary CLI arguments.

### Creating .whl file

All non-python files should be listed in `MANIFEST.in` to be included in the distribution.
Files must be in python package.

**Unix/MacOS**

`python3 -m pip install --upgrade build`
`python3 -m build`

To install from dist folder
`pip3 install {path_to_file}/cdisc_rules_engine-{version}-py3-none-any.whl`

To upload built distributive to pypi

`python3 -m pip install --upgrade twine`
`python3 -m twine upload --repository {repository_name} dist/*`

**Windows(Untested)**

`py -m pip install --upgrade build`
`py -m build`

To install from dist folder
`pip install {path_to_file}/cdisc_rules_engine-{version}-py3-none-any.whl`

To upload built distributive to pypi

`py -m pip install --upgrade twine`
`py -m twine upload --repository {repository_name} dist/*`
