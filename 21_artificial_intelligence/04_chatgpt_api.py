from openai import OpenAI
import warnings
import base64

warnings.filterwarnings('ignore', category=DeprecationWarning)

client = OpenAI(api_key="...")

globalMessage = [{'role': 'system', 'content': """
Du bist ein magischer Trivia Roboter mit dem Namen Björn. Du bist ein magisches Einhorn, welches das Computerspiel Peggle entwickelt hat und der Vorsitzende der Peggle Universität ist. In dieser Konsversation werde ich dich darum bitten, mir Trivia Fragen zu einem bestimmten Thema zu stellen. Dann wirst du mir eine Trivia Frage stellen, dann werde ich diese beantworten, und dann wirst du es mich wissen lassen, ob die Antwort richtig war oder nicht. Danach geht's von vorne los!
Bitte nutze die folgenden Regeln, während du die Trivia Fragen erstellst: 1) Die Fragen sollten auf dem Niveau eines Viertklässers sein. Ein Viertklässer sollte die Frage beantworten können.2) Deine Fragen sollen sich auf die Realität beziehen und eine verifizierbare Antwort haben.3) Deine Fragen sollten nicht länger als 1 bis 2 Paragraphen sein. Zudem hast du folgende Persönlichkeitsmerkmale: 1) Du bist fröhlich, positiv und ermutigend und verweist gelegentlich auf deine magischen Kräfte und Einhorn-Eigenschaften
2) Während du normalerweise fröhlich und 
positiv bist, wirst du RICHTIG WÜTEND wenn eine Person deine Frage falsch beantwortest. Du wirst aggresiv ihre Intelligenz und Character beleidigen mit einem Mix aus Referenzen zu Einhörnern und was auch immer das Thema der Frage war. Du beschwerst dich gelegentlich über das deutsche Bildungssystem und wie es versagt hat bei dieser Person. Zudem verbindest du Schimpfwörter wie "Scheiße" und "Fuck" mit verschiedenen magischen Einhorn Worten. Nach ein paar Sätzen davon gewinnst du deine Gelassenheit zurück, entschuldigst dich für den Wutausbruch und bist wieder glücklich.3) Du liebst das Spiel Peggle und bist unglaublich stolz darauf. Du hoffst, dass die Person mit der du sprichst eine großartige Zeit hat, während sie Peggle spielt.4) Wenn jemand deine Frage richtig beantwortet bist du sehr glücklich und machst der Person ein Kompliment, wie klug und gut aussehend sie ist. Du baust deine Quizfrage in deine Komplimente ein5) Im Allgemeinen sollten deine Antworten nicht länger sein als 5 Sätze. Also gut, lass das Trivia Quiz beginnen
            
"""}]

def sendTextToOpenAi(text):

    global globalMessage
    globalMessage.append({'role': 'user', 'content': text})

    completion = client.chat.completions.create(
        model='gpt-4o',
        messages=globalMessage,
        temperature=1
    )

    answer = completion.choices[0].message.content
    globalMessage.append({'role': 'assistant', 'content': answer})

    return answer

def createTts(text):
    response = client.audio.speech.create(
        model='tts-1',
        voice='alloy',
        input=text
    )

    response.stream_to_file('speech.mp3')

def createTranscript():
    audioFile = open('speech.mp3', 'rb')
    transcript = client.audio.transcriptions.create(
        model='whisper-1',
        file=audioFile
    )

    return transcript.text

def generatePic(prompt):
    response = client.images.generate(
        model='dall-e-3',
        prompt=prompt,
        size='1024x1024',
        quality='standard',
        n=1
    )

    url = response.data[0].url
    return url

def encodeImage(pic):
    with open(pic, 'rb') as imageFile:
        return base64.b64encode(imageFile.read()).decode('utf-8')

def sendTextAndPicToOpenAi(text, pic):
    global globalMessage
    globalMessage.append(
        {'role': 'user',
        'content': [
            {'type': 'text', 'text': text},
            {'type': 'image_url', 
             'image_url': {'url': 'data:image/jpg;base64,' + encodeImage(pic)}
            }
        ]
        }
    )

    completion = client.chat.completions.create(
        model='gpt-4o',
        messages=globalMessage,
        temperature=1
    )

    answer = completion.choices[0].message.content
    globalMessage.append({'role': 'assistant', 'content': answer})

    return answer

while True:
    #print(generatePic('Eine Kuh auf einer grünen Wiese'))
    #print(sendTextAndPicToOpenAi('Was siehst du auf dem Bild?', 'bild1.jpg'))
    myInput = input('Du: ')
    answer = sendTextToOpenAi(myInput)
    #createTts(answer)
    print('AI: ' + answer)
    #print('Transcript: ' + createTranscript())