Overview
This project is a Python-based automation bot that streamlines the process of searching and saving jobs on LinkedIn. By leveraging Selenium WebDriver, the bot automates tasks such as logging into LinkedIn, navigating job search pages, and saving relevant job listings.

Key Features
Automated LinkedIn Login: Uses Selenium to securely log into LinkedIn with user-provided credentials.
Job Search Automation: Navigates to the Python Developer job listings for the London area, scraping and interacting with multiple job posts.
Job-Saving Functionality: Automatically clicks the 'Save' button for job postings, demonstrating bot’s ability to handle UI elements dynamically.
Error Handling: Exception handling for missing or dynamic elements to ensure script robustness.

Skills Demonstrated
Selenium Automation: Proficient in using Selenium WebDriver for web automation tasks, including interacting with dynamic web pages and handling forms.
Python Scripting: Developed a structured Python script with modular functions for login, navigation, and interaction with web elements.
Exception Handling: Demonstrates strong error-handling practices to manage cases of missing elements (e.g., jobs not clickable or buttons missing).
Web Scraping: Showcases basic web scraping techniques to collect and interact with job listings using CSS selectors and XPaths.
Secure Handling of Credentials: Removed hardcoded credentials and replaced them with secure input handling, showcasing security awareness in automation projects.

How It Works
Login Process: The bot prompts the user to input LinkedIn credentials. It then automates the login process, ensuring secure data handling.
Job Search: The bot navigates to a predefined job search page and loads available listings.
Interaction with Jobs: It clicks on each job listing and attempts to save the job using Selenium’s ability to interact with web elements.
Error Handling: Built-in exception handling ensures the script continues running even if a particular job posting is unavailable.

Future Improvements
Implement multi-threading for faster job-saving processes.
Add functionality for auto-applying to jobs with user-uploaded resumes.
Integrate an option to search for jobs in multiple locations or roles dynamically.

