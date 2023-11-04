# Gmail Email Sorter

This script, designed for terminal use, employs IMAP to connect to Gmail and implements a set of basic rules for sorting emails. Given Gmail's lack of a straightforward rules system similar to Outlook, the script utilizes custom if statements for effective sorting.

### Key Features

- **Basic Rules for Sorting**: The script applies a set of if statements to sort incoming emails. Due to Gmail's labeling system instead of traditional folders, the script ensures that emails are properly labeled, maintaining an organized inbox.

- **Emulation of Folders with Labels**: Gmail's unique label system means moving emails does not clear them from the inbox. Consequently, the script ensures proper copying instead of moving to maintain an organized inbox structure.

- **Archive Synchronization**: Recognizing the importance of tracking received emails, the script downloads all emails from Gmail's 'All Mail' section (equivalent to Archive) to update the local archive on your computer.

### How It Works

1. **IMAP Connection**: The script establishes a connection to Gmail via IMAP to manage and access emails.
2. **Sorting Logic**: Upon receiving emails, the script evaluates and labels them based on predefined rules.
3. **Archive Update**: The script synchronizes with Gmail's 'All Mail' section to ensure the local archive remains updated.

### Usage

1. **Setup**: Configure the script with your Gmail credentials and adjust sorting rules as needed.
2. **Execution**: Run the script from the terminal.
3. **Organized Inbox**: Enjoy the automated sorting and archiving of your emails.

This script simplifies the management of Gmail emails, compensating for Gmail's absence of an intuitive rules system by utilizing custom if statements for sorting. It ensures an organized inbox by employing label-based sorting and maintaining an updated local archive.


