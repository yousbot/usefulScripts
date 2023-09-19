def convert_jsonl_to_json(jsonl_file_path, json_file_path, buffer_size):
    """Convert a JSONL file to a standard JSON file.
    
    Parameters:
        jsonl_file_path (str): The path to the source JSONL file.
        json_file_path (str): The path where the converted JSON file will be saved.
        buffer_size (int): The size of the read buffer in bytes.
    """
    with open(jsonl_file_path, 'r') as infile, open(json_file_path, 'w') as outfile:
        # Write the opening bracket for the JSON array
        outfile.write('[')
        
        # Initialize buffer and a flag to manage object separators
        buffer = ""
        is_first_object = True

        while True:
            chunk = infile.read(buffer_size)
            if not chunk:
                break  # End of file reached
            
            buffer += chunk
            lines = buffer.split('\n')
            
            for i in range(len(lines) - 1):
                # Add a comma separator for all objects after the first
                if not is_first_object:
                    outfile.write(',')
                outfile.write(lines[i])
                
                is_first_object = False  # Update flag after writing the first object
            
            # Keep the last (potentially incomplete) line for the next iteration
            buffer = lines[-1]

        # Write any remaining content in buffer
        if buffer:
            if not is_first_object:
                outfile.write(',')
            outfile.write(buffer)

        # Write the closing bracket for the JSON array
        outfile.write(']')


# Constants
BUFFER_SIZE = 50 * 1024 * 1024  # 50 MB

# Convert JSONL to JSON
convert_jsonl_to_json('isbndb_2022_09.jsonl', 'isbndb_2022_09.json', BUFFER_SIZE)
