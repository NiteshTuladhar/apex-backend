from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.api.views import BaseCreatorCreateAPIView, BaseCreatorUpdateAPIView
from common.paginations import StandardResultsSetPagination
from common.permissions import IsAdminorSuperAdminorDirector
from exams.filters import ExamOnCourseFilter
from exams.models import Exam, ExamTemplate, ExamTemplateStatus, Question, Section

from ..api_common.serializers import ExamMiniSerializer
from .serializers import (
    ExamCreateSerializer,
    ExamDetailSerializer,
    ExamImageAdminSerializer,
    ExamListAdminSerializer,
    ExamListOverviewAdminSerializer,
    ExamOverviewCardSerializer,
    ExamRetrieveAdminSerializer,
    ExamTemplateCreateUpdateSerializer,
    ExamTemplateMiniSerializer,
    ExamTemplateRetrieveSerializer,
    ExamUpdateSerializer,
    OptionCUDSerializer,
    QuestionCreateSerializer,
    QuestionUpdateSerializer,
    SectionCRUDSerializer,
)


class QuestionCreateAPIView(CreateAPIView):
    serializer_class = QuestionCreateSerializer
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class QuestionUpdateAPIView(UpdateAPIView):
    serializer_class = QuestionUpdateSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionCRUDSerializer
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionCRUDSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class SectionDeleteAPIView(DestroyAPIView):
    serializer_class = SectionCRUDSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class ExamTemplateCreateAPIView(BaseCreatorCreateAPIView):
    serializer_class = ExamTemplateCreateUpdateSerializer
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class ExamTemplateDropdownListAPIView(ListAPIView):
    serializer_class = ExamTemplateMiniSerializer
    queryset = ExamTemplate.objects.all()
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]

    def get_queryset(self):
        return super().get_queryset().filter(status=ExamTemplateStatus.COMPLETED)


class ExamTemplateListAPIView(ListAPIView):
    serializer_class = ExamTemplateCreateUpdateSerializer
    queryset = ExamTemplate.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class ExamTemplateRetrieveAPIView(RetrieveAPIView):
    serializer_class = ExamTemplateRetrieveSerializer
    queryset = ExamTemplate.objects.all()
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class ExamTemplateUpdateAPIView(BaseCreatorUpdateAPIView):
    serializer_class = ExamTemplateCreateUpdateSerializer
    queryset = ExamTemplate.objects.all()
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class ExamTemplateDeleteAPIView(DestroyAPIView):
    queryset = ExamTemplate.objects.all()
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class OptionCreateAPIView(CreateAPIView):
    serializer_class = OptionCUDSerializer
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class OptionUpdateAPIView(UpdateAPIView):
    serializer_class = OptionCUDSerializer
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]
    queryset = Question.objects.all()


class OptionsDeleteAPIView(DestroyAPIView):
    serializer_class = OptionCUDSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class QuestionDeleteAPIView(DestroyAPIView):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class ExamCreateAPIView(BaseCreatorCreateAPIView):
    serializer_class = ExamCreateSerializer
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class ExamUpdateAPIView(BaseCreatorUpdateAPIView):
    serializer_class = ExamUpdateSerializer
    queryset = Exam.objects.all()
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class ExamDeleteAPIView(DestroyAPIView):
    queryset = Exam.objects.all()
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class ExamListAPIView(ListAPIView):
    serializer_class = ExamListAdminSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filterset_class = ExamOnCourseFilter
    queryset = Exam.objects.all()
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class ExamListOverviewAPIView(ExamListAPIView):
    serializer_class = ExamListOverviewAdminSerializer


class ExamOverviewCardAPIView(GenericAPIView):
    serializer_class = ExamOverviewCardSerializer
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]
    queryset = Exam.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)


class ExamDropdownListAPIView(ListAPIView):
    serializer_class = ExamMiniSerializer
    queryset = Exam.objects.all()
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class ExamRetrieveAPIView(RetrieveAPIView):
    serializer_class = ExamRetrieveAdminSerializer
    queryset = Exam.objects.all()
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]


class ExamImageUploadAPIView(CreateAPIView):
    serializer_class = ExamImageAdminSerializer
    # permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]

    def perform_create(self, serializer):
        exam_id = self.kwargs.get("exam_id")
        exam = get_object_or_404(Exam, id=exam_id)
        return serializer.save(exam=exam)


class ExamDetailAPIView(RetrieveAPIView):
    serializer_class = ExamDetailSerializer
    queryset = Exam.objects.all()
    permission_classes = [IsAuthenticated & IsAdminorSuperAdminorDirector]
