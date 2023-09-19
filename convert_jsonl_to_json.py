BUFFER_SIZE = 50 * 1024 * 1024  # 10 MB

with open('isbndb_2022_09.jsonl', 'r') as infile, open('isbndb_2022_09.json', 'w') as outfile:
    outfile.write('[')  # Start JSON array
    buffer = ""
    first = True  # Flag to handle commas between JSON objects
    
    while True:
        chunk = infile.read(BUFFER_SIZE)
        if not chunk:
            break  # End of file
        buffer += chunk
        lines = buffer.split('\n')
        
        for i in range(len(lines) - 1):
            if first:
                first = False
            else:
                outfile.write(',')
            outfile.write(lines[i])
        
        buffer = lines[-1]  # Keep the last line in the buffer, as it might be incomplete

    if buffer:  # Write any remaining content
        if not first:
            outfile.write(',')
        outfile.write(buffer)
        
    outfile.write(']')  # End JSON array
