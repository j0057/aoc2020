# Advent of Code 2020

## Setting up the python environment

I tested this on Python 3.8, and try to make liberal use of the latest and
greatest features, so it won't work on anything older.

If you use `direnv`, whitelist the `.envrc`; if you don't, source the
environment variables manually:

    . .envrc

This sets `$PYTHONUSERBASE`, causing everything to be installed into the `env`
directory. No `virtualenv` magic needed!

Install pip and friends into `env`:

    python3 -m ensurepip

Install the requirements:

    pip3 install -r requirements.txt

## Running the python tests

Running all tests, showing the 10 slowest:

    pytest --durations 10

Watch for changes, run only day 13:

    pytest-watch -c -- -vk day13

Do check out pytest's other 1000 cool features with `pytest --help`.
