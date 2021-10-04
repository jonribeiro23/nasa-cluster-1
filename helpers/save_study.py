import requests
from pprint import pprint
from models.db import DB

db = DB()

class SaveStudy:
	def save_correlation(self, data):
		try:
			# pprint(data['hits']['hits'])
			[db.save(self._change_key(x)) for x in data]
			
		except Exception as e:
			raise e
			return False
		else:
			return [self.most_commom_words(self._format_to_save(x)) for x in data]
			

	def most_commom_words(self, data):
		try:
			# r = requests.post(f'http://127.0.0.1:5002/commom-words', data=data)
			r = requests.post(f'https://octopus-nlp.herokuapp.com', data=data)
		except Exception as e:
			raise e
		else:
			return r.json()

	def _format_to_save(self, data):
		protocol_name = data['_source']['Study Protocol Name']
		tecnology_type = data['_source']['Study Assay Technology Type']
		title = data['_source']['Study Title']
		protocol_description = data['_source']['Study Protocol Description']
		description = data['_source']['Study Description']
		return {

			'study_id': data['_source']['Accession'],
			'title': title,
			'content': f"{protocol_name} {tecnology_type} {title} {protocol_description} {description}"

		}

	def _change_key(self, data):
		data['id'] = data.pop('_id')
		return data