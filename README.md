# PythonMarkdownToDocxConverter

A simple Python script to convert Markdown (`.md`) files to DOCX (`.docx`) format using the `pypandoc` library. This tool is useful for anyone looking to quickly transform Markdown files into a more structured document format like DOCX.

## How It Works

The script takes the name of the Markdown file (without the extension) as an argument, searches for the corresponding `.md` file, and converts it to a `.docx` file with the same name in the same directory.

### Example Usage

Run the script using Python:

```bash
python3 md_to_docx_converter.py "FILENAME"
```

Where FILENAME is the name of the Markdown file (without the .md extension).

This command will convert MyDocument.md to MyDocument.docx.

## Prerequisites

Before running the script, ensure you have pypandoc installed. You can install it using pip

```bash
pip install pypandoc
```

## Limitations

This project is intended for educational purposes only and should not be used in other context (such as production environments).

## Contributing

Your contributions are welcome! If you have suggestions for improvements, encounter any issues, or would like to contribute to the development of this project, please feel free to submit pull requests or report issues via the GitHub issue tracker.

## License and Disclaimer

This project is open-source and available under [MIT License](https://opensource.org/licenses/MIT). You are free to copy, modify, and use the project as you wish. However, any responsibility for the use of the code is solely yours. Please use it at your own risk and discretion.
