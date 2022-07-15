from elasticsearch_dsl import Q

from blog.documents import ArticleDocument, UserDocument, CategoryDocument
from blog.serializers import (
    ArticleSerializer, UserSerializer, CategorySerializer
)

from search.paginated_es_view import PaginatedElasticSearchAPIView


class SearchUsers(PaginatedElasticSearchAPIView):
    serializer_class = UserSerializer
    document_class = UserDocument

    def generate_q_expression(self, query):
        return Q('bool',
                 should=[
                     Q('match', username=query),
                     Q('match', first_name=query),
                     Q('match', last_name=query),
                 ], minimum_should_match=1)


class SearchCategories(PaginatedElasticSearchAPIView):
    serializer_class = CategorySerializer
    document_class = CategoryDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'name',
                    'description',
                ], fuzziness='auto')


class SearchArticles(PaginatedElasticSearchAPIView):
    serializer_class = ArticleSerializer
    document_class = ArticleDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'title',
                    'author',
                    'type',
                    'content'
                ], fuzziness='auto')
