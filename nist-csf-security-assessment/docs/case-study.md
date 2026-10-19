# Case Study: Security Assessment and Hardening for a Simulated Industrial Supplier

**Author:** Noah Tongen  
**Environment:** Simulated engagement. "Techcorp" (client) and "Cyberworks" (consultant) are fictional.  
**Framework:** NIST Cybersecurity Framework · **Method:** Waterfall · **Dates:** Aug 1-19, 2025

## 1. Problem
Techcorp, an industrial equipment supplier, suffered several data breaches that exposed customer PII, causing reputational harm, lost client trust and potential financial penalties. The infrastructure was outdated and had no intrusion detection, encryption or MFA. Employees had no security awareness training, which left them open to phishing and social engineering.

## 2. Approach
The work ran in six waterfall phases, each finishing before the next began, mapped to the NIST CSF functions (Identify, Protect, Detect, Respond, Recover).

| NIST CSF function | Work performed |
|---|---|
| Identify | Security audit, gap analysis against NIST guidance, NIST SP 800-30 risk assessment with risk matrix, baseline metrics |
| Protect | OS updates and patching, BitLocker and SQL TDE (AES-256), Entra ID MFA, badge system with role-based access, time-of-day restrictions, awareness training |
| Detect | IDS, SIEM with dashboards and alerts, DLP, CCTV |
| Respond | Incident response runbooks, escalation chain |
| Recover | Phishing simulations, lessons-learned review, penetration test to verify controls before handoff |

**Why NIST CSF + waterfall:** the CSF's sequence parallels an incident response workflow, and waterfall's finish-to-start phases match it. The usual waterfall drawback, costly late changes, was reduced by running the audit and pentest first and scoping the rest of the work around the findings.

## 3. Key design decisions and sources
- **Social engineering focus.** The Verizon DBIR and SANS Security Awareness Report both show the human element driving most breaches, so the training program targeted phishing and social engineering, safe handling of sensitive data, reporting suspicious activity, and physical workstation habits.
- **Zero trust principles.** CISA's Zero Trust Maturity Model guided least-privilege role-based access, phishing-resistant MFA, and encryption of data at rest, especially on the database holding customer data.
- **Risk-driven prioritization.** NIST SP 800-30 drove the risk assessment. The top risk was financial and reputational loss from another breach.
- **SIEM for faster response.** Gartner's SIEM research supported aggregating feeds in one place to detect and investigate threats consistently.
- **Cost context.** IBM's Cost of a Data Breach report (2024) cites a $4.88M average breach cost and shows MFA and encryption reduce losses. This is an industry figure, not a result of this project.

## 4. Implementation highlights
**Vulnerability remediation.** A vulnerability scanner identified missing patches and outdated operating systems. Updates were applied after hours to protect uptime. Each system was rebooted and tested, then re-scanned to confirm no critical vulnerabilities remained. Audit logs showed 100% of systems patched and were cross-checked by the client.

**Encryption.** BitLocker (AES-256) on Windows devices, chosen for its Active Directory integration. Transparent Data Encryption (AES-256) on SQL Server databases, which needs minimal environment change. Verification used T-SQL queries (see [`encryption/`](../encryption/)) and PowerShell status checks. All three databases (InventoryDB, CustomersDB, OrdersDB) showed encryption state 3 with AES-256.

**MFA.** Microsoft Entra ID with Microsoft Authenticator, enforced by policy for all users, systems and applications, so no one had an easier path in. Rolled out early in the infrastructure phase and fully verified by handoff.

**Physical security.** Badge system, locks and CCTV, with role-based access ([`physical-security/`](../physical-security/)) and time-of-day restrictions.

**Detection and response.** IDS and SIEM deployment, plus incident response runbooks and an escalation chain for incidents beyond the response team's scope.

**Awareness.** Training sessions with completion reporting (100% completion) and simulated phishing to test effectiveness.

## 5. Timeline

| Milestone | Planned | Actual |
|---|---|---|
| Security audit and risk assessment | Aug 1-3 | Aug 1-3 |
| Technical infrastructure updates | Aug 4-8 | Aug 4-6 (2 days early) |
| IDS, SIEM and DLP deployment | Aug 9-12 | Aug 7-10 |
| Physical security deployment | Aug 13-15 | Aug 11-13 |
| Employee training program | Aug 16-18 | Aug 14-16 |
| SQL injection remediation (unplanned) | n/a | Aug 17-18 |
| Go-live and handoff | Aug 19 | Aug 19 |

See [`lessons-learned/sql-injection-scope-creep.md`](../lessons-learned/sql-injection-scope-creep.md) for the unplanned work.

## 6. Results
- **Detection:** across 20 simulated incidents, mean time to detect fell from **1,112 minutes (18.5 hours) to 15.1 minutes**, a 98.6% reduction. Before the changes, 5 of 20 incidents took a day or more, and the longest took 7,200 minutes (5 days). The median before was 46 minutes, so the average was driven by the long outliers. Data and script: [`detection/`](../detection/).
- **Vulnerabilities:** re-scans after patching showed no unaddressed critical vulnerabilities; audit logs showed 100% patch coverage.
- **Encryption and MFA:** deployed across all in-scope systems, verified with queries and status checks.
- **Training:** 100% employee completion.
- **Schedule:** handoff delivered on the original date despite the unplanned remediation.

## 7. Limitations
- This was a simulated environment; the detection incidents were simulated, not real attacks.
- MTTD is a mean over only 20 incidents, so it is directional, not statistically conclusive.
- Phishing simulation results are not published here.

## References
- Cybersecurity and Infrastructure Security Agency. (2023). *Zero Trust Maturity Model* (Version 2.0). https://www.cisa.gov/zero-trust-maturity-model
- National Institute of Standards and Technology. (2012). *Guide for Conducting Risk Assessments* (SP 800-30 Rev. 1). https://doi.org/10.6028/NIST.SP.800-30r1
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (CSWP 29). https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
- Spitzner, L. (2025). *SANS 2025 Security Awareness Report: Embedding a Strong Security Culture*. SANS Institute. https://www.sans.org/white-papers/sans-2025-security-awareness-report
- IBM & Ponemon Institute. (2024). *Cost of a Data Breach Report 2024*. IBM.
- Verizon. (2025). *Data Breach Investigations Report*.
- Gartner. (2022). *Critical Capabilities for Security Information and Event Management*.
