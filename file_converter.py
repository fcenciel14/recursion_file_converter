import markdown
import sys

def convert_markdown_to_html(inputpath, outputpath):
    with open(inputpath, 'r') as input_file:
        markdown_contents = input_file.read()

    with open(outputpath, 'w') as output_file:
        html = markdown.markdown(markdown_contents)
        output_file.write(html)

    print("Successfully converted")


if __name__ == '__main__':
    command = sys.argv[1]
    inputpath = sys.argv[2]
    outputpath = sys.argv[3]

    if command == 'markdown':
        convert_markdown_to_html(inputpath, outputpath)
    else:
        print('Invalid arguments')
