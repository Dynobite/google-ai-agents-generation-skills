## Reconciling IDE Friction with CI/CD Enforcement

To catch these structural flaws, we must balance developer velocity with strict security enforcement. Attempting to aggressively hard-block insecure prompts directly within the developer's IDE is easily bypassed and can cause excessive friction for benign developers trying to iterate on complex logic.

Instead, "shifting left" should be implemented via Developer Advisory Linters in the IDE to provide real-time guidance, while the unyielding security enforcement is pushed to deterministic checks within the CI/CD pipeline. Integrating Static Application Security Testing

(SAST) and Software Composition Analysis (SCA) into the pipeline ensures that all generated application logic is deterministically scanned for vulnerable dependencies and structural flaws before the code ever reaches production.
