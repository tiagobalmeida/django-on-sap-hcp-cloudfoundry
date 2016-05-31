# Cloud Foundry Django sample app: Tasks

This is a basic Python Django app designed to run on a cloud foundry python buildpack.
It allows the user to store tasks and display all tasks. Requires a postgresql service.
*It is not an example of good django project structure or best practices* but to test the platform.

Example to push the app.

```bash
~/bin/cf/cf push -n cfdjango3
```
