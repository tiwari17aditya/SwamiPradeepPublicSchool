# Antigravity Agent Guidelines for Swami Pradeep Public School

## Slash Commands & Workflows

### `/packup`
Whenever the user invokes `/packup` or asks to wrap up the session:
1. **Audit Documentation**: Ensure `README.md` and all tabular ledgers in `raw_inputs/`, `output_pdfs/`, and `digitized_texts/` are updated.
2. **Privacy Audit**: Verify that `config/drive_config.json` is not tracked in Git and `.gitignore` protects credentials and personal paths.
3. **Git Commit & Push**: Run `git add -A`, commit changes with a comprehensive summary, and push to `origin main`.
4. **Utility Check**: Run `python Digitalizing_Papers/utilities.py --status` to display a clean summary of project files and Google Drive sync status.
5. **Inspiring Proverb**: Always conclude the `/packup` response with a meaningful and inspiring proverb related to education, teaching, or wisdom.

---

## Security & Path Isolation Rules
- Never commit absolute local filesystem paths (e.g. `G:\My Drive\...` or `C:\Users\...`).
- Always keep `config/drive_config.json` untracked and provide `config/drive_config.example.json` with placeholders.
- Sample inputs and outputs must remain in `Digitalizing_Papers/sample/` to keep `raw_inputs/` and `output_pdfs/` clean for live production runs.
