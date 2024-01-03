## Configurations with Security Impact

1. **Lack of Two-Factor Authentication (2FA):**
   - NIST Compliance Category: Identification and Authentication
   - Description: Without 2FA, your GitHub account relies solely on a password for access. Adding 2FA is like having an additional lock on your account, requiring a second verification form, such as a code sent to your phone.
   - Best Practice Recommendation: Enable Two-Factor Authentication for your GitHub account to add an extra layer of security
   - Meaning of Configuration: 2FA enhances security by requiring users to provide two forms of identification before accessing their account, significantly reducing the risk of unauthorized access
   - Risks of Not Following Best Practice: Without 2FA, if a password is compromised, an attacker can gain unauthorized access to the GitHub account, potentially leading to data loss, unauthorized code changes,         or even account takeover.
   - Steps to Fix or Work Around Risks: Enable 2FA on your GitHub account by going to the Security settings. This adds an extra step during login, requiring a code from your mobile device and your password.
   - Impact on GitHub Usage: Enabling 2FA may slightly increase the time it takes to log in, but the added security is crucial, especially for accounts handling sensitive code or repositories.
   - MITRE Attack Techniques: Phishing (T1566): Attackers might attempt to trick users into revealing their passwords. With 2FA, the second factor adds an additional barrier against unauthorized access even if the password is compromised.

2. **Public Repository with Sensitive Information**

    - NIST Compliance Category: System and Communications Protection 

    - Description: Make sure repositories containing sensitive data are set to private, not public, to limit access.

    - Best Practice Recommendation: Review repository settings and ensure sensitive information is stored in private repositories.

    - Configuration Meaning: If a repository with sensitive data is public, anyone on the internet can access and potentially misuse that information.

    - Risks of Misconfiguration: Unauthorized access to sensitive data, compliance violations, and potential legal consequences.

    - Steps to Fix: Change the repository from public to private in the repository settings.

    - Impact on GitHub Usage: Limits access to authorized collaborators. Public repositories are accessible to anyone, while private repositories restrict access to team members.

    - MITRE Attack Techniques: Data from Information Repositories (T1213) is related. Public repositories may expose sensitive information that can be exploited

   
3. **Lack of Code Review Practices**

    - NIST Compliance Category: Configuration Management 


    
4.  **Insufficient Branch Protection Rules**

    - NIST Compliance Category: Access Control


 5. **Lack of Security Alerts and Notifications**

    - NIST Compliance Category: Incident Response