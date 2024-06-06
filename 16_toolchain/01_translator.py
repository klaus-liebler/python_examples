from googletrans import Translator
translator = Translator()
spanische_übersetzung=translator.translate('Guten Tag. Ich möchte eine Paella essen.', src='de', dest='es').text;
print(spanische_übersetzung)