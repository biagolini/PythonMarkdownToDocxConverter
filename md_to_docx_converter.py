import sys
import os
import pypandoc

def convert_md_to_docx(input_md, output_docx):
    # Converts the Markdown file to DOCX using pypandoc
    try:
        output = pypandoc.convert_file(input_md, 'docx', outputfile=output_docx)
        return output
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

def remove_md_extension(filename):
    # Removes the .md extension if it's present
    if filename.lower().endswith(".md"):
        return filename[:-3]
    return filename

def main():
    # Checks if the argument was passed
    if len(sys.argv) != 2:
        print("Usage: python3 main.py 'FILENAME'")
        sys.exit(1)
    
    # Gets the file name and removes .md extension if necessary
    file_name = remove_md_extension(sys.argv[1])

    # Defines the markdown and docx file names
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
