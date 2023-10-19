#!/bin/bash

# Set the output file name
output_file="biobio.db"

# Set the target directory
target_directory="data/raw"

# Confirm that gdown is installed (Google Drive downloader tool)
if ! command -v gdown &> /dev/null; then
    echo "The 'gdown' command is required but not found. Please install it."
    return 1
fi

echo "Be patient. File size is 436 MB."

# Download the file using gdown
gdown "1Z4ICTDEFqQGY1wHLI92aLcs_3cSbCPtt" -O "$output_file"


# Check if the download was successful
if [ $? -eq 0 ]; then
    echo "Download completed: $output_file"

    echo "Moving the downloaded file..."
    mv "$output_file" "$target_directory/$output_file"

    if [ $? -eq 0 ]; then
        echo "File moved to $target_directory/$output_file"
    else
        echo "Failed to move the file to $target_directory."
    fi
else
    echo "Download failed."
fi