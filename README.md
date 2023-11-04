## Gmail Email Sorter

This script is a custom solution for sorting and managing Gmail emails via IMAP. It performs basic sorting actions using if statements in the terminal.

### Features

- **Sorting Rules**: The script applies basic sorting rules to incoming emails, ensuring appropriate labeling and organization. It emulates folder-like organization through label assignments, essential as Gmail's inbox does not empty when emails are labeled/moved.
  
- **Archive Synchronization**: To maintain an up-to-date local archive, the script downloads all emails from the 'All Mail' section (equivalent to 'Archive' in Gmail) and updates a local archive.

### How It Works

1. **Connection via IMAP**: The script establishes a connection to your Gmail account using IMAP to access and manage emails.
2. **Sorting**: Upon receiving new emails, the script evaluates and labels them based on predefined rules.
3. **Archive Update**: To maintain an up-to-date local archive, the script syncs with the 'All Mail' section.

### Usage

1. **Setup**: Configure the script with your Gmail credentials and adjust sorting rules if needed.
2. **Run**: Launch the script from the terminal.
3. **Enjoy**: Let the script handle the sorting and archiving of your emails.

This script is designed to manage Gmail emails effectively, compensating for Gmail's lack of an intuitive rules system and utilizing labels instead of folders.
