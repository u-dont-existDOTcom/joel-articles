# Reverse-model pilot instance records

These are the nonweight records recovered from Vast pilot instance `53306647` under the handoff shutdown directive at `b529de83bb9298a2f2c7ff8e65231c0ad9b905c1`.

| Archive | Contents | SHA-256 of complete archive |
|---|---|---|
| `v4-roundtrip-complete.tar.gz` | Version 4 request journal, reservations, responses, trial outcomes, summary, manifest and log | `46f7d033d04165d0903500fc8dca6df148edfbf6a34a8d7f2e7209f3d426d976` |
| `slots-complete.tar.gz` | Version 3 English-slot fallback trial records | `04ae558bf9e9ad31c4e63a012f8df79e78e454641405a79954f2e64c77aa1665` |
| `instance-remainder.tar.gz.part001`–`part014` | Every other inventoried nonweight pilot file, split into parts below 50 MB | `e47c1c0906ad6a9726d6192a8060ee562610181df61a2546f3d888fa819b95ea` after joining |

`INSTANCE-INVENTORY.tsv` lists pilot paths, sizes, SHA-256 hashes and archive classifications. Hugging Face model weights, cache files and partial downloads are listed by path and size only and can be downloaded again at their pinned revisions. `EXCLUDED-CREDENTIAL-PATHS.txt` names excluded credential paths without their contents. `SHA256SUMS` contains hashes for each published file and the complete remainder archive.

To verify the published files, run `sha256sum -c SHA256SUMS` after joining the parts; the two small archives appear twice in that list because the source manifest records both original archives and published files. Join the large archive with `cat instance-remainder.tar.gz.part* > instance-remainder.tar.gz`, then verify the complete hash above. Do not commit the joined archive because it exceeds the branch's 50 MB per-file limit.
