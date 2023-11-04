#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // Command to call the python script
    char command[] = "python -u /your-directory/mail.py";
    

    // Call the Python script using the system function
    int result = system(command);
    
    if (result == -1) {
        perror("Error executing");
        return 1;
    }

    // Check if the destination directory exists
    const char* sourceFolder = "/your-directory/emails"; // Change to the source folder path
    const char* destinationFolder = "/your-directory-destination"; // Change to the destination folder path

    FILE *file;
    if ((file = fopen(destinationFolder, "r"))) {
        fclose(file);

        // Command to copy the folder to the destination directory
        char copyCommand[512];
        snprintf(copyCommand, sizeof(copyCommand), "cp -r %s %s", sourceFolder, destinationFolder);

        // Copy the folder using the system function
        int copyResult = system(copyCommand);

        if (copyResult == -1) {
            perror("Error copying");
            return 1;
        }
    } else {
        return 1;
    }

    return 0;
}
