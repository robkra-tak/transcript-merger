# Merge Transcripts Script

This script allows users to merge transcripts from multiple text files and update timestamps based on the elapsed time. It processes all `.txt` files in the specified directory (and its subdirectories) to create a consolidated transcript with updated timestamps.

## Prerequisites

- Python 3.x

## How to Use

1. **Clone the Repository**:
   If you haven't already, clone this repository to your local machine.

2. **Navigate to the Directory**:
   Use the terminal or command prompt to navigate to the directory containing the script.

3. **Run the Script**:
   Execute the script using:
   ```
   python app.py
   ```

4. **Provide Inputs**:
   - **Input Directory Path**: Enter the full path to the directory containing the transcript `.txt` files.
   - **Output Directory**: Specify the directory where you want the merged transcript to be saved. If you press Enter without specifying a directory, the script will save the file in the current directory by default.
   - **Output File Name**: Enter the name for the merged transcript file. If you press Enter without providing a name, the default name `output.txt` will be used.

5. **Check the Output**:
   Once the script completes execution, navigate to the specified output directory to access the merged transcript.

## Features

- **Recursive File Search**: The script searches not only the specified directory but also its subdirectories for `.txt` files to process.

- **Timestamp Update**: Merges the content of the files and updates the timestamps based on the elapsed time to maintain continuity.

- **Customizable Output**: Choose the directory and file name for the consolidated transcript.

## Notes

- The script assumes that the input `.txt` files have timestamps in the format "MM:SS".

- Make sure the input directory contains only transcript files to avoid unintentional processing of unrelated `.txt` files.

- Ensure that the timestamps in the input files are accurate and consistent for the best merging result.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. If you find any bugs or have suggestions for improvements, please open an issue.

## License

This script is provided under the MIT License. See the LICENSE file for details.