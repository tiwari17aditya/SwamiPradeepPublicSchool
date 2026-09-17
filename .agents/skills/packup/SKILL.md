---
name: packup
description: >-
  Handles end-of-session project wrap-up when the user invokes /packup or asks to pack up:
  updates all documentation, stages and pushes changes to Git, verifies working tree cleanliness,
  runs utility health checks, and concludes with an inspiring proverb.
---

# Packup Workflow Runbook (/packup)

When the user types `/packup` or requests to pack up / wrap up the session, perform the following steps autonomously:

## Step 1: Documentation & Ledger Audit
1. Audit and update all project documentation:
   - `Digitalizing_Papers/README.md`: Ensure latest features, usage commands, and configs are documented.
   - `Digitalizing_Papers/raw_inputs/README.md`: Ensure input table is up to date.
   - `Digitalizing_Papers/output_pdfs/README.md`: Ensure output table and year/exam hierarchy are accurate.
   - `Digitalizing_Papers/digitized_texts/README.md`: Ensure extracted text catalog is current.

## Step 2: Privacy & Security Check
1. Verify that personal Google Drive paths, tokens, or credentials are NOT tracked by Git:
   - `Digitalizing_Papers/config/drive_config.json` must be in `.gitignore`.
   - Only `Digitalizing_Papers/config/drive_config.example.json` with placeholder values should be committed.
   - Credentials files (`credentials.json`, `token.json`, `*.pyc`) must remain excluded.

## Step 3: Git Commit & Push
1. Check repository status:
   ```bash
   git status
   ```
2. Stage all modified and untracked files that belong in version control:
   ```bash
   git add -A
   ```
3. Commit with a clear, descriptive message summarizing the session's accomplishments.
4. Push to remote:
   ```bash
   git push origin main
   ```
5. Confirm that the working tree is clean (`nothing to commit, working tree clean`).

## Step 4: Run Utility Status Check
Display a quick summary of:
- Repository commit status and latest commit hash.
- Files categorized under each academic session and exam type.
- Google Drive connection status.

## Step 5: Conclude with an Inspiring Proverb
Always conclude the `/packup` report with an inspiring proverb on education, wisdom, or perseverance (e.g., Sanskrit, Hindi, or English school motto), such as:
> *"विद्या ददाति विनयं विनयाद् याति पात्रताम्।"*  
> *(Knowledge bestows humility, from humility comes worthiness, and from worthiness comes success.)*
