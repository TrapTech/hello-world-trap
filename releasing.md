# Making a new release

1. Update CHANGELOG.md, make sure to keep the formatting consistent

2. Create a tag on the `main` branch that adheres to the format: `release/vx.y.z`, where `x.y.z` is the released version (same as in CHANGELOG.md)

3. Push the tag, let GitHub Actions run and create a new release.

4. Edit the release to have a consistent name (remove the `release/` prefix) and include the changelog entry in the release description.
