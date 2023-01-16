# hello-world-trap

This is a basic TrapInit trap that showcases the basic functionalities of a trap: alerts, incidents and baits.

You can run it using the TrapInit application (downloadable [here](https://downloads.traptech.pl)).

You can download the actual trap definition from the [releases](https://github.com/TrapTech/hello-world-trap/releases) or from [downloads.traptech.pl](https://downloads.traptech.pl).

## Building

To build this trap locally, you need the following installed (on a Linux system or WSL2):

- Docker - since TrapInit traps are based on Docker images

- `zip`

- `curl`

Then, just run the `build.sh` script, which will build the trap into the `hello-world-trap.zip` file.

You can also download a build of this trap from any commit from the [actions](https://github.com/TrapTech/hello-world-trap/actions) tab. Note that the downloaded
result will be double-zipped, so you need to unpack the download file before uploading it to TrapInit.
