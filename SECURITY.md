# Security Policy — LAB AI OS

This document describes how to report security issues and the project's security practices.

## Supported Versions

We support the latest stable release and the previous minor release for critical security fixes. See the CHANGELOG.md for version history.

## Reporting Vulnerabilities

If you discover a security vulnerability, please report it privately to the project security team at security@labaios.org. Include:

- Affected component and version
- Detailed steps to reproduce
- Impact assessment and any suggested mitigations

Do not open public issues for vulnerabilities.

## Security Policy

- The project prioritizes fixes for vulnerabilities that enable remote code execution, privilege escalation, data exfiltration, or bypass of authentication/authorization.
- Security patches are coordinated and released with appropriate advisories and, when relevant, backported to supported versions.

## Responsible Disclosure

We appreciate responsible disclosure. Upon receiving a valid report, the security team will:

1. Acknowledge receipt within 48 hours.
2. Triage and reproduce the issue.
3. Collaborate with maintainers to create a remediation plan.
4. Coordinate public disclosure once a fix and release are available.

## Response Timeline

- Acknowledgement: within 48 hours
- Initial triage: within 7 business days
- Patch release: timeline depends on severity; high-severity issues targeted for expedited patches.

## Security Best Practices

- Do not commit secrets (API keys, passwords) to the repository.
- Use environment variables or secret management systems for sensitive configuration.
- Run dependency scanners and keep third-party dependencies up to date.
- Enforce least privilege for worker runtimes and connectors.
- Log security-relevant events to audit systems (without logging secrets in plaintext).

For urgent or sensitive reports where email is not suitable, maintainers may provide alternative secure channels upon initial contact.