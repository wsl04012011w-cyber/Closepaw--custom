# ClosePaw Custom

Experimental build workspace for a customized ClosePaw Android agent.

## Upstream
This workspace tracks the upstream project at https://github.com/imoonkey/closepaw.
The first CI job builds the upstream `main` as a baseline. Custom changes will be added as small, reviewable patches after the Codex sign-in flow has been inspected.

## Build
GitHub Actions runs a debug build from the upstream source. The resulting APK is an experimental artifact, not a signed production release.

## Important
- Do not commit API keys, OAuth tokens, keystores, passwords, or personal data.
- ChatGPT subscription access and OpenAI API billing are separate. A ChatGPT sign-in flow must be implemented and used according to the provider's supported OAuth/Codex protocol; changing a model label alone does not create entitlement.
- Review app permissions before installing any build.
