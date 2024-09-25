import sys
import os
import pypandoc

def convert_md_to_docx(input_md, output_docx):
    # Converts the Markdown file to DOCX using pypandoc
    output = pypandoc.convert_file(input_md, 'docx', outputfile=output_docx)
    return output

def main():
    # Checks if the argument was passed
    if len(sys.argv) != 2:
        print("Usage: python3 main.py 'FILENAME'")
        sys.exit(1)
    
    # Gets the file name without extension
    file_name = sys.argv[1]

    # Defines the markdown and docx file names, in the same folder as the script or the provided path
    input_md = f"{file_name}.md"
    output_docx = f"{file_name}.docx"

    # Checks if the markdown file exists
    if not os.path.exists(input_md):
        print(f"File {input_md} not found.")
        sys.exit(1)
    
    # Converts the file
    convert_md_to_docx(input_md, output_docx)
    print(f"File {output_docx} generated successfully.")

if __name__ == "__main__":
    main()
