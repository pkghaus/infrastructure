# infrastructure

Infrastructure-as-code for pkg.haus. Everything about the zone lives here;
nothing is changed by hand in the Cloudflare dashboard or via ad-hoc API calls.

| Concern | Tool | Config | State |
| --- | --- | --- | --- |
| DNS records | [octodns](https://github.com/octodns/octodns) | `octodns.yaml` | `dns/<zone>.yaml` |
| WAF / rulesets / zone security | [octorules](https://github.com/barnumbirr/octorules) | `octorules.yaml` | `waf/<zone>.yaml` |

Both tools own their scope completely: a record or rule absent from this
repository is removed on deploy. Pull requests get a plan posted as a comment;
merges to `master` deploy.

## License

Apache-2.0. See [LICENSE](LICENSE).
