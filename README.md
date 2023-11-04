# Gmail Email Sorter

This script is a custom solution for sorting and managing Gmail emails via IMAP. As Gmail lacks a native and intuitive rules system similar to that in Outlook, I developed a script that performs basic sorting actions from the terminal.

## Features

### Sorting Rules
The script uses a series of if statements to apply basic sorting rules to incoming emails. Since Gmail relies on labels rather than folders, the script ensures that emails are appropriately labeled and managed, emulating a folder-like organization through label assignments. This is essential, especially as Gmail's inbox does not empty when emails are labeled/moved.

### Archive Synchronization
To maintain an up-to-date local archive, the script downloads all emails from the 'All Mail' section (equivalent to 'Archive' in Gmail) and updates an archive stored on the local computer. This ensures that the local archive matches the contents of the Gmail 'All Mail,' providing a complete and synchronized record of received emails.

## How It Works

1. **Connection via IMAP**: The script establishes a connection to your Gmail account using IMAP to access and manage emails.
2. **Sorting**: Upon receiving new emails, the script evaluates them based on predefined rules and labels them accordingly.
3. **Archive Update**: To maintain an up-to-date local archive, the script downloads all emails from the 'All Mail' section and updates the local archive.

## Why This Script?

Gmail's lack of an intuitive rules system and its usage of labels instead of folders inspired the development of this script. It provides a simple yet effective way to manage emails and maintain an organized inbox and local archive.

## Usage

1. **Setup**: Configure the script with your Gmail credentials and adjust sorting rules as necessary.
2. **Run**: Launch the script from the terminal.
3. **Enjoy**: Sit back and let the script handle the sorting and archiving of your emails.

Feel free to contribute, suggest improvements, or adapt this script to suit your needs!
