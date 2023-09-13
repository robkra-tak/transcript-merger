import os
import re

def merge_transcripts(input_dir, output_dir=os.getcwd(), output_file="output.txt"):
    """
    Merge transcripts from multiple text files and update timestamps based on elapsed time.

    Args:
        input_dir (str): Path to input directory containing text files.
        output_dir (str, optional): Path to output directory. Defaults to current working directory.
        output_file (str, optional): Name of output file. Defaults to "output.txt".
    """
    # Get list of text files in input directory and its subdirectories
    file_list = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".txt"):
                file_list.append(os.path.join(root, file))
    # Sort file list alphabetically
    file_list.sort()
    # Iterate through file list and calculate new timestamps
    merged_transcript = ""
    elapsed_time = 0
    for file in file_list:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                # Check if line contains timestamp
                if re.match(r"\d+:\d+", line):
                    # Calculate new timestamp
                    timestamp = re.findall(r"\d+:\d+", line)[0]
                    new_timestamp = add_time(timestamp, elapsed_time)
                    # Replace old timestamp with new timestamp
                    line = line.replace(timestamp, new_timestamp)
                    # Update elapsed time
                    elapsed_time = get_elapsed_time(new_timestamp)
                # Append line to merged transcript
                merged_transcript += line
    # Save merged transcript to output file
    with open(os.path.join(output_dir, output_file), "w") as f:
        f.write(merged_transcript)

def add_time(timestamp, elapsed_time):
    """
    Add elapsed time to timestamp and return new timestamp.

    Args:
        timestamp (str): Timestamp in the format "MM:SS".
        elapsed_time (int): Elapsed time in seconds.

    Returns:
        str: New timestamp in the format "MM:SS".
    """
    # Convert timestamp to seconds
    minutes, seconds = map(int, timestamp.split(":"))
    total_seconds = minutes * 60 + seconds
    # Add elapsed time to total seconds
    total_seconds += elapsed_time
    # Convert total seconds to timestamp
    new_minutes = total_seconds // 60
    new_seconds = total_seconds % 60
    new_timestamp = "{:02d}:{:02d}".format(new_minutes, new_seconds)
    return new_timestamp

def get_elapsed_time(timestamp):
    """
    Convert timestamp to elapsed time in seconds.

    Args:
        timestamp (str): Timestamp in the format "MM:SS".

    Returns:
        int: Elapsed time in seconds.
    """
    # Convert timestamp to seconds
    minutes, seconds = map(int, timestamp.split(":"))
    total_seconds = minutes * 60 + seconds
    return total_seconds

def main():
    """
    Main function for merging transcripts from multiple text files.
    """
    # Get input directory from user
    input_dir = input("Enter path to input directory: ")
    # Get output directory from user
    output_dir = input("Enter path to output directory (leave blank for current working directory): ")
    if output_dir == "":
        output_dir = os.getcwd()
    # Get output file name from user
    output_file = input("Enter output file name (leave blank for 'output.txt'): ")
    if output_file == "":
        output_file = "output.txt"
    # Merge transcripts and save to output file
    merge_transcripts(input_dir, output_dir, output_file)
    print("Transcripts merged successfully.")

if __name__ == "__main__":
    main()