import argparse
import ollama

def main():
    parser = argparse.ArgumentParser(description='Process an image with Ollama Vision.')
    parser.add_argument('-i', '--image', required=True, help='Path to the image file')
    parser.add_argument('-q', '--question', default='What is in this image?', help='Question to ask about the image')
    parser.add_argument('-m', '--model', default='llama3.2-vision:11b', help='Model to use for processing the image')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')

    args = parser.parse_args()

    response = ollama.chat(
        model=args.model,
        messages=[{
            'role': 'user',
            'content': args.question,
            'images': [args.image]
        }],
        debug=args.debug,
    )

    print(response['message']['content'])

if __name__ == '__main__':
    main()