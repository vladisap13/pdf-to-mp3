from gtts import gTTS
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path='test.pdf', language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'\nOriginal file: {Path(file_path).name}')
        print(f'Processing...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)

        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'{file_name}.mp3 saved successfully!'
    else:
        return 'File is not exists!'

def main():
    file_path = input('Enter a file\'s path: ')
    language = input('Choose language, for example \'en\': ')
    print(pdf_to_mp3(file_path=file_path, language=language))

if __name__ == '__main__':
    main()
