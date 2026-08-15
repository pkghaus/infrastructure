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

```
Copyright 2026 pkg.haus

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## Buy us a coffee?

If you feel like buying us a coffee (or a beer?), donations are welcome:

```
BTC : bc1qq04jnuqqavpccfptmddqjkg7cuspy3new4sxq9
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
ETH : 0x2238A11856428b72E80D70Be8666729497059d95
LTC : MQwXsBrArLRHQzwQZAjJPNrxGS1uNDDKX6
```
