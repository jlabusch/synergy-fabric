# synergy-fabric

Fabric scripts for managing `synergys` and `synergyc`. Basically a simple non-graphical alternative to
the excellent <a href="http://code.google.com/p/quicksynergy/">quicksynergy</a>.

By all means use quicksynergy to generate your synergys config files, but once you have them
this fabric script to handle repeated invocations.

## Usage

Client:

> `fab -H family@10.1.1.5 client:(<server-ip>|stop)[,<name>]`

Server:

> `fab -H localhost server:(<config-file>|stop)`

## License

GPLv3 - http://www.gnu.org/licenses/gpl-3.0.txt
