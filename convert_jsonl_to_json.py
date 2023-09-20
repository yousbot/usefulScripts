
import sys

def convert_jsonl_to_json(jsonl_file_path, json_file_path, buffer_size):
    """Convert a JSONL file to a standard JSON file.
    
    Parameters:
        jsonl_file_path (str): The path to the source JSONL file.
        json_file_path (str): The path where the converted JSON file will be saved.
        buffer_size (int): The size of the read buffer in bytes.
    """
    with open(jsonl_file_path, 'r') as infile, open(json_file_path, 'w') as outfile:
        outfile.write('[')
        buffer = ""
        is_first_object = True

        while True:
            chunk = infile.read(buffer_size)
            if not chunk:
                break
            
            buffer += chunk
            lines = buffer.split('\n')
            
            for i in range(len(lines) - 1):
                if not is_first_object:
                    outfile.write(',')
                outfile.write(lines[i])
                is_first_object = False
            
            buffer = lines[-1]

        if buffer:
            if not is_first_object:
                outfile.write(',')
            outfile.write(buffer)

        outfile.write(']')

if __name__ == "__main__":
    if len(sys.argv) > 3:
        jsonl_file_path = sys.argv[1]
        json_file_path = sys.argv[2]
        buffer_size = int(sys.argv[3])
        convert_jsonl_to_json(jsonl_file_path, json_file_path, buffer_size)
    else:
        print("Usage: python script.py <JSONL_File_Path> <JSON_File_Path> <Buffer_Size>")
