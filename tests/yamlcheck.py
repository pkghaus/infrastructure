#!/usr/bin/env python3
"""Parse YAML with a loader that rejects duplicate mapping keys.

PyYAML's safe_load takes the last of a repeated key and says nothing. That is
benign in most files and dangerous in these: octodns and octorules treat state
absent from the repo as a deletion, so a key silently swallowed by its twin is
a record removed from the live zone on the next deploy. Since DNSSEC went live
on 2026-09-03 the result of a wrong DNS deploy is a SERVFAIL rather than a
wrong answer, which raises the cost of exactly this failure.

The plan-on-PR would show such a deletion, so a reviewer reading the plan
comment is the other safety net. This one does not need a reviewer to notice.

Copied from pkghaus/buildinfos tests/yamlcheck.py. It is a copy rather than a
shared dependency because there is no public home the estate's repos can share
code through; the file is small and stable enough for that to be the cheaper
trade.
"""
import sys

import yaml


class StrictLoader(yaml.SafeLoader):
    pass


def no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(f"duplicate key: {key!r}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, no_duplicates
)

status = 0
for path in sys.argv[1:]:
    try:
        with open(path, "rb") as handle:
            yaml.load(handle, StrictLoader)
    except (ValueError, yaml.YAMLError) as exc:
        print(f"FAIL {path}: {exc}", file=sys.stderr)
        status = 1
    else:
        print(f"ok   {path}")
sys.exit(status)
