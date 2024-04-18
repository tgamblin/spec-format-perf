# Spec Performance

This is a little benchmark for testing `Spec.format()` performance in Spack.

What it does:

1. Read in a JSON file full of all the specs and format strings used in a single solve of `hdf5`.
2. Run `Spec.format()` as for every pair of arguments.
3. Output timings.

There are around 29,000 specs formatted in each solve.
