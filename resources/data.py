from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from helpers.save_study import SaveStudy
import json
from pprint import pprint
from models.db import DB

db = DB()
from models.search import (
    GeneLab,
    ImagesVideos,
    TechPort,
    CatalogData
)

gene_lab = GeneLab()
images_videos = ImagesVideos()
tech_port = TechPort()
catalogue_data = CatalogData()


class SimpleSearch(Resource):
    def get(self, term):
        data = gene_lab.search(term)

        if data:
            sv = SaveStudy()
            related = sv.save_correlation(data['hits']['hits'])
            [x.pop('_id') if '_id' in x.keys() else '' for x in data['hits']['hits']]
            data['related'] = related
            return {'message': 'ok', 'content': data}, 200
        return {'message': 'err'}, 501


class IVSearch(Resource):
    def get(self, term):
        data = images_videos.search(term)
        if data:
            return {'message': 'ok', 'content': data}, 200
        return {'message': 'err'}, 501


class TPSearch(Resource):
    def get(self):
        data = tech_port.search()
        if data:
            return {'message': 'ok', 'content': data}, 200
        return {'message': 'err'}, 501


class ProjectSearch(Resource):
    def get(self, _id):
        data = tech_port.search_project(_id)
        if data:
            return {'message': 'ok', 'content': data}, 200
        return {'message': 'err'}, 501


class CDSearch(Resource):
    def get(self, term):
        data = catalogue_data.search(term)
        if data:
            return {'message': 'ok', 'content': data}, 200
        return {'message': 'err'}, 501


class Related(Resource):
    def get(self, _id):
        data = db.get_article(_id)
        if data:
            return {'message': 'ok', 'content': data}, 200
        return {'message': 'err'}, 501



class ListCoursesByInstructor(Resource):
    def get(self, _id):
        # course = CourseModel()
        # all_courses = course.list_courses_by_instructor(_id)
        # if all_courses:
        #     return {'message': 'ok', 'courses': all_courses}
        # return {'message': 'Erro ao listar cursos.'}
        pass
