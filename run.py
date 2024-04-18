#!/usr/bin/env spack-python

import json
from spack.util.timer import Timer
from spack.spec import Spec

timer = Timer()

timer.start("load")
with open("spec_list.json") as f:
    specs = json.load(f)
timer.stop("load")

timer.start("parse")
concrete_spec_list = []
spec_list = []
for record in specs:
    if record["concrete"]:
        spec = Spec.from_json(record["spec"])
    else:
        try:
            spec = Spec(record["spec"])
        except Exception as e:
            # some problem with '[virtuals=openmpi] foo'
            spec = Spec("^" + record["spec"])

    spec_list.append((spec, record["format"]))
timer.stop("parse")

timer.start("format")
for i in range(10):
    for spec, fmt in spec_list:
        spec.format(fmt)
timer.stop("format")

print(f"Processed {len(spec_list)} specs")
timer.write_tty()
