import os, io
import pandas as pd

from google.cloud import texttospeech_v1
from google.cloud import translate_v2
from google.cloud import language_v1
from google.cloud import vision_v1


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_credentials.json'
client = vision_v1.ImageAnnotatorClient()
client1=texttospeech_v1.TextToSpeechClient()
client2=translate_v2.Client()

FOLDER_PATH = 'C:\Handwritten to text\Handwritten\Pics'
IMAGE_FILE = '7th.jpeg'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

image = vision_v1.types.Image(content=content)
response = client.document_text_detection(image=image)

docText = response.full_text_annotation.text
print(docText)
pages = response.full_text_annotation.pages
"""
for page in pages:
    for block in page.blocks:
        print('block confidence:', block.confidence)

        for paragraph in block.paragraphs:
            print('paragraph confidence:', paragraph.confidence)

            for word in paragraph.words:
                word_text = ''.join([symbol.text for symbol in word.symbols])

                print('Word text: {0} (confidence: {1}'.format(word_text, word.confidence))

                for symbol in word.symbols:
                    print('\tSymbol: {0} (confidence: {1}'.format(symbol.text, symbol.confidence))
"""
text =  docText 

synthesis_input = texttospeech_v1.SynthesisInput(ssml=text)

voice1 = texttospeech_v1.VoiceSelectionParams(
    language_code = 'en-in',
    ssml_gender= texttospeech_v1.SsmlVoiceGender.FEMALE )


print(client1.list_voices)
audio_config= texttospeech_v1.AudioConfig(
    audio_encoding = texttospeech_v1.AudioEncoding.MP3
)

response1 = client1.synthesize_speech (
    input=synthesis_input,
    voice=voice1,
    audio_config=audio_config
)

with open('audio.mp3','wb',) as output:
    output.write(response1.audio_content)


target = input(" Enter the language to which you wish to translate : ")

output1 = client2.translate(text,target_language = target)

print(output1)


synthesis_input1 = texttospeech_v1.SynthesisInput(ssml=output1['translatedText'])

voice2 = texttospeech_v1.VoiceSelectionParams(
    language_code = target,
    ssml_gender= texttospeech_v1.SsmlVoiceGender.FEMALE )


print(client1.list_voices)
audio_config= texttospeech_v1.AudioConfig(
    audio_encoding = texttospeech_v1.AudioEncoding.MP3
)

response2 = client1.synthesize_speech (
    input=synthesis_input1,
    voice=voice2,
    audio_config=audio_config
)

with open('audio1.mp3','wb',) as output10:
    output10.write(response2.audio_content)





def sample_analyze_entities(docText):
    client3 = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": docText, "type_": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8
    response = client3.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})
    for entity in response.entities:
        print(u"Representative name for the entity: {}".format(entity.name))
        print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))
        print(u"Salience score: {}".format(entity.salience))
        for metadata_name, metadata_value in entity.metadata.items():
            print(u"{}: {}".format(metadata_name, metadata_value))
        for mention in entity.mentions:
            print(u"Mention text: {}".format(mention.text.content))
            print(u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name)  )
    print(u"Language of the text: {}".format(response.language))

sample_analyze_entities(docText)