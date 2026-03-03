# CISSP Study Guide

A comprehensive overview of the CISSP exam, its eight domains, and exam format. Use this as your roadmap for what to study.

---

## CISSP Overview

### What is CISSP?

**CISSP** = **Certified Information Systems Security Professional**, issued by **ISC2** (International Information Systems Security Certification Consortium).

- **One of the most respected security certifications** in the industry
- Required by many government contractors, Fortune 500 companies, and security leaders
- Requires both **exam passing** AND **5 years of security experience** (or 4 years with a related degree)

### The Exam

| Attribute | Detail |
|-----------|--------|
| **Duration** | 3 hours |
| **Questions** | 125 multiple-choice |
| **Passing Score** | ~70% (100-800 scale; varies slightly by administration) |
| **Cost** | ~$750 USD |
| **Retakes** | $475 (if you don't pass) |
| **Format** | Computer-based testing (Pearson VUE proctored) |
| **Frequency** | Year-round (multiple test dates) |

### Exam Structure

All questions are **multiple choice** (A, B, C, D). No essay, no practicum, no hands-on component.

**Important**: The exam uses **adaptive testing**. If you answer questions correctly, they get harder. If you struggle, easier questions appear. This means difficulty varies by test-taker and even by question (no two tests are identical).

---

## The 8 CISSP Domains

The exam covers **8 domains** with specific weights. Know these inside and out.

### Domain 1: Security and Risk Management (15% — 18-19 questions)

**What it covers**: Governance, risk management frameworks, compliance, ethics, security policies, and strategic decision-making.

**Key topics**:
- Security governance (IT governance, InfoSec governance)
- Risk management process (identification, analysis, response, monitoring)
- Risk models and frameworks (NIST, ISO 27001, COBIT)
- Compliance and legal/regulatory frameworks (GDPR, HIPAA, PCI-DSS, SOX)
- Business continuity and disaster recovery planning
- Security policies, standards, and procedures
- Organizational structures and responsibility models

**Memory hook**: "Risk = Threat × Vulnerability × Asset Value. Manage all three."

**Why it matters**: This is the **strategy** domain. Without good governance, nothing else matters.

---

### Domain 2: Asset Security (10% — 12-13 questions)

**What it covers**: Data classification, handling, storage, lifecycle, and physical security.

**Key topics**:
- Data classification schemes (public, internal, confidential, restricted)
- Data handling throughout its lifecycle (collection, processing, storage, transmission, disposal)
- Data retention policies and secure deletion methods
- Media protection and storage security
- Privacy and data residency requirements
- Physical security (access controls, environmental controls)

**Memory hook**: "Classify early, handle carefully, delete securely."

**Why it matters**: Most breaches result from poor data handling, not sophisticated attacks.

---

### Domain 3: Security Architecture and Engineering (12% — 15 questions)

**What it covers**: Cryptography, secure system design, architectural patterns, and security controls.

**Key topics**:
- Cryptography fundamentals (symmetric, asymmetric, hashing)
- Cryptographic systems (AES, RSA, ECC, SHA)
- Key management and PKI (certificates, CAs, trust models)
- Design principles (least privilege, defense in depth, fail-safe defaults, separation of duties)
- Secure design patterns (zero trust, defense in depth, implicit deny)
- Security mechanisms (firewalls, IDS/IPS, proxies)
- Enterprise architecture and integration security
- System resilience and redundancy

**Memory hook**: "Crypto is math. AES = strong, RSA = keys, SHA = fingerprints. Design for least privilege and defense in depth."

**Why it matters**: This domain tests your understanding of **how** to build secure systems, not just what tools to use.

---

### Domain 4: Communication and Network Security (14% — 17-18 questions)

**What it covers**: Network protocols, secure communication, transmission security, and OSI model application.

**Key topics**:
- OSI model and network protocols (TCP/IP, DNS, DHCP, HTTP/HTTPS)
- Network security protocols (TLS/SSL, IPsec, SSH, VPN)
- Secure communications and transmission (encryption in transit)
- Network access controls (firewalls, ACLs, segmentation)
- Wireless security (WPA2, WPA3, 802.1X)
- Voice and video security (VoIP security)
- Email security (S/MIME, SPF, DKIM, DMARC)
- Network attack types and mitigation (DoS, MitM, spoofing)

**Memory hook**: "TLS = HTTPS (web). IPsec = VPN (tunnels). SSH = remote access. WPA3 = newest wireless standard."

**Why it matters**: Networks are the attack surface; secure communication is foundational.

---

### Domain 5: Identity and Access Management (13% — 16-17 questions)

**What it covers**: Authentication, authorization, access control models, and identity governance.

**Key topics**:
- Authentication methods (something you know, have, are, do)
- Multi-factor authentication (MFA, 2FA)
- Authorization models (DAC, MAC, RBAC, ABAC)
- Single sign-on (SSO) and federation (SAML, OAuth, OpenID Connect)
- Identity and access management (IAM) platforms
- Privilege access management (PAM)
- Account management (provisioning, deprovisioning, lifecycle)
- Non-repudiation and digital signatures

**Memory hook**: "Authentication = are you who you claim? Authorization = what can you access? OAuth = login, SAML = SSO enterprise."

**Why it matters**: Every breach starts with compromised credentials; strong IAM is your first defense.

---

### Domain 6: Security Assessment and Testing (12% — 15 questions)

**What it covers**: Vulnerability assessment, penetration testing, security testing methodologies, and audit.

**Key topics**:
- Vulnerability assessments (scanning, classification, prioritization)
- Penetration testing (methodology, rules of engagement, scope)
- Security testing types (black-box, white-box, gray-box)
- Test coverage and metrics
- Code review and software testing
- Control testing and compliance validation
- Auditing and audit trails
- Test results interpretation and remediation

**Memory hook**: "Vulnerability assessment = find weaknesses. Penetration testing = exploit them (with permission). Both are essential."

**Why it matters**: You can't fix what you don't measure. Assessment is how you know if your security works.

---

### Domain 7: Security Operations (16% — 20-21 questions) ⭐

**What it covers**: Incident response, logging, monitoring, threat detection, and day-to-day security operations. **This is the largest domain on the exam.**

**Key topics**:
- Incident management and response (detection, containment, eradication, recovery, lessons learned)
- Logging, monitoring, and alerting
- SIEM (Security Information and Event Management)
- Threat intelligence and threat hunting
- Vulnerability management
- Patch and configuration management
- Change management
- Recovery and backup strategies
- Evidence handling and forensics
- Disaster recovery and business continuity
- Third-party/vendor risk management

**Memory hook**: "If you're in security operations, you're on the front lines. Detect fast, respond faster, learn from every incident."

**Why it matters**: This is where most security professionals live. Incident response saves companies millions.

---

### Domain 8: Software Development Security (8% — 10 questions)

**What it covers**: Secure software development lifecycle (SDLC), secure coding, and application security.

**Key topics**:
- SDLC models and phases
- Secure coding practices and code review
- Security testing in development (unit testing, integration testing)
- Code obfuscation and anti-tampering
- Application security (OWASP Top 10, injection, XSS, CSRF)
- Database security
- API security
- Dependency management and supply chain security
- Security in cloud development and containers

**Memory hook**: "Secure coding = stop vulnerabilities before they're born. OWASP Top 10 = start here for app security."

**Why it matters**: **This is the smallest domain**, but it's critical if you work with development teams or cloud-native security.

---

## Domain Weight Summary

Use this to allocate study time:

| Domain | Exam Weight | # Questions | Priority | Study Time |
|--------|---|---|---|---|
| 1. Security & Risk Management | 15% | 18-19 | HIGH | 15% |
| 2. Asset Security | 10% | 12-13 | MEDIUM | 10% |
| 3. Security Architecture & Engineering | 12% | 15 | HIGH | 12% |
| 4. Communication & Network Security | 14% | 17-18 | HIGH | 14% |
| 5. Identity & Access Management | 13% | 16-17 | HIGH | 13% |
| 6. Security Assessment & Testing | 12% | 15 | MEDIUM | 12% |
| 7. Security Operations ⭐ | 16% | 20-21 | **CRITICAL** | **20%** |
| 8. Software Development Security | 8% | 10 | LOW-MEDIUM | 8% |

**Key insight**: Domains 1, 3, 4, 5, and 7 together are ~70% of the exam. Master these, and you'll likely pass.

---

## 2025-2026 Exam Updates

The CISSP exam landscape continues to evolve to reflect emerging threats and technologies. Be aware of these recent additions to the exam:

### AI/ML Security

- **AI governance and risk**: How to govern machine learning systems responsibly
- **Model security**: Adversarial attacks, model poisoning, data poisoning
- **LLM security**: Prompt injection, jailbreaking, data leakage through models
- **AI bias and fairness**: Detecting and mitigating algorithmic bias in security decisions

### Zero Trust Architecture

- **Zero Trust principles**: Never trust, always verify (shift from perimeter security)
- **Microsegmentation**: Breaking networks into small zones, verify access at each boundary
- **Least privilege access**: Apply to both users and services/workloads
- **Continuous verification**: Monitor and re-authenticate continuously

### SASE (Secure Access Service Edge)

- **SASE definition**: Converged network and security services delivered at the edge
- **Cloud-first security**: Moving from VPN to cloud-based security
- **DLP in cloud**: Data loss prevention in cloud and SaaS environments
- **User and device verification**: Authentication and posture checking for cloud resources

### Privacy Expansion

- **144+ countries with data protection laws**: GDPR is no longer unique; many nations have equivalent laws
- **GDPR 72-hour breach notification**: Enhanced from original 30-day requirement
- **NIS2 (EU Network and Information Security Directive 2)**: New EU standard for critical infrastructure
- **US state privacy laws**: CCPA (California), VCCPA (Virginia), MPPA (Montana), similar laws in 10+ states
- **Privacy by design**: Required in many regulatory frameworks
- **Consent management**: GDPR, CCPA, and others require explicit user consent for data processing

### Supply Chain Security

- **Software supply chain**: Dependency management, vulnerable libraries (Log4j lessons)
- **SBOMs (Software Bill of Materials)**: Tracking components and versions
- **Third-party risk**: Vendor assessment, continuous monitoring of supplier security
- **Hardware supply chain**: Compromised chips, counterfeit components

### Cloud-Native Security

- **Container security**: Docker, Kubernetes, image scanning, runtime protection
- **Serverless security**: Lambda, Google Cloud Functions; different threat model
- **Infrastructure as Code (IaC) security**: Terraform, CloudFormation; scanning for misconfigurations
- **API security**: Service-to-service authentication, OAuth 2.0 in microservices

### Post-Quantum Cryptography

- **Quantum threat horizon**: Quantum computers can break RSA, ECC
- **NIST post-quantum standards**: Approved algorithms (Kyber, Dilithium) for migration planning
- **Hybrid cryptography**: Using both classical and post-quantum algorithms during transition
- **Crypto-agility**: Designing systems that can swap algorithms without rebuild

### Updated Exam Format (as of 2026)

| Attribute | Detail |
|-----------|--------|
| **Duration** | 3 hours |
| **Questions** | 100-150 (CAT adaptive) |
| **Passing Score** | ~700/1000 (70% threshold) |
| **Format** | Computer Adaptive Testing (CAT) — difficulty adapts to your performance |
| **Cost** | ~$750 USD |
| **Retakes** | $475 (if you don't pass) |

**Key change**: The exam uses **Computer Adaptive Testing (CAT)**, meaning the difficulty of questions adjusts based on your answers. This means:
- Correct answers → harder questions appear next
- Incorrect answers → easier questions appear next
- No two tests are identical in difficulty
- Your score depends on both number correct AND difficulty of questions answered

---

## Recommended Study Order

### Option 1: Bootcamp-Friendly (Monday-Saturday)

Study one domain per day, repeat weekly:

1. **Monday**: Security and Risk Management
2. **Tuesday**: Asset Security
3. **Wednesday**: Security Architecture and Engineering
4. **Thursday**: Communication and Network Security
5. **Friday**: Identity and Access Management
6. **Saturday**: Security Assessment and Testing + Operations + Software Development Security

(Lighter domains Mon-Fri, heavier on Saturday)

### Option 2: Importance-Based

Study in order of exam weight and difficulty:

1. **Week 1**: Security Operations (largest domain, most critical)
2. **Week 1-2**: Communication and Network Security (14%, foundational)
3. **Week 2**: Identity and Access Management (13%, heavily tested)
4. **Week 2-3**: Security and Risk Management (15%, strategic)
5. **Week 3**: Security Architecture and Engineering (12%, technical)
6. **Week 3-4**: Security Assessment and Testing (12%, practical)
7. **Week 4**: Asset Security (10%, foundational)
8. **Week 4**: Software Development Security (8%, specialized)

### Option 3: Self-Paced

Study domains in any order. Use this kit's self-paced mode to pick 1-2 per day.

---

## Study Tips

### 1. Understand, Don't Memorize

CISSP tests **conceptual understanding**, not trivia. You need to:
- Understand **why** a security decision matters
- Apply concepts to **scenarios**
- Compare and contrast similar concepts (least privilege vs. zero trust)

### 2. Know Your Frameworks

The exam heavily references:
- **NIST** (U.S. cybersecurity frameworks)
- **ISO 27001** (international security standards)
- **COBIT** (IT governance)
- **CIS Controls** (practical security controls)

You don't need to memorize every detail, but know the major frameworks by name.

### 3. Distinguish Between Similar Concepts

CISSP loves testing your ability to tell concepts apart:
- **Identification vs. authentication vs. authorization**
- **Threat vs. vulnerability vs. risk**
- **Confidentiality vs. integrity vs. availability**
- **OAuth vs. SAML vs. OpenID Connect**
- **DAC vs. MAC vs. RBAC vs. ABAC**

### 4. Real-World Scenarios

Practice applying concepts to scenarios:
- "A user's password was compromised. What should you do?"
- "You need to allow developers to access production data without storing passwords. What's the best approach?"
- "Your organization needs to meet GDPR. What controls should you implement?"

This kit provides scenario-based questions to help.

### 5. Study Domain Weights Proportionally

Spend ~15% of your time on Security and Risk Management, but ~20% on Security Operations. Don't overstudy small domains (Software Dev is only 8%).

### 6. Wrong Answers Are Gold

Every wrong answer shows a knowledge gap. The wrong-answer bank in this kit accumulates them so you can focus on weak areas. **This is more valuable than retaking easy questions.**

### 7. Spaced Repetition

You'll forget concepts if you only study them once. This kit uses spaced repetition:
- First exposure: daily quiz
- Reinforcement: weekly review quiz (weighted to weak areas)
- Long-term: wrong-answer bank reviewed periodically

### 8. Time Management on Exam Day

- **125 questions in 3 hours** = ~1.4 minutes per question
- You can review at the end; don't get stuck on one question
- Read carefully; CISSP questions are wordy and test nuance
- Watch for absolutes ("always," "never") — they're often wrong

---

## Free and Paid Resources

### Free

- **ISC2 Study Materials**: ISC2 publishes free study guides for each domain (available on their website)
- **NIST Frameworks**: Free downloads from nist.gov (NIST Cybersecurity Framework, NIST SP 800 series)
- **YouTube**: Search "CISSP domain X" for free lectures (quality varies)
- **Reddit**: r/cissp has community advice and study groups
- **This kit**: Generates CISSP-standard questions from Claude's training data

### Paid

- **Official ISC2 Study Guide**: ~$40-60, comprehensive, official (recommended)
- **Practice Exams**: ISC2 provides official practice exams (~$150-200)
- **Udemy/Coursera Courses**: $10-100, structure your learning (varies in quality)
- **Bootcamps**: $2,000-5,000, intensive (5-10 weeks), instructor-led
- **ACI Learning**: ~$500/year, video courses and labs

**Recommendation**: Combine this kit with one paid resource (official study guide + practice exams, or a bootcamp). This kit is free and works standalone, but official materials are worth the investment.

---

## Exam Day Checklist

Before the exam, ensure:

- [ ] You've passed at least 3-4 practice exams at 70%+
- [ ] You understand all 8 domains conceptually
- [ ] Your wrong-answer bank is reviewed (mastered most weak concepts)
- [ ] You know the time limit (3 hours, ~1.4 min per question)
- [ ] You know the location and check-in procedures (arrive 15 minutes early)
- [ ] You bring valid ID (passport or driver's license)
- [ ] You're well-rested (more important than last-minute cramming)

---

## Post-Exam

After the exam:

1. **If you pass**: Congratulations! You're officially a CISSP. Maintain your 40 CPE (Continuing Professional Education) credits per year to keep the credential.

2. **If you don't pass**: Don't be discouraged. Many people pass on the second attempt. Review your wrong areas, take the exam again in 30-90 days, and focus study on weak domains.

3. **Regardless**: This kit will help you maintain knowledge. Even after passing, periodic review prevents knowledge decay.

---

## Long-Term Learning

CISSP is a "living" credential. The security landscape evolves constantly:
- New threats emerge
- New tools and technologies arrive
- Regulations change (GDPR, CCPA, etc.)

**Maintain your credential** by:
- Staying current with security news and blogs
- Taking 40 CPE credits per 3-year cycle
- Attending conferences (BSides, Black Hat, Infosec, etc.)
- Teaching others (great for CPEs and retention)
- Contributing to open-source security tools

This kit can be used repeatedly to maintain knowledge or to help others study.

---

## Final Words

CISSP is **not** an easy certification. It's designed for seasoned security professionals. But it's absolutely achievable with consistent study, focus on weak areas, and understanding (not memorization).

**You've got this.** Use this study kit daily, focus on your wrong-answer bank, and trust the process.

---

**Next steps:**
1. Edit **CONFIG.md** with your study schedule
2. Review this guide to understand domain weights
3. Run **DAILY-PROMPT.md** to start your first study session
4. Track wrong answers in **WRONG-ANSWER-BANK.md**
5. Take **REVIEW-PROMPT.md** weekly to assess progress

Good luck! 🎯
