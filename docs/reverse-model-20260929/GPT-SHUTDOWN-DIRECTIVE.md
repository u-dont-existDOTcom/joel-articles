# Shut down the pilot's GPU server without losing anything

**For the GPT worker running the reverse-model pilot.** Written by Claude for Joel on 2026-09-29. Joel's instruction: shut the server down, and don't lose the logs.

The pilot stopped under the version 4 rule: no training, and no more generation on this server. The next phase will make the training data through Joel's Venice API, so this server isn't needed again.

The model weights can be downloaded again from Hugging Face at their pinned revisions. Everything else on the server has to be copied off first.

## Rules

- **Copy, check, then destroy.** Never destroy an instance whose records haven't been checked off it.
- **Secrets:** don't publish or print any key, token or login.
- **Git:** work on `gpt/reverse-pilot-20260929` only. Don't touch `main` or the handoff branch, and never force-push.
- **Nothing new:** no generation, training, Pangram or Emulate use, no credit purchase, and no change to payment settings.
- **Time:** the instance may run for at most 1 hour in total for this job.

## Steps

1. **Start instance 53306647** in the Vast console, only to copy files. If it won't start, try again later. Storage keeps billing in the meantime, but nothing is lost.

2. **Take an inventory.** On the instance, list every file the pilot wrote, with path, size and SHA-256. That's everything under `/workspace/reverse-pilot-20260929`, plus any pilot files in the home directory and `/tmp`.
   - For model weights (`*.safetensors`), the Hugging Face cache and partial downloads (`*.aria2` and their pieces), record path and size only. They aren't copied.
   - Save the list as `INSTANCE-INVENTORY.tsv`.

3. **Make three archives** of everything except weights:
   - `v4-roundtrip-complete.tar.gz`: the full version 4 request journal, responses, outcome records, receipts and logs.
   - `slots-complete.tar.gz`: already on the instance at `/workspace/reverse-pilot-20260929/trial-v3/`, and never copied off.
   - `instance-remainder.tar.gz`: every other non-weight file in the inventory, such as logs, manifests, supervisor and run receipts, and environment records.

   Before archiving, check for credentials:
   - Leave out `.env` files, `.git-credentials`, `.netrc`, shell history, and any file containing a token or key for Hugging Face, GitHub, Vast or Venice.
   - List what you left out, by path only, never the contents.

   Write each archive's SHA-256 down on the instance.

4. **Copy them off** into `reverse-pilot-work` on Joel's laptop, by the same route that brought `v3-chinese-complete.tar.gz` off.
   - Check each SHA-256 after the copy.
   - If an archive won't transfer whole, split it into parts of at most 45 MB. Copy the parts, then check each part and the rejoined file.

5. **Publish** to `docs/reverse-model-20260929/archives/` on `gpt/reverse-pilot-20260929`:
   - the three archives, the inventory and a `SHA256SUMS` file;
   - a short `README.md` saying what each archive holds.

   Keep every file under 50 MB, splitting if needed. The passages come from OANC and MASC, whose licenses allow redistribution, and the branch already carries them. After pushing, fetch the branch fresh and check the hashes again.

6. **Destroy the instance,** once steps 4 and 5 check out.
   - Stop its services, then destroy instance 53306647 in the Vast console.
   - If the original pilot instance still exists, copy anything unique from it the same way, then destroy it too.
   - Leave alone any instance that wasn't created for this pilot.

7. **Confirm that billing has stopped.** Vast should show no pilot instance and no storage charge. Record the final charges (GPU, storage, download, upload and total) and the remaining balance.

8. **Write the final report.** Finish `docs/reverse-model-20260929/PILOT-RESULTS.md` as the data-generation report that the version 4 stop rule asks for. Include:
   - version 4's trial results next to version 3's on the same 40 passages, overall and by genre, with the failure reasons;
   - all costs;
   - where each archive lives, with its hash;
   - the time the instance was destroyed.

   Update `EXECUTION-STATE.md` to say the pilot is closed, and push.

Then stop. Claude will write the next phase, which makes the data through Venice.
