from os import environ
from google.cloud import translate

def translate_text(text):
	project_id = environ.get("PROJECT_ID", "")
	assert project_id
	parent = f"projects/{project_id}"
	client = translate.TranslationServiceClient()

	target_language_code = "pt"

	response = client.translate_text(
	    contents=[text],
	    target_language_code=target_language_code,
	    parent=parent,
	)

	for translation in response.translations:
	    return(translation.translated_text)